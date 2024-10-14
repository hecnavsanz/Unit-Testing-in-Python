# conftest.py configuration file:
# - contain directory-specific hook implementations
# - test running activities will invoke all hooks defined in conftest.py files.
import pytest


# setup initial configuration (category: initialization hook)
def pytest_configure(config):
    # register the models module for assertion rewriting
    pytest.register_assert_rewrite("models")
