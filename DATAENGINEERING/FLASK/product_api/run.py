"""
Application entry point
Author: Shaziya Sayed
"""

from app import create_app

# Create Flask app
app = create_app()


# =========================================================
# Health/Home endpoint
# =========================================================
@app.route("/", methods=["GET"])
def home():
    return {"message": "Flask Product API is running"}


# =========================================================
# Run server
# =========================================================
if __name__ == "__main__":
    app.run(debug=True)
