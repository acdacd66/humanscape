from django.apps import AppConfig


# class ClinicalinformationConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'clinicalInformation'



class BatchConfig(AppConfig):
    name = 'clinicalInformation'

    def ready(self):
        print("Starting Scheduler ...")
        from .batch_scheduler import batchUpdater
        batchUpdater.start()
