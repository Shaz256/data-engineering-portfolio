from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from backend import models
from backend.database import engine, get_db

# ✅ create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Manager API")

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==============================
# GET products
# ==============================
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()


# ==============================
# ADD product
# ==============================
@app.post("/products")
def add_product(product: dict, db: Session = Depends(get_db)):
    db_product = models.Product(**product)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# ==============================
# DELETE product
# ==============================
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if product:
        db.delete(product)
        db.commit()

    return {"message": "Deleted"}
