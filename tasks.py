from celery import Celery
from celery.schedules import crontab

from webapp import create_app
from wear_lines import read_and_save_in_base

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def read_and_save_in_db():
    with flask_app.app_context():
       read_and_save_in_base()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), read_and_save_in_db.s())
