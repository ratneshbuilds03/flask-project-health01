import pytest
from app import create_app ,db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING']=True
    app.config['SQLALCHEMY_DATABASE_URL']='sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        
def test_health_check(client):
    response = client.get('/health')
    assert response.status_code ==200
    assert response.get_json()=={"status":"ok"}
    
def test_signup(client):
    response =client.post('/signup', json={
        "name": "Test User",
        "email": "test@example.com",
        "password": "test123"
    })
    assert response.status_code==201
    assert response.get_json()["email"]=="test@example.com"
def test_singup_missing_fields(client):
    response =client.post('/signup', json={"email": "test@example.com"})
    assert response.status_code==400
def test_login_wrong_password(client):
    client.post('/signup', json={
        "name": "Test User",
        "email": "test2@example.com",
        "password": "correctpass"
    })
    response = client.post('/login', json={
        "email": "test2@example.com",
        "password": "wrongpass"
    })
    assert response.status_code == 401