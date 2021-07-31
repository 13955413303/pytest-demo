import pytest


@pytest.fixture(scope='function')
def product_fixture():
    print('这是商品管理前置的方法')
    yield
    print('这是商品管理后置的方法')