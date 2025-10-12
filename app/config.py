class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/todo_dev'

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
