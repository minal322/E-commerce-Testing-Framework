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

    def go_to_cart(self):
        # Go to Cart
        self.driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()

        # Pay with stripe
        self.driver.find_element(By.XPATH, "//div/button[text()='Pay with Stripe']").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/span[.='Pay E-commerce']")))
        message = self.driver.find_element(By.XPATH, ".//div/span[.='Pay E-commerce']").text
        print(message)

    def checkout(self,email,shipping_method,card_details,card_holder_name,country,address,city,pincode,state):
        #Enter User details
        self.driver.find_element(*self.email_input).send_keys(email)
        ship_amount =""

        #Select mode of shipping
        if "Fast" in shipping_method or "fast" in shipping_method:
            print("inside fast")
            self.driver.find_element(By.XPATH,"//div[.='Fast Shipping in India']").click()
            # //div[@class='ShippingSelector-price']/span[.='₹60.00']
            ship_amount = self.driver.find_element(By.XPATH,"//div[@class='ShippingSelector-price']/span[.='₹60.00']").text
            print(shipping_method)
            print(ship_amount)
        elif "Free" in shipping_method or "free" in shipping_method:
            #//label[contains(@aria-label,'Free Shipping')]
            self.driver.find_element(By.XPATH, "//label[contains(@aria-label,'Free Shipping')]").click()

        #Enter card Details
        self.driver.find_element(By.ID,"cardNumber").send_keys(card_details["card_number"])
        self.driver.find_element(By.ID, "cardExpiry").send_keys(card_details["expiry_date"])
        self.driver.find_element(By.ID, "cardCvc").send_keys(card_details["cvc"])
        self.driver.find_element(By.ID, "billingName").send_keys(card_holder_name)

        #Enter Country
        select_obj = Select(self.driver.find_element(By.CSS_SELECTOR,".Select-source"))
        select_obj.select_by_visible_text(country)

        #Enter Address
        address1= self.driver.find_element(By.ID,"billingAddressLine1")
        self.driver.execute_script("arguments[0].setAttribute('autocomplete', 'off')",address1 )
        address1.send_keys(address)
        #self.driver.find_element(By.TAG_NAME, "body").click()

        # self.driver.find_element(By.ID, "billingAddressLine2").send_keys(address)
        # self.driver.find_element(By.TAG_NAME, "body").click()
        self.driver.find_element(By.ID, "billingLocality").send_keys(city)
        self.driver.find_element(By.ID, "billingPostalCode").send_keys(pincode)

        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        select_obj = Select(self.driver.find_element(By.ID, "billingAdministrativeArea"))
        select_obj.select_by_visible_text(state)
        time.sleep(5)

        print("Entered all details")


    def submit_payment(self):
        #go to end of page

        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        time.sleep(2)
        print("Submit payment")
        #self.driver.find_element(By.TAG_NAME, "body").click()
        #click on pay button
        self.driver.find_element(By.CSS_SELECTOR,".SubmitButton").click()
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "h2")))
        message = self.driver.find_element(By.TAG_NAME, "h2").text
        print(message)

        assert not "Thank you" in message


