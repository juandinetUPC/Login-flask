class Config:
    SECRET_KEY = 'JUANDINET!@#$%^&*()_+'

class DevelopmentConfig(Config):
    """
    Development configuration
    """
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flask_login'

    
config={
    'development': DevelopmentConfig
}