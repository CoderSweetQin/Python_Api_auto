#coding=utf-8
import unittest
import requests
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from config import base_url
import base64


##用户登录接口示例
class Login(unittest.TestCase):
    """用户登录接口--tester"""
    def setUp(self):
        logger.info("*" * 80)

    def getTest(self,data):
        logger.info("***************用户登录接口开始****************")
        num=data['tc_num']
        name=data['tc_name']
        case = data['case']
        user=data['phone']+":"+data['password']
        code=int(data['code'])
        params = "deviceType=WINDOWS&deviceId=861735031960296&deviceName=MAC&code=0000"
        authorization=str(base64.b64encode(user.encode(encoding="utf-8")), 'utf-8')
        headers={}
        headers["X-Forwarded-For"]="127.0.0.1"
        headers["Authorization"]="Basic "+authorization
        logger.info(num+"_"+name+"_"+case)
        requests.packages.urllib3.disable_warnings()
        res = requests.get(url=base_url.get_base_url(case) + base_url.login_url, params=params, headers=headers, verify=False)
        logger.info(res.text)
        result = res.json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'],code)
        logger.info("****************用户登录接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)

# 调用这个方法__generateTestCases的参数说明：类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称
__generateTestCases(Login, "login",  "login_api_data.xlsx", "用户登录")
