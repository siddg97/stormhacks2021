from time import sleep
from celery import Celery

celery = Celery(__name__, autofinalize=False)


@celery.task(bind=True)
def add(self, x, y):
    print("sleeping...")
    sleep(5)
    print("woke up")
    print(f"Sum is: {x+y}")