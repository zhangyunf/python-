import logging
#创建一个logger
logger = logging.getLogger()
logger1 = logging.getLogger("mylogger")
logger1.setLevel(logging.INFO)

#创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
#再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

#定义handler的输出格式formatter
formatter = logging.Formatter("%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)
logger1.addHandler(fh)
logger1.addHandler(ch)

#记录日志
logger.debug("logger debug")
logger.error("logger error")

#重新制定日志记录
fh.s
logger1.debug("logger1 debug")
logger1.error("logger1 error")