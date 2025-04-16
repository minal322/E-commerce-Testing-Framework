from pages.shopping import ShopProducts
from pages.checkout import CheckoutPayment
import pytest
import json
from pathlib import Path
file_path = Path(__file__).parent.parent / "config" / "input_data.json"
print(file_path)

with open(file_path) as curr_file:
    test_data = json.load(curr_file)
    data_list = test_data["datas"]
    print(data_list)

@pytest.mark.parametrize("new_data_list",data_list)
def test_online_shopping(browserInstance,new_data_list):
    driver = browserInstance

    #shop product and add to cart
    shop_obj = ShopProducts(driver)
    shop_obj.select_product(new_data_list["product_name"])
    shop_obj.add_product_to_cart(int(new_data_list["quantity"]))

    #Checkout and confirmation
    checkout = CheckoutPayment(driver)
    checkout.go_to_cart()
    checkout.checkout(new_data_list)
    checkout.submit_payment()