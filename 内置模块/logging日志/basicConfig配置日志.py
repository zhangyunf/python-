import logging

logging.basicConfig(
    format='%(asctime)s %(lineno)d %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
logger.info("hello world")