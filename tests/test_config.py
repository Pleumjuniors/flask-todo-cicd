from app.config import config

def test_testing_config():
    cfg = config['testing']
    assert cfg.SQLALCHEMY_DATABASE_URI == 'sqlite:///:memory:'
    assert cfg.TESTING is True

def test_development_config():
    cfg = config['development']
    assert 'postgresql://' in cfg.SQLALCHEMY_DATABASE_URI
    assert hasattr(cfg, 'init_app')
