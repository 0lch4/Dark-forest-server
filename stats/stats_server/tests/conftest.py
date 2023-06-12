import pytest
from django.conf import settings


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db) -> None:  # noqa: ARG001, ANN001
    pass


def pytest_configure() -> None:
    settings.DEBUG = False
