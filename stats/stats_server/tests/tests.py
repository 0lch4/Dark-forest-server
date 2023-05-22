import pytest
from django.test import RequestFactory
from django.contrib.auth.models import User

#my tests
@pytest.mark.django_db
def test_create_user_view():
    from stats_server.views import create_user
    
    factory = RequestFactory()
    request = factory.post('create_user', {'username': 'test', 'password': 'pass'})
    response = create_user(request)
    assert response.status_code == 302
    assert User.objects.filter(username='test').exists()
    assert response.url == '/stats/register_success'
    
@pytest.mark.django_db
def test_login_view():
    from stats_server.views import login_view
    
    factory = RequestFactory()
    request = factory.post('login_view', {'username': 'test', 'password': 'pass'})
    response = login_view(request)
    assert response.status_code == 302
    assert response.url == '/stats/login'
    