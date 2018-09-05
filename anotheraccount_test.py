# -*- coding: utf-8 -*-
#coding=utf-8

from selenium import webdriver
import time
import pytest
import os
import re
import sys
import logging
import time
import pytest
from config import config
from public.base import *

# logger
logger = logging.getLogger()
logFormatter = logging.Formatter(
    '[%(asctime)-15s][%(filename)s][%(funcName)s#%(lineno)d] %(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(logFormatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)

class AnotherAccountTest(BaseTests):
    def test_login_twitter_account(self):
        try:
            for i in range(4):
                self.action.move_to_element_with_offset(self.driver.find_element_by_class_name('menu'),40,30).click()
                self.action.perform()

            time.sleep(1)

            self.driver.find_element_by_css_selector('.btn.btn-social.btn-twitter').click()

            user = config.TWITTER_ACCOUNT
            pwd = config.TWITTER_ACCOUNT_PWD

            time.sleep(2)
            self.driver.find_element_by_id('username_or_email').send_keys(user)
            time.sleep(1)
            self.driver.find_element_by_id('password').send_keys(pwd)
            time.sleep(1)
            self.driver.find_element_by_id('allow').click()

            time.sleep(2)

            try:
                self.driver.find_element_by_xpath('//form/label/div/input')
            except Exception as e:
                pass
            else:
                self.driver.find_element_by_xpath('//form/label/div/input').send_keys(pwd)
                time.sleep(1)
                self.driver.find_element_by_css_selector('.btn.btn-submit').click()

        except Exception as e:
            logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            raise