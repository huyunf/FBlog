import os

basdir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY  = os.envrion.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX  = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <yfhu.dev@hotmail.com>'
    FLASKY_ADMIN = os.envrion.get('FLASKY_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass
