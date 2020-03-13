from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium
import os
import cv2
import numpy as np
import logging
import re
 
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")


from webdriver_manager.chrome import ChromeDriverManager



def get_screenshot(url):
    """
    :param url: Url to screen shot.
    :return: .png screen shot
    """
    # driver = webdriver.Chrome(executable_path = DRIVER_BIN)

    # driver = webdriver.Remote("lucid_allen:4444/wd/hub", DesiredCapabilities.CHROME)
    if not re.match(r"^https?", url):
        url = "http://" + url

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=os.path.join(os.path.dirname(__file__),'chromedriver_win.exe'))

    driver.set_page_load_timeout(10)
    driver.get(url)
    data = driver.get_screenshot_as_png()
    try:
        try:
            driver.get(url)
            data = driver.get_screenshot_as_png()
        except selenium.common.exceptions.UnexpectedAlertPresentException:
            webdriver.common.alert.Alert(driver).accept()
            logging.error("website had an alert! woo: "+url)
            data = driver.get_screenshot_as_png()
        except AttributeError:
            logging.error("I think this is because I clicked something, idk")
        except selenium.common.exceptions.TimeoutException:
            logging.error("Time out exception")
            #data = driver.get_screenshot_as_png()
            driver.quit()
            return
    except:
        print("fuck exception chaining")
        driver.quit()
        return

    driver.quit()
    return data

def string_to_image(binary_string):
    """
    Converts binary string to numpy array
    :param binary_string:
    :return:
    """
    # used https://stackoverflow.com/a/33522724
    if not binary_string: return None
    npimg = np.fromstring(binary_string, dtype=np.uint8)
    return cv2.imdecode(npimg, 1)