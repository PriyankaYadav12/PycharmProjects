import logging
from logstash_async.handler import AsynchronousLogstashHandler

host = 'localhost'
port = 5000
# Create the logger and set it's logging level
logger = logging.getLogger("invoke_python")
logger.setLevel(logging.ERROR)

# Create the handler
async_handler = AsynchronousLogstashHandler(
    host='logstash',
    port=5000,
    ssl_enable=True,
    ssl_verify=False,
    database_path='')
logger.addHandler(async_handler)
import time
while True:
    logger.info("this is an info message at %s", time.time())
    time.sleep(0.5)




# Send log records to Logstash
#logger.error('python-logstash-async: test error message.')
#logger.info('python-logstash-async: test info message.')
#logger.warning('python-logstash-async: test warning message.')
#logger.debug('python-logstash-async: test debug message.')