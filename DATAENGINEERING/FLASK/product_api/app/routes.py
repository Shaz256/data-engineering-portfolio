from flask import Blueprint, request, jsonify
from app import db
from app.models import Product

product_bp = Blueprint("products", __name__)


# =========================================================
# GET all products
# =========================================================
@product_bp.route("/products", methods=["GET"])
def get_products():
    """
    Get all products
    ---
    responses:
      200:
        description: List of products
    """
    products = Product.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "quantity": p.quantity,
        }
        for p in products
    ])


# =========================================================
# CREATE product
# =========================================================
@product_bp.route("/products", methods=["POST"])
def add_product():
    """
    Add a new product
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          properties:
            name:
              type: string
            price:
              type: number
            quantity:
              type: integer
    responses:
      201:
        description: Product created
    """
    data = request.json

    product = Product(**data)
    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product added"}), 201


# =========================================================
# UPDATE product
# =========================================================
@product_bp.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """
    Update a product
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
    """
    product = Product.query.get_or_404(product_id)
    data = request.json

    product.name = data.get("name", product.name)
    product.price = data.get("price", product.price)
    product.quantity = data.get("quantity", product.quantity)

    db.session.commit()

    return jsonify({"message": "Product updated"})


# =========================================================
# DELETE product
# =========================================================
@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """
    Delete a product
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
    """
    product = Product.query.get_or_404(product_id)

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted"})
