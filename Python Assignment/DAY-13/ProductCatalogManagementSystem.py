import xml.etree.ElementTree as ET

PRODUCT_FILE = "products.xml"


def load_products():
    try:
        tree = ET.parse(PRODUCT_FILE)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        root = ET.Element("products")
        tree = ET.ElementTree(root)
        tree.write(PRODUCT_FILE)
        return root


def save_products(root):
    tree = ET.ElementTree(root)
    tree.write(PRODUCT_FILE)


def add_product(product):
    root = load_products()
    product_element = ET.SubElement(root, "product")
    for key, value in product.items():
        ET.SubElement(product_element, key).text = value
    save_products(root)
    print("Product added successfully.")


def update_product(product_id, new_data):
    root = load_products()
    for product in root.findall("product"):
        if product.find("id").text == product_id:
            for key, value in new_data.items():
                product.find(key).text = value
            save_products(root)
            print("Product updated successfully.")
            return
    print("Product not found.")


def delete_product(product_id):
    root = load_products()
    for product in root.findall("product"):
        if product.find("id").text == product_id:
            root.remove(product)
            save_products(root)
            print("Product deleted successfully.")
            return
    print("Product not found.")


def get_product(product_id):
    root = load_products()
    for product in root.findall("product"):
        if product.find("id").text == product_id:
            print("Product Details:")
            for child in product:
                print(f"{child.tag}: {child.text}")
            return
    print("Product not found.")


def main():
    while True:
        print("\nProduct Catalog Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Get Product Details")
        print("5. Export Product Catalog to XML")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            product = {}
            product["id"] = input("Enter product ID: ")
            product["name"] = input("Enter product name: ")
            product["price"] = input("Enter product price: ")
            add_product(product)
        elif choice == "2":
            product_id = input("Enter product ID to update: ")
            new_data = {}
            new_data["name"] = input("Enter new name: ")
            new_data["price"] = input("Enter new price: ")
            update_product(product_id, new_data)
        elif choice == "3":
            product_id = input("Enter product ID to delete: ")
            delete_product(product_id)
        elif choice == "4":
            product_id = input("Enter product ID to get details: ")
            get_product(product_id)
        elif choice == "5":
            print("Exporting product catalog to XML...")
            root = load_products()
            save_products(root)
            print("Product catalog exported successfully.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
