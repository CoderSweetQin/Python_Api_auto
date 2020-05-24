# -*- coding: utf-8 -*-
import unittest
import time
import os.path
import sys
basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(basedir)
from lib import HTMLTestRunner3
from lib import send_email


"""unittest.defaultTestLoader(): defaultTestLoader()类，
通过该类下面的discover()方法可自动根据测试目录start_dir匹配查找测试用例文件（test*.py），
并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover"""
suite = unittest.defaultTestLoader.discover(basedir + '/test/testcase/', pattern='*.py')
filePath = basedir + "/report/testReport.html"
fp = open(filePath, 'wb')
"""生成报告的Title,描述"""
runner = HTMLTestRunner3.HTMLTestRunner(stream=fp, title='API自动化测试报告', description='API自动化测试报告')
runner.run(suite)
fp.close()
time.sleep(3)
send_email.send_mail_report("*****API自动化测试报告*****")


