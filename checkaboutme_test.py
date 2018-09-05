# -*- coding: utf-8 -*-
#coding=utf-8

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

class CheckAboutmeTest(BaseTests):
    def test_check_aboutme(self):
        try:
            for i in range(4):
                self.action.move_to_element_with_offset(self.driver.find_element_by_class_name('menu'),40,30).click()
                self.action.perform()
                time.sleep(0.5)

            time.sleep(1)

            self.driver.find_element_by_css_selector('.btn.btn-email').click()

            user = config.EMAIL_ACCOUNT
            pwd = config.EMAIL_PWD

            time.sleep(1)
            self.driver.find_element_by_xpath('//form/section/label[1]/input').send_keys(user)
            time.sleep(1)
            self.driver.find_element_by_xpath('//form/section/label[2]/input').send_keys(pwd)
            time.sleep(1)
            self.driver.find_element_by_css_selector('.btn.btn-submit').click()

            self.driver.get('https://www-staging.soocii.me/user/s.carolineccc')

            time.sleep(1)

            self.driver.find_element_by_css_selector('.cover-photo')

            self.driver.find_element_by_class_name('avatar-large')
            
            self.driver.find_element_by_class_name('show-list')

            self.driver.find_element_by_css_selector('.btn-follow').click()

            self.driver.find_element_by_css_selector('.dialog-body.message-body')

            self.driver.find_element_by_css_selector('.btn.btn-primary').click()

        except Exception as e:
            logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            raise


# - 登入後，開啟該網址
# - 確認是否有有區塊「封面照」、「大頭照」、「最常玩的遊戲」以及「我的貼文」區域
# - 點追蹤按鈕，是否有變成「追蹤中」(或是點「追蹤中」按鈕，是否有變回「追蹤」)