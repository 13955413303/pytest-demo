import random
import sys

import pytest

def start_class():
    print('this is class begin')

def end_class():
    print('this is class finish')

def start_func():
    print('this is function start ')


def end_func():
    print('this is function end ')

@pytest.fixture(scope='class',autouse=True)
def my_class_fixture():
    start_class()
    yield
    end_class()

class TestZyang():

    @pytest.fixture(scope='function', autouse=False, params=['aaa', 'bbb', 'ccc'])
    def my_function_fixture(self, request):
        start_func()
        yield request.param
        end_func()

    def test_001(self, my_function_fixture):
        try:
            assert random.randint(0, 1)
        except AssertionError:
            # print(sys._getframe().f_code.co_name)
            raise AssertionError

    def test_002(self):
        try:
            assert random.randint(0, 1)
        except AssertionError:
            print(sys._getframe().f_code.co_name)
            raise AssertionError

# class TestZyang:
#     def setup_class(self):
#         print('\nbegin--test', end='')
#
#     def setup(self):
#         print('\nstart_test_case ')
#
#     def test_001(self):
#         try:
#             assert random.randint(0, 1)
#         except AssertionError:
#             print(sys._getframe().f_code.co_name)
#             raise AssertionError
#
#     def test_002(self):
#         try:
#             assert random.randint(0, 1)
#         except AssertionError:
#             print(sys._getframe().f_code.co_name)
#             raise AssertionError
#
#     def teardown(self):
#         print('\nend_test_case')
#
#     def teardown_class(self):
#         print('finish--test')
