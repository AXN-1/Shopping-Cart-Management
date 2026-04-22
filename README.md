# 🛒 Shopping Cart Management System (Python)

A simple command-line based shopping cart application built in Python. This project demonstrates object-oriented programming concepts such as classes, encapsulation, and basic data handling.

---

## 📌 Features

* View available products
* Add items to the cart
* Remove items from the cart
* Update item quantity
* View cart details with total price
* Checkout and clear cart

---

## 🧱 Project Structure

### 1. **Product Class**

Represents a product with:

* `name`: Name of the product
* `price`: Price of the product

---

### 2. **CartItem Class**

Represents an item in the cart:

* `product`: Product object
* `quantity`: Number of units

**Methods:**

* `get_total_price()` → Returns total price for that item

---

### 3. **ShoppingCart Class**

Handles all cart operations.

**Methods:**

* `add_item(product, quantity)` → Adds or updates item quantity
* `remove_item(product_name)` → Removes item from cart
* `update_quantity(product_name, quantity)` → Updates item quantity
* `calculate_total()` → Returns total cart value
* `show_cart()` → Displays all items in the cart
* `checkout()` → Displays total and clears cart

---

## 🛍️ Product Catalog

Predefined products in the system:

| ID | Product    | Price (₹) |
| -- | ---------- | --------- |
| 1  | Laptop     | 50000     |
| 2  | Mouse      | 500       |
| 3  | Keyboard   | 1500      |
| 4  | Headphones | 2000      |

---

## ▶️ How to Run

1. Make sure you have Python installed (Python 3.x recommended)
2. Save the file as `cart_management.py`
3. Run the script:

```bash
python cart_management.py
```

---

## 📋 Menu Options

```
1. Show Products
2. Add to Cart
3. Remove Item
4. Update Quantity
5. View Cart
6. Checkout
7. Exit
```

---

## 💡 Example Usage

* Select option `1` to view products
* Choose option `2` to add items
* View cart with option `5`
* Complete purchase using option `6`

---

## ⚙️ Concepts Used

* Object-Oriented Programming (OOP)
* Classes and Objects
* Lists and Dictionaries
* Loops and Conditional Statements
* User Input Handling

---

## 🚀 Possible Improvements

* Add persistent storage (save cart to file/database)
* Implement user authentication
* Add GUI (Tkinter / Web app)
* Support discount coupons
* Improve error handling and input validation

---

## 📄 License

This project is open-source and free to use for learning purposes.

---

## 👨‍💻 Author

Developed as a beginner-friendly Python project to understand shopping cart logic and OOP fundamentals.
