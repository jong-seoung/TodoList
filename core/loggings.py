import logging
from django.conf import settings

# 'db_logger' 로거 가져오기
db_logger = logging.getLogger('db_logger')

def log_db_url():
    db_url = settings.DATABASES['default'].get('HOST', 'localhost')
    db_name = settings.DATABASES['default'].get('NAME', 'unknown_db')
    db_user = settings.DATABASES['default'].get('USER', 'unknown_user')
    
    db_logger.info(f"Database URL: {db_url}")