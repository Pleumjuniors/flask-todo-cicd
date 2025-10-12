from app import create_app

def test_app_creation():
    app = create_app('testing')
    assert app is not None
    assert app.name == 'app'

def test_app_config():
    app = create_app('testing')
    assert app.config['TESTING'] is True
