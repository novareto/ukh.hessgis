import logging
logger = logging.getLogger('uvcsite.ukh.hessgis')

def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)
