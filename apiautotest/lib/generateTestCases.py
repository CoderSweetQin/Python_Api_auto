# coding=utf-8
import os
from lib import readexceldata
from config import config

# 类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称
def __generateTestCases(instanse, inerfaceName, tesDataName, sheetName):
    file = os.path.join(config.datapath, tesDataName)
    data_list = readexceldata.excel_to_list(file, sheetName)
    for i in range(len(data_list)):
        setattr(instanse, 'test_' + inerfaceName + '_%s' % (str(data_list[i]["tc_num"])),instanse.getTestFunc(data_list[i]))
