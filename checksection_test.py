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

class CheckSectionTest(BaseTests):
    def test_sectioncheck(self):
        try:
            self.driver.find_element_by_class_name('video-wrapper')

            self.driver.find_element_by_class_name('video-list')

            self.driver.find_element_by_class_name('hot-section')

            flag = 0
            for item in self.driver.find_elements_by_class_name('section-caption'):
                if((item.text).encode('utf-8') == '全新聞(中文)'):
                    flag +1
                    
            if(flag == 0):
                self.assertFalse

            self.driver.find_element_by_class_name('footer')

        except Exception as e:
            logger.info('caught exception: {}'.format(sys.exc_info()[0]))
            raise