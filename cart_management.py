class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                print(f"✅ Updated {product.name} quantity to {item.quantity}")
                return
        self.items.append(CartItem(product, quantity))
        print(f"✅ {product.name} added to cart")

    def remove_item(self, product_name):
        for item in self.items:
            if item.product.name == product_name:
                self.items.remove(item)
                print(f"❌ {product_name} removed from cart")
                return
        print("⚠️ Item not found")

    def update_quantity(self, product_name, quantity):
        for item in self.items:
            if item.product.name == product_name:
                item.quantity = quantity
                print(f"🔄 {product_name} quantity updated to {quantity}")
                return
        print("⚠️ Item not found")

    def calculate_total(self):
        return sum(item.get_total_price() for item in self.items)

    def show_cart(self):
        if not self.items:
            print("\n🛒 Cart is empty")
            return

        print("\n🛒 Your Cart:")
        for item in self.items:
            print(f"{item.product.name} x {item.quantity} = ₹{item.get_total_price()}")
        print(f"💰 Total: ₹{self.calculate_total()}")

    def checkout(self):
        if not self.items:
            print("⚠️ Cart is empty!")
            return

        total = self.calculate_total()
        print(f"\n💳 Total amount: ₹{total}")
        print("✅ Payment successful! Thank you for shopping.")
        self.items.clear()


# 🧾 Product Catalog
products = {
    1: Product("Laptop", 50000),
    2: Product("Mouse", 500),
    3: Product("Keyboard", 1500),
    4: Product("Headphones", 2000)
}


# ▶️ Main Program
def main():
    cart = ShoppingCart()

    while True:
        print("\n===== MENU =====")
        print("1. Show Products")
        print("2. Add to Cart")
        print("3. Remove Item")
        print("4. Update Quantity")
        print("5. View Cart")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n🛍️ Products:")
            for pid, product in products.items():
                print(f"{pid}. {product.name} - ₹{product.price}")

        elif choice == "2":
            pid = int(input("Enter product id: "))
            qty = int(input("Enter quantity: "))
            if pid in products:
                cart.add_item(products[pid], qty)
            else:
                print("⚠️ Invalid product")

        elif choice == "3":
            name = input("Enter product name to remove: ")
            cart.remove_item(name)

        elif choice == "4":
            name = input("Enter product name: ")
            qty = int(input("Enter new quantity: "))
            cart.update_quantity(name, qty)

        elif choice == "5":
            cart.show_cart()

        elif choice == "6":
            cart.checkout()

        elif choice == "7":
            print("👋 Exiting...")
            break

        else:
            print("⚠️ Invalid choice")


if __name__ == "__main__":
    main()