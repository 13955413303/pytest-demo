import pytest


@pytest.fixture(scope='function')
def all_fixture():
    print('这是前置的方法')
    yield
    print('这是后置的方法')