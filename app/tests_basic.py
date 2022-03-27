import pytest

from model import User


@pytest.fixture
def user():
    return User('Aaron')


# A pretty redundant test meant to make sure that we're up and running
def test_constructor():
    u = User('Aaron')
    assert isinstance(u, User)


def test_add_activity(user):
    '''
    Testing the functionality of add_activity. Can multiple activities
    be added? Do we always initialize with an empty container?
    Is activity_name limited to the list of pre-defined activities?
    '''
    assert len(user.activities) == 0
    user.add_activity('foo')
    assert len(user.activities) > 0
    user.add_activity('bar')
    assert len(user.activities) == 2
