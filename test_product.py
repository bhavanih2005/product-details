from product import product_details

def test_employee_details():
    expected_output = (
        "Product Name: iphone\n"
        "Product ID: I14\n"
        "Quantity: 1\n"
        "Price: 70000"
    )
    assert product_details("iphone", "I14", 1, 70000) == expected_output