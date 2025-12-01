import pytest
def product_details(name, prod_id, quantity, price):
    result = (
        f"Product Name: {name}\n"
        f"Product ID: {prod_id}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result

if __name__ == "__main__":
    # Sample values
    name = "iphone"
    prod_id = "I14"
    quantity = 1
    price = 70000

    print(product_details(name, prod_id, quantity, price))