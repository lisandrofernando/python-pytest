
from pytest import fixture

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@fixture(scope='class')
def setup(request):
        driver = webdriver.Chrome()
        browser_name = request.config.getoption("browser_name")
        if browser_name == "Chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_name == "firefox":
            print("firefox")
        elif browser_name == "MicrosoftEdge":
            print("Edge")
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()

# To invoke the browser in the terminal dynamically use: py.test --browser_name chrome or firefox..
    