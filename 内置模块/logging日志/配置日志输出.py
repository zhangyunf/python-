import logging

logging.basicConfig(
    level=logging.NOTSET,  #通过具体的参数来更改logging模块默认行为
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def log(message):
    logging.info(message)