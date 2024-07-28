import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'generator.settings')

# Create a Celery instance and set the broker and result backend.
app = Celery('generator')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')