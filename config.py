import os 

class config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "Secret string"