import pytest


@pytest.fixture ()  # file conftest.py (7.13)
def set_up():
    print ('\nSTART TEST')  # print when running
    yield
    print ('\nFINISH TEST')  # print when finished


@pytest.fixture (scope='module')  # scope='module' (7.14)
def set_group():
    print ('\nENTER SYSTEM')  # print when running
    yield
    print ('\nEXIT SYSTEM')  # print when finished
