#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
import os
import time

# 相对路径的父路径就是项目根目录
base_path = os.path.dirname(os.path.abspath('.'))


class Logger(object):
    def __init__(self, logger):
        '''''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 项目根目录下/Logs 保存日志
        self.log_path = base_path +'/test_reports/' + rq

        # 判断路径是否存在
        isExists = os.path.exists(self.log_path)

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(self.log_path)

        log_name = self.log_path + '/log.txt'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

    def report_path(self):
        return self.log_path