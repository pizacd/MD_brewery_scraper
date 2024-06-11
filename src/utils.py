# utils.py
# [TODO] incorporate logging into functions
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from abc import ABC, abstractmethod
from typing import Dict


def setup_driver(set_options = False):
    if set_options == True:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    return driver

class Authenticator(ABC):
    @abstractmethod
    def needs_authentication():
        pass

    @abstractmethod
    def is_authenticated() -> bool:
        pass
class XpathAuthenticator(Authenticator):
    def __init__(self, attribute_dict: Dict):
        self.attribute_dict = attribute_dict
        self.authenticated = False

    def authenticate_age(self, driver: webdriver.chrome.webdriver.WebDriver):
        assert len(self.attribute_dict.items())==1
        scraping_path = list(self.attribute_dict.values())[0]
        try:
            button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, scraping_path))
            )
            return button.click()
        except ValueError:
            pass
 
class ClassNameAuthenticator(Authenticator):
    def __init__(self, attribute_dict):
        self.attribute_dict = attribute_dict
        self.authenticated = False


    def authenticate_age(self, driver: webdriver.chrome.webdriver.WebDriver):
        assert len(self.attribute_dict.items())==1
        scraping_path = list(self.attribute_dict.values())[0]
        try:
            button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, scraping_path))
            )
            return button.click()
        except ValueError:
            pass

class NameAuthenticator(Authenticator):
    def __init__(self,attribute_dict):
        self.attribute_dict = attribute_dict
        self.authenticated = False

    def authenticate_age(self, driver: webdriver.chrome.webdriver.WebDriver):
        assert len(self.attribute_dict.items())==1
        scraping_path = list(self.attribute_dict.values())[0]
        try:
            button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, scraping_path))
            )
            return button.click()
        except ValueError:
            pass

# def authenticate_age(driver: webdriver.chrome.webdriver.WebDriver,
#                      attribute_dict: dict):
#     assert len(attribute_dict.items())==1
#     scraping_method = list(attribute_dict.keys())[0]
#     scraping_path = list(attribute_dict.values())[0]
#     if scraping_method.lower() == "class_name":
#         try:
#             button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CLASS_NAME, scraping_path))
#             )
#             return button.click()
#         except ValueError:
#             pass
#     elif scraping_method.lower() == "xpath":
#         try:
#             button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, scraping_path))
#             )
#             return button.click()
#         except ValueError:
#             pass
#     elif scraping_method.lower() =="name":
#         try:
#             button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.NAME, scraping_path))
#             )
#             return button.click()
#         except ValueError:
#             pass

def extract_text(driver: webdriver.chrome.webdriver.WebDriver,
                attribute_dict: dict) ->list:
    """returns the text of a webpage using the argument scraping_method for
    path scraping_path"""
    assert len(attribute_dict.items())==1
    scraping_method = list(attribute_dict.keys())[0]
    scraping_path = list(attribute_dict.values())[0]
    if scraping_method.lower() == 'class_name':
        try:
            elements = WebDriverWait(driver,
                                     10).until(
                                         EC.presence_of_all_elements_located(
                                             (
                                                 By.CLASS_NAME,
                                                 scraping_path
                                                 )
                                              )
        )
            text = [ele.text for ele in elements]
            return text
        except ValueError:
            pass
    if scraping_method.lower() == 'name':
        try:
            elements = WebDriverWait(driver,
                                     10).until(
                                         EC.presence_of_all_elements_located(
                                             (
                                                 By.NAME,
                                                 scraping_path
                                                 )
                                              )
        )
            text = [ele.text for ele in elements]
            return text
        except ValueError:
            pass
    elif scraping_method.lower() == "xpath":
        try:
            elements = WebDriverWait(driver,
                                     10).until(
                                         EC.presence_of_all_elements_located(
                                             (
                                                 By.XPATH,
                                                 scraping_path
                                                 )
                                              )
        )
            text = [ele.text for ele in elements]
            return text
        except ValueError:
            pass
    # else:
    #     raise ValueError("Invalid method. Use 'xpath' or 'tag_name'.")
    
    # [col.text for col in driver.find_elements(By.CLASS_NAME,'item-abv')]
    # pass
################# CHATGPT Recommended functions #################

# def click_button(driver, by, identifier):
#     try:
#         button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((by, identifier))
#         )
#         button.click()
#     except Exception as e:
#         logging.error(f"Error clicking button: {e}")
#         raise
# def wait_for_element(driver, by, identifier):
#     try:
#         element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((by, identifier))
#         )
#         return element
#     except Exception as e:
#         logging.error(f"Error waiting for element: {e}")
#         raise
