# -*- coding: utf-8 -*-

import time
import pytest
import os
import re
import sys
import logging

from config import config
from selenium import webdriver
from public.base import *
from selenium.webdriver.support import expected_conditions as EC

# logger
logger = logging.getLogger()
logFormatter = logging.Formatter(
    '[%(asctime)-15s][%(filename)s][%(funcName)s#%(lineno)d] %(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(logFormatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)

class EmailAccountTest(BaseTests):
    def test_emailaccount(self):
        try:
            for i in range(4):
                self.action.move_to_element_with_offset(self.driver.find_element_by_class_name('menu'),40,30).click()
                self.action.perform()

            time.sleep(1)

            self.driver.find_element_by_css_selector('.btn.btn-email').click()

            user = config.EMAIL_ACCOUNT
            pwd = config.EMAIL_PWD

            time.sleep(2)
            self.driver.find_element_by_xpath('//form/section/label[1]/input').send_keys(user)
            time.sleep(1)
            self.driver.find_element_by_xpath('//form/section/label[2]/input').send_keys(pwd)
            time.sleep(1)
            self.driver.find_element_by_css_selector('.btn.btn-submit').click()

        except Exception as e:
            logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            raise