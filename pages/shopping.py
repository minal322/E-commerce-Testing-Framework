from selenium.webdriver.common.by import By


class ShopProducts:
    def __init__(self,driver):
        self.driver = driver
        self.all_products= (By.CSS_SELECTOR, "div[class='product-card']")
        self.each_product = (By.CSS_SELECTOR, "p[class='product-name']")
        self.increment_quantity= (By.CSS_SELECTOR, "p span[class='plus']")
        self.add_to_cart_button = (By.CSS_SELECTOR, ".add-to-cart")
        self.home_page_link = (By.LINK_TEXT,"Headphones And Mobiles")

    def select_product(self,product_name):
        # Inputs from user

        # Collect list of all products names
        all_products_element = self.driver.find_elements(*self.all_products)
        print(len(all_products_element))

        # Find mobile_name in all values and click on it
        for curr_element in all_products_element:
            current_product = curr_element.find_element(*self.each_product).text
            print(current_product)
            if current_product in product_name:
                curr_element.click()
                break


    def add_product_to_cart(self,quantity):
        # Select two quantity of mobiles
        for i in range(0, quantity):
            print(i)
            self.driver.find_element(*self.increment_quantity).click()
        # Add to cart
        self.driver.find_element(*self.add_to_cart_button).click()

    def go_to_home(self):
        self.driver.find_element(*self.home_page_link).click()
