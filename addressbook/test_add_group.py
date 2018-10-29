import pytest
import time
from application import Application
from group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


'''
def test_login(app):
    app.open_home_page()
    app.login()
    time.sleep(5)
    app.logout()
'''


def test_add_group(app):
    app.open_home_page()
    app.login()
    app.create_group(Group('2', '22', '222'))
    app.return_to_groups()

