import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    # Signup mutates module-level state, so restore it after every test.
    snapshot = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(snapshot)
