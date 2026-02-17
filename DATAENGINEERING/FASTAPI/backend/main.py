from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from DATAENGINEERING.FASTAPI.backend import models, schemas
from DATAENGINEERING.FASTAPI.backend.database import engine, get_db

# ==============================
# Create tables
# ==============================
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Manager API")

# ==============================
# CORS
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# GET products (pagination + search + sorting)
# ==============================
@app.get("/products", response_model=list[schemas.ProductResponse])
def get_products(
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    sort_by: str = "id",
    db: Session = Depends(get_db),
):

    query = db.query(models.Product)

    # 🔍 Search by name
    if search:
        query = query.filter(models.Product.name.ilike(f"%{search}%"))

    # 🔽 Sorting (safe check)
    if hasattr(models.Product, sort_by):
        query = query.order_by(getattr(models.Product, sort_by))

    products = query.offset(skip).limit(limit).all()
    return products


# ==============================
# ADD product
# ==============================
@app.post(
    "/products",
    response_model=schemas.ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# ==============================
# UPDATE product
# ==============================
@app.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(
    product_id: int,
    product: schemas.ProductUpdate,
    db: Session = Depends(get_db),
):
    db_product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = product.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product


# ==============================
# DELETE product
# ==============================
@app.delete(
    "/products/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
