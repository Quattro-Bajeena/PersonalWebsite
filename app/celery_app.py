import os
from dotenv import load_dotenv

from celery import Celery


load_dotenv('.env')
broker = os.environ.get('REDIS_URL') or os.environ.get('REDIS_URL_LOCAL')

celery_app = Celery( broker=broker, backend=broker)
celery_app.conf.imports = ['app.celery_tasks']