import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    LANGUAGES = {'en' : 'English', 'pl' : 'Poland'}
    DEBUG = True