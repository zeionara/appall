from appall import AppallingLogger

logger = AppallingLogger(print)

logger.log("foo")
logger.log("qux")
logger.loop()

logger.log("bar")
logger.log("quux")

logger.log("baz")
logger.log("quuz")

logger.print(column_width = 10)
