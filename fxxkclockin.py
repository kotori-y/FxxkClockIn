# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:21:24 2020

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
@Blog: https://blog.iamkotori.com

♥I love Princess Zelda forever♥
"""


import datetime
import os
import csv
from selenium import webdriver
from lxml import etree
import numpy
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


desired_capabilities = DesiredCapabilities.EDGE  # 修改页面加载策略
desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出


class AutoClockIn(object):
    
    def __init__(self, uname, pwd, driverpath='msedgedriver.exe'):
        """
        """
        self.uname = uname
        self.pwd = pwd
        self.driver = webdriver.Edge(executable_path = driverpath)
    
    def logIn(self):
        self.driver.get("http://ca.its.csu.edu.cn/home/login/215")
        loginButtonxpath = '//*[@id="login-btn"]'
        userNamexpath = '//*[@class="login_table_text1_input"][@id="userName"]'
        passWordxpath = '//*[@class="login_table_text1_input"][@id="passWord"]'
        
        self._wait(loginButtonxpath)
        time.sleep(1)
        self._send_keys(userNamexpath, self.uname)
        self._send_keys(passWordxpath, self.pwd)
        self._click(loginButtonxpath)
        
    def clockIn(self):
        self._wait('//*[@class="banners"]')
        self.driver.get('https://wxxy.csu.edu.cn/ncov/wap/default/index')
        self.getLocation()
        time.sleep(1)
        self._click('//*[@class="wapcf-btn-qx"]')
        
    
    def getLocation(self):
        self._wait('//*[@name="area"]')
        self._click('//*[@name="area"]')
    
    
    def _send_keys(self, xpath, keys):
        self.driver.find_element_by_xpath(xpath).clear(
                )
        self.driver.find_element_by_xpath(xpath).send_keys(keys
                                    )
    def _click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click(
                )
    
    def _wait(self, xpath):
        Wait(self.driver, 40).until(EC.presence_of_element_located(
                (By.XPATH,xpath)
                )
        )
    
    def _getTime(self):
        """
        get local time

        Returns
        -------
        nowTime : str
            Time in formate of HH:MM

        """
        nowTime = time.strftime('%H:%M', 
                                time.localtime(
                                    time.time(
                                        )
                                    )
                                )
        return nowTime
    
    
    
if '__main__' == __name__:
    clockin = AutoClockIn('', '')
    clockin.logIn()
    clockin.clockIn()
    
    
    
    
    