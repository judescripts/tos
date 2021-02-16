"""

"""
#import atexit
#import pickle
#from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
#from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
#from apscheduler.schedulers.background import BackgroundScheduler
#from environs import Env
#from pytz import utc
#
#env = Env()
#env.read_env()
#jobstores = {
#    'default': SQLAlchemyJobStore(url=env.str("DATABASE_URL"), pickle_protocol=pickle.DEFAULT_PROTOCOL)
#}
#executors = {
#    'default': ThreadPoolExecutor(20),
#    'processpool': ProcessPoolExecutor(5)
#}
#job_defaults = {
#    'coalesce': False,
#    'max_instances': 3
#}
#scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
#atexit.register(lambda: scheduler.shutdown(wait=False))
