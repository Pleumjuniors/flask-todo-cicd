from app import create_app

def test_app_config():
    app = create_app('testing')
    assert app.config['TESTING'] is True
