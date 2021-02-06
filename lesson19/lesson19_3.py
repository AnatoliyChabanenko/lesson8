import pytest


# @pytest.fixture()
def somsing_with_file(fail_name):
    with open(fail_name , 'w') as f:
        f.write('hello')


def test_my_test()