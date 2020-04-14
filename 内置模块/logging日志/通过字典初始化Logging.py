#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import logging.config
import logging

standard_format = '%(asctime)s %(threadName)s %(lineno)s %(message)s'
simplie_format = '%(levelname)s %(message)s'

LOGGING_DIC = {
    # 版本号
    'version': 1,
    # 是否使用此处定义的处理器
    'disable_existing_loggers': False,
    # 定义日志格式
    'formatters': {
        "standard": {
            "format": standard_format,
        },
        "simple": {
            "format": simplie_format
        }
    },
    # 定义过滤器
    'filters': {},
    # 定义处理器
    'handlers': {
        'handler_fileHandler': {
            'filename': 'test.log',
            'class': "logging.FileHandler",
            'formatter': 'simple',
        },
        'handler_consoleHandler': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    # 定义logger
    'loggers': {
        'root': {
            'handlers': ['handler_consoleHandler', 'handler_fileHandler'],
            'level': 'INFO'
        },
        "simple": {
            'handlers': ['handler_consoleHandler'],
            'level': 'DEBUG'
        }
    }
}
logging.config.dictConfig(LOGGING_DIC)
logger = logging.getLogger('simple')
logger.info('hello world')




    


