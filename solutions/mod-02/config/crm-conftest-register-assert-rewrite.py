# conftest.py configuration file
import pytest

# setup
def pytest_configure(config):
    # register the models module for assertion rewriting
    pytest.register_assert_rewrite("models")
    # pass

