import logging
logging.basicConfig(filename = "test.log", level = logging.DEBUG)

#需要指定，不然无法输出
logging.exception("11111111")