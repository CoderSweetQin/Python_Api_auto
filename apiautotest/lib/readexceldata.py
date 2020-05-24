# -*- coding: utf-8 -*-
import xlrd
'''
读取excel文件,将excle文件里面对应的sheet of addbook数据转换为python 列表对象，其中列表中每一个元素为一个字典
'''
def excel_to_list(file, tag):
    """将excel表中数据转换成python对象"""
    data_list = []
    """打开excel文件"""
    book = xlrd.open_workbook(file)
    """选择读取sheet工作表"""
    tag = book.sheet_by_name(tag)
    """获取行数"""
    row_num = tag.nrows
    header = tag.row_values(0)
    for i in range(1, row_num):
        """读取行"""
        row_data = tag.row_values(i)
        """读取行中的每一列的值"""
        d = dict(zip(header, row_data))
        data_list.append(d)
    return data_list

"""获取测试数据,判断传入的test_name 是否存在，存在则返回一个列表中对应的字典数据"""
def get_test_data(test_name, test_list):
    for test_dict in test_list:
        if test_name == test_dict['test_name']:
            return test_dict
