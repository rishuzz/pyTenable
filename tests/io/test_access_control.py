import pytest
from requests import Response


@pytest.mark.vcr()
def test_details(api):
    data = api.v3.access_control.details('7c54920a-3b28-412e-a5e3-638694187722')
    assert data['permission_uuid'] == '7c54920a-3b28-412e-a5e3-638694187722'


def test_get_user_permission():
    assert False


def test_get_user_group_permission():
    assert False


def test_get_current_user_permission():
    assert False


def test_delete():
    assert False


def test_create():
    assert False


def test_update():
    assert False
