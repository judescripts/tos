# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a ..env file to set
environment variables.
"""
import pickle

#from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
#from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SECRET_KEY = env.str("SECRET_KEY")
SEND_FILE_MAX_AGE_DEFAULT = env.int("SEND_FILE_MAX_AGE_DEFAULT")
BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS", default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SCHEDULER_JOBSTORES = {
#    'default': SQLAlchemyJobStore(url=env.str("DATABASE_URL"), pickle_protocol=pickle.DEFAULT_PROTOCOL)
#}
#SCHEDULER_EXECUTORS = {
#    'default': ThreadPoolExecutor(20),
#    'processpool': ProcessPoolExecutor(5)
#}
#SCHEDULER_JOB_DEFAULTS = {
#    'coalesce': True,
#    'max_instances': 100,
#    'misfire_grace_time': 60
#}
#SCHEDULER_API_ENABLED = True
