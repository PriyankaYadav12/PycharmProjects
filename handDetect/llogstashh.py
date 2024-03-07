import logging
import logstash
import random
test_logger = logging.getLogger('service_name')
test_logger.setLevel(logging.DEBUG)
test_logger.addHandler(logstash.TCPLogstashHandler('logstash-server-ip', 5959 , version=1))
extra = {
    'app_name':"service_name"
}
 #This code logs 10 times
test_logger.debug('There is some error in the request', extra=extra)
test_logger.info('INFO', extra=extra)
test_logger.warning('WARNING', extra=extra)
test_logger.critical('CRITICAL', extra=extra)
test_logger.error('ERROR', extra=extra)