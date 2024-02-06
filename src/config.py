#! python3
import os
class Config(object):
    SECRET_KEY = os.environ.get('JAPHOLIO_SECRET_KEY')
