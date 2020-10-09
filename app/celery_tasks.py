from .celery_app import celery_app


from .scheduler import update_all
from . import app


@celery_app.task(name="Update Activities Async", bind=True)
def update_activities_async(self):
    print("Celery Task Update ACtivities Start")
    for status in update_all():
        if status['progress'] == True:
            self.update_state(state='PROGRESS', meta={'current' : status['current'], 'total' : status['total'], 'status' : status['status']})
        else:
            return status

    