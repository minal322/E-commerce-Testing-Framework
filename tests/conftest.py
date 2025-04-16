import pytest
from selenium import webdriver

driver = None
#### Registering command line options (Mandatory)
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome" , help= "Browser Selection"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser") # --browser
    if browser_name == "chrome" or browser_name == "Chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge" or browser_name == "Edge":
        driver = webdriver.Edge()
    elif browser_name == "firefox" or browser_name == "Firefox":
        driver = webdriver.Firefox()
    driver.get("https://e-commerce-updated-0993-311gkb9ju-minal322s-projects.vercel.app/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
