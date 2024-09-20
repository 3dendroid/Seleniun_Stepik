import pytest


@pytest.fixture()
def set_up():
    print(' Log in the system')
    yield
    print(' Log out the system')


@pytest.fixture(scope="module")
def module():
    print('Start test 1')
    yield
    print('End test 1')


# @pytest.fixture(scope="function")
# def function():
#     print('Start test 1')
#     yield
#     print('End test 1')
