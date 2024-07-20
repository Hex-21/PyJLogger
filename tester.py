import PyJLogger
logger = PyJLogger.get_logger("test_logger_name", 3)


def testfunc():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warn("This is a warning message")
    logger.exception("This is an exception message")
    logger.error("This is an error message")
    logger.crit("This is a critical message")


if __name__ == "__main__":
    testfunc()
