import pytest


@pytest.fixture(scope='function')
def user_fixture():
    print('这是用户管理前置的方法')
    yield
    print('这是用户管理后置的方法')