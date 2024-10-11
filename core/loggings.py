import logging
from django.db import connections

logger = logging.getLogger('db_logger')

def log_db_url():
    for alias, connection in connections.databases.items():
        host = connection.get('HOST', 'localhost')
        logger.info(f"Using database alias: {alias} - Host: {host}")