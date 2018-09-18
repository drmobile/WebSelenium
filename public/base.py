#coding=utf-8

import sys
import logging
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# logger
logger = logging.getLogger()
logFormatter = logging.Formatter(
    '[%(asctime)-15s][%(filename)s][%(funcName)s#%(lineno)d] %(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(logFormatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)


class BaseTests(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        options = webdriver.ChromeOptions()
        # default window size
        options.add_argument('--window-size=1280x800')
        # default browser lang
        options.add_argument('--lang=zh-TW')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--user-agent="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"')
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)

        self.driver.get("https://www-staging.soocii.me")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'menu')))
        
        self.action = webdriver.ActionChains(self.driver)
        
    def tearDown(self):
        self.driver.save_screenshot('{}.png'.format(__name__))
        self.driver.close()
        self.driver.quit()
