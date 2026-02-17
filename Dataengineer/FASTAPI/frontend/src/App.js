import React, { useEffect, useState } from "react";

const API = "http://127.0.0.1:8000";

function App() {
  const [products, setProducts] = useState([]);
  const [filtered, setFiltered] = useState([]);
  const [loading, setLoading] = useState(false);

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [quantity, setQuantity] = useState("");
  const [search, setSearch] = useState("");

  // ================= LOAD =================
  const loadProducts = async () => {
    setLoading(true);
    const res = await fetch(`${API}/products`);
    const data = await res.json();
    setProducts(data);
    setFiltered(data);
    setLoading(false);
  };

  useEffect(() => {
    loadProducts();
  }, []);

  // ================= SEARCH =================
  useEffect(() => {
    const f = products.filter(
      (p) =>
        p.name.toLowerCase().includes(search.toLowerCase()) ||
        (p.description || "")
          .toLowerCase()
          .includes(search.toLowerCase())
    );
    setFiltered(f);
  }, [search, products]);

  // ================= ADD =================
  const addProduct = async () => {
    if (!name || !price) {
      alert("Name and Price required");
      return;
    }

    await fetch(`${API}/products`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name,
        description,
        price: parseFloat(price),
        quantity: parseInt(quantity || 0),
      }),
    });

    setName("");
    setDescription("");
    setPrice("");
    setQuantity("");
    loadProducts();
  };

  // ================= DELETE =================
  const deleteProduct = async (id) => {
    if (!window.confirm("Delete this product?")) return;

    await fetch(`${API}/products/${id}`, {
      method: "DELETE",
    });

    loadProducts();
  };

  return (
    <div style={styles.page}>
      <h1 style={styles.title}>📦 Sharaazians Trac</h1>

      {/* 🔍 SEARCH */}
      <div style={styles.card}>
        <input
          style={styles.search}
          placeholder="🔍 Search by name or description..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>

      {/* ➕ ADD */}
      <div style={styles.card}>
        <h2>Add Product</h2>

        <div style={styles.inputRow}>
          <input
            style={styles.input}
            placeholder="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />

          <input
            style={styles.input}
            placeholder="Description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />

          <input
            style={styles.input}
            placeholder="Price"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
          />

          <input
            style={styles.input}
            placeholder="Quantity"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
          />

          <button style={styles.addBtn} onClick={addProduct}>
            Add
          </button>
        </div>
      </div>

      {/* 📋 TABLE */}
      <div style={styles.card}>
        <h2>Products ({filtered.length})</h2>

        {loading ? (
          <div style={styles.loader}>Loading...</div>
        ) : filtered.length === 0 ? (
          <div style={styles.empty}>No products found</div>
        ) : (
          <table style={styles.table}>
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Description</th>
                <th>Price</th>
                <th>Qty</th>
                <th>Action</th>
              </tr>
            </thead>

            <tbody>
              {filtered.map((p) => (
                <tr key={p.id}>
                  <td>{p.id}</td>
                  <td>{p.name}</td>
                  <td>{p.description}</td>
                  <td>${p.price}</td>
                  <td>{p.quantity}</td>
                  <td>
                    <button
                      style={styles.deleteBtn}
                      onClick={() => deleteProduct(p.id)}
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}

export default App;

/* ================= 🎨 STYLES ================= */

const styles = {
  page: {
    minHeight: "100vh",
    padding: "40px",
    background: "linear-gradient(135deg, #6a5acd, #7b68ee)",
    fontFamily: "Arial",
  },

  title: {
    color: "white",
    marginBottom: "25px",
  },

  card: {
    background: "white",
    padding: "25px",
    borderRadius: "16px",
    marginBottom: "25px",
    boxShadow: "0 10px 25px rgba(0,0,0,0.15)",
  },

  search: {
    width: "100%",
    padding: "12px",
    borderRadius: "10px",
    border: "1px solid #ccc",
    fontSize: "14px",
  },

  inputRow: {
    display: "flex",
    gap: "10px",
    flexWrap: "wrap",
    marginTop: "15px",
  },

  input: {
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #ccc",
    minWidth: "140px",
  },

  addBtn: {
    background: "#6a5acd",
    color: "white",
    border: "none",
    padding: "10px 18px",
    borderRadius: "8px",
    cursor: "pointer",
    fontWeight: "bold",
  },

  deleteBtn: {
    background: "#e74c3c",
    color: "white",
    border: "none",
    padding: "6px 12px",
    borderRadius: "6px",
    cursor: "pointer",
  },

  loader: {
    padding: "30px",
    textAlign: "center",
    fontWeight: "bold",
  },

  empty: {
    padding: "30px",
    textAlign: "center",
    color: "#777",
  },

  table: {
    width: "100%",
    borderCollapse: "collapse",
    marginTop: "15px",
  },
};
