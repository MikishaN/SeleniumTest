from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3

    @staticmethod
    def create_driver(driver_id, is_headless=True):
        if DriverFactory.CHROME == driver_id:
            chrome_options = Options()
            if is_headless:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")    
            chrome_options.add_argument("--disable-gpu") 
            # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())

        return driver
