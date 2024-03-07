import logging
import logstash
import  sys

host = 'localhost'
port = 5000
test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler('host','port'))
test_logger.info('python-logstash: test logstash info message')