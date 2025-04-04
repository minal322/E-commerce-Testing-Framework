from pages.shopping import ShopProducts
from pages.checkout import CheckoutPayment


def test_online_shopping(browserInstance):
    driver = browserInstance
    product_name = "OnePlus 9 Pro"
    quantity = 2
    email = "patilminal322@gmail.com"
    shipping_method ="Fast shipping"
    card_details = {"card_number":"4242424242424242", "expiry_date": "03/26" , "cvc":"235"}
    card_holder_name = "Minal Patil"
    country = "India"
    address= "bs"
    city = "Pune"
    pincode= "411048"
    state = "Maharashtra"

    #shop product and add to cart
    shop_obj = ShopProducts(driver)
    shop_obj.select_product(product_name)
    shop_obj.add_product_to_cart(quantity)

    #Checkout and confirmation
    checkout = CheckoutPayment(driver)
    checkout.go_to_cart()
    checkout.checkout(email,shipping_method,card_details,card_holder_name,country,address,city,pincode,state)
    checkout.submit_payment()