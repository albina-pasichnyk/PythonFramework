from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME = 1
SAFARI = 2
FIREFOX = 3

options = Options()
options.headless = True
options.add_argument('--no-sandbox')


def create_driver_factory(driver_id):
    if int(driver_id) == CHROME:
        driver = webdriver.Chrome(options=options)
        return driver
    elif int(driver_id) == SAFARI:
        driver = webdriver.Safari()
        return driver
    elif int(driver_id) == FIREFOX:
        driver = webdriver.Firefox()
        return driver
    else:
        driver = webdriver.Chrome()
        return driver
