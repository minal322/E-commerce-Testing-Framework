from pages.shopping import ShopProducts
from pages.checkout import CheckoutPayment
import pytest
import time
import json
from pathlib import Path
file_path = Path(__file__).parent.parent / "config" / "input_data.json"
print(file_path)

with open(file_path) as curr_file:
    test_data = json.load(curr_file)
    data_list = test_data["multiple_datas"]
    print(data_list)

@pytest.mark.parametrize("new_data_list",data_list)
def test_online_shopping(browserInstance,new_data_list):
    driver = browserInstance

    #shop product and add to cart
    shop_obj = ShopProducts(driver)
    #print(new_data_list[0]["product_details"])
    print(new_data_list)
    for current_prod in new_data_list["product_details"]:
        print(current_prod)
        shop_obj.select_product(current_prod["product_name"])
        shop_obj.add_product_to_cart(int(current_prod["quantity"]))
        shop_obj.go_to_home()

    #Checkout and confirmation
    checkout = CheckoutPayment(driver)
    checkout.go_to_cart()
    checkout.checkout(new_data_list)
    checkout.submit_payment()