# Program
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def update_product(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].quantity += quantity
        else:
            print(f"Product with ID {product_id} not found.")

    def display_inventory(self):
        print("Inventory:")
        print("+-----------+---------------+--------+----------+")
        print("| Product ID | Product Name  | Price  | Quantity |")
        print("+-----------+---------------+--------+----------+")
        for product in self.products.values():
            print(f"| {product.product_id:>11} | {product.name:15} | {product.price:6.2f} | {product.quantity:10} |")
        print("+-----------+---------------+--------+----------+")

class Sale:
    def __init__(self, sale_id):
        self.sale_id = sale_id
        self.products = []
        self.total_price = 0

    def add_product(self, product, quantity):
        self.products.append((product, quantity))
        self.total_price += product.price * quantity

class SalesManager:
    def __init__(self, inventory):
        self.inventory = inventory
        self.sales = {}

    def process_sale(self):
        sale_id = int(input("Enter Sale ID: "))
        sale = Sale(sale_id)

        while True:
            product_id = input("Enter Product ID to sell (or 'done' to finish): ")
            if product_id.lower() == "done":
                break

            if product_id not in self.inventory.products:
                print(f"Product with ID {product_id} not found.")
                continue

            product = self.inventory.products[product_id]
            quantity = int(input(f"Enter quantity for {product.name}: "))

            if quantity > product.quantity:
                print(f"Insufficient stock for {product.name}. Only {product.quantity} available.")
                continue

            sale.add_product(product, quantity)
            self.inventory.update_product(product_id, -quantity)

        self.sales[sale_id] = sale
        print(f"Sale {sale_id} recorded successfully.")

    def display_sales_report(self):
        print("Sales Report:")
        print("+-----------+---------------+---------------+---------------+----------+")
        print("| Sale ID   | Product ID    | Product Name  | Quantity Sold | Total Price |")
        print("+-----------+---------------+---------------+---------------+----------+")
        for sale_id, sale in self.sales.items():
            for product, quantity in sale.products:
                print(f"| {sale_id:>11} | {product.product_id:>13} | {product.name:15} | {quantity:15} | {sale.total_price:10.2f} |")
        print("+-----------+---------------+---------------+---------------+----------+")

class ShopSystem:
    def __init__(self):
        self.inventory = Inventory()
        self.sales_manager = SalesManager(self.inventory)
        self.load_products()

    def load_products(self):
        products = [
            Product("101", "Soap", 20.0, 50),
            Product("102", "Shampoo", 120.0, 30),
            Product("103", "Toothpaste", 60.0, 40),
            Product("104", "Rice", 500.0, 20),
            Product("105", "Sugar", 45.0, 25)
        ]

        for product in products:
            self.inventory.add_product(product)

    def run(self):
        while True:
            print("--- Small Shop Management System ---")
            print("1. View Inventory")
            print("2. Add Product to Inventory")
            print("3. Process a Sale")
            print("4. View Sales Report")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.inventory.display_inventory()
            elif choice == "2":
                product_id = input("Enter Product ID: ")
                name = input("Enter Product Name: ")
                price = float(input("Enter Product Price: "))
                quantity = int(input("Enter Product Quantity: "))
                product = Product(product_id, name, price, quantity)
                self.inventory.add_product(product)
                print("Product added to the inventory.")
            elif choice == "3":
                self.sales_manager.process_sale()
            elif choice == "4":
                self.sales_manager.display_sales_report()
            elif choice == "5":
                print("Exiting the system...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    shop_system = ShopSystem()
    shop_system.run()
