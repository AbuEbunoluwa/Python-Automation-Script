from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware # Import the middleware

app = FastAPI(title="Masterpiece Home Essentials Marketplace API")

# Allow your local frontend to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins for local testing
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
async def get_products():
    return [
        {"id": 1, "name": "Sectional Sofa", "category": "Living Room", "price": 750},
        {"id": 1, "name": "Sectional Sofa", "category": "Living Room", "price": 750},
        {"id": 2, "name": "Air Fryer", "category": "Kitchen", "price": 120},
        {"id": 3, "name": "Memory Foam Mattress", "category": "Bedroom", "price": 450},
        {"id": 4, "name": "Smart Coffee Maker", "category": "Kitchen", "price": 90},
        {"id": 5, "name": "Robot Vacuum", "category": "Cleaning", "price": 300}, 
         # ... your other 29 items ...
    ]
# --- DATA MODELS ---
class Product(BaseModel):
    id: int
    name: str
    category: str  # e.g., Kitchen, Bedroom, Kids Room
    price: float
    stock: int

class Order(BaseModel):
    product_ids: List[int]
    customer_email: str

# --- THE "30 HOME ESSENTIALS" DATABASE (Mock) ---
products = [
    # Living Room
    {"id": 1, "name": "Sectional Sofa", "category": "Living Room", "price": 899.99, "stock": 5},
    {"id": 2, "name": "Coffee Table", "category": "Living Room", "price": 149.99, "stock": 12},
    # Bedroom
    {"id": 3, "name": "Memory Foam Mattress", "category": "Bedroom", "price": 499.00, "stock": 10},
    {"id": 4, "name": "Nightstand", "category": "Bedroom", "price": 75.50, "stock": 20},
    # Kitchen
    {"id": 5, "name": "Air Fryer", "category": "Kitchen", "price": 120.00, "stock": 15},
    {"id": 6, "name": "Knife Set", "category": "Kitchen", "price": 45.00, "stock": 30},
    # Laundry
    {"id": 7, "name": "Steam Iron", "category": "Laundry", "price": 35.00, "stock": 25},
    # Garage
    {"id": 8, "name": "Tool Organizer", "category": "Garage", "price": 60.00, "stock": 8},
    # Kids Room
    {"id": 9, "name": "Toy Storage Bin", "category": "Kids Room", "price": 25.00, "stock": 50},
    # ... (Add more to reach 30)
]

# --- API ENDPOINTS ---

@app.get("/")
def read_root():
    return {"message": "Welcome to the Home Essentials API"}

@app.get("/products", response_model=List[Product])
def get_products(category: Optional[str] = None):
    """Returns products, optionally filtered by category."""
    if category:
        return [p for p in products if p["category"].lower() == category.lower()]
    return products

@app.post("/checkout")
def checkout(order: Order):
    """Handles the checkout functionality."""
    total_price = 0
    for p_id in order.product_ids:
        product = next((p for p in products if p["id"] == p_id), None)
        if not product or product["stock"] <= 0:
            raise HTTPException(status_code=400, detail=f"Product {p_id} out of stock or not found")
        
        total_price += product["price"]
        product["stock"] -= 1 # Simple stock reduction
        
    return {
        "status": "Success",
        "total": round(total_price, 2),
        "message": f"Order confirmed for {order.customer_email}!"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
