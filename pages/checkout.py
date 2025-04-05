from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time


class CheckoutPayment:
    def __init__(self,driver):
        self.driver = driver
        self.go_cart_button = (By.CSS_SELECTOR, ".cart-icon")
        self.payment_button = (By.XPATH, "//div/button[text()='Pay with Stripe']")
        self.email_input= (By.ID,"email")
        self.fast_shipping_mode = (By.XPATH,"//div[.='Fast Shipping in India']")
        self.free_shipping_mode = (By.XPATH, "//label[contains(@aria-label,'Free Shipping')]")
        self.card_number = (By.ID,"cardNumber")
        self.card_expiry = (By.ID, "cardExpiry")
        self.card_cvc = (By.ID, "cardCvc")
        self.card_holder = (By.ID, "billingName")
        self.country = (By.CSS_SELECTOR,".Select-source")
        self.city =(By.ID, "billingLocality")
        self.pincode = (By.ID, "billingPostalCode")
        self.address = (By.ID,"billingAddressLine1")
        self.submit_payment_button = (By.CSS_SELECTOR,".SubmitButton")

    def go_to_cart(self):
        # Go to Cart button
        self.driver.find_element(*self.go_cart_button).click()
        # Pay with stripe button
        self.driver.find_element(*self.payment_button).click()

    def checkout(self,new_data_list):
        shipping_method = new_data_list["shipping_method"]
        card_details = new_data_list["card_details"]

        #Enter User details
        self.driver.find_element(*self.email_input).send_keys(new_data_list["email"])
        ship_amount =""

        #Select mode of shipping
        if "Fast" in shipping_method or "fast" in shipping_method:
            print("inside fast")
            self.driver.find_element(*self.fast_shipping_mode).click()
            ship_amount = self.driver.find_element(By.XPATH,"//div[@class='ShippingSelector-price']/span[.='₹60.00']").text
            print(shipping_method)
            print(ship_amount)
        elif "Free" in shipping_method or "free" in shipping_method:
            #//label[contains(@aria-label,'Free Shipping')]
            self.driver.find_element(*self.free_shipping_mode).click()
            print(shipping_method)

        #Enter card Details
        self.driver.find_element(*self.card_number).send_keys(card_details["card_number"])
        self.driver.find_element(*self.card_expiry).send_keys(card_details["expiry_date"])
        self.driver.find_element(*self.card_cvc).send_keys(card_details["cvc"])
        self.driver.find_element(*self.card_holder).send_keys(new_data_list["card_holder_name"])

        #Enter Country
        select_obj = Select(self.driver.find_element(*self.country))
        select_obj.select_by_visible_text(new_data_list["country"])

        #Enter Address
        address1= self.driver.find_element(*self.address)
        self.driver.execute_script("arguments[0].setAttribute('autocomplete', 'off')",address1 )
        address1.send_keys(new_data_list["address"])
        #self.driver.find_element(By.TAG_NAME, "body").click()

        # self.driver.find_element(By.ID, "billingAddressLine2").send_keys(address)
        # self.driver.find_element(By.TAG_NAME, "body").click()
        self.driver.find_element(*self.city).send_keys(new_data_list["city"])
        self.driver.find_element(*self.pincode).send_keys(new_data_list["pincode"])

        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        state_elements = self.driver.find_elements(By.ID, "billingAdministrativeArea")
        if state_elements and state_elements[0].is_displayed():
            select_obj = Select(state_elements[0])
            select_obj.select_by_visible_text(new_data_list["state"])
        time.sleep(5)

    def submit_payment(self):
        #go to end of page

        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        time.sleep(2)
        print("Submit payment")
        self.driver.find_element(By.TAG_NAME, "body").click()
        #click on pay button
        self.driver.find_element(*self.submit_payment_button).click()
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "h2")))
        message = self.driver.find_element(By.TAG_NAME, "h2").text
        print(message)

        assert not "Thank you" in message


