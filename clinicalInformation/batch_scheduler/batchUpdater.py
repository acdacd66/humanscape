from apscheduler.schedulers.background import BackgroundScheduler
from clinicalInformation.views import BatchDataView
def start():
  scheduler = BackgroundScheduler()
  batch = BatchDataView()
  scheduler.add_job(batch.post, "interval", minutes=60,id="batch_001",replace_existing=True)
  scheduler.start()

