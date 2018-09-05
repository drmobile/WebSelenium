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

class FacebookAccountTest(BaseTests):
    def test_login_facebook_account(self):
        try:
            for i in range(4):
                self.action.move_to_element_with_offset(self.driver.find_element_by_class_name('menu'),40,30).click()
                self.action.perform()

            time.sleep(2)

            self.driver.find_element_by_css_selector('.btn.btn-social.btn-facebook').click()

            user = config.FACEBOOK_ACCOUNT1
            pwd = config.FACEBOOK_ACCOUNT1_PWD
            uid = config.FACEBOOK_ACCOUNT1_SOOCIIID

            time.sleep(2)
            self.driver.find_element_by_id('email').send_keys(user)
            time.sleep(1)
            self.driver.find_element_by_id('pass').send_keys(pwd)
            time.sleep(1)
            self.driver.find_element_by_id('loginbutton').click()

            time.sleep(3)

            try:
                self.driver.find_element_by_xpath('//form/label/div/input')
            except Exception as e:
                pass
            else:
                self.driver.find_element_by_xpath('//form/label/div/input').send_keys(uid)
                time.sleep(1)
                self.driver.find_element_by_css_selector('.btn.btn-submit').click()

        except Exception as e:
            logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            raise