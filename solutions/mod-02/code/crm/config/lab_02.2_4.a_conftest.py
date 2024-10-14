# conftest.py configuration file:
# - contain directory-specific hook implementations.
# - test running activities will invoke all hooks defined in conftest.py files.
from models.customer import Customer


# custom assertion message when comparing Customer instances in failing assert expressions
# (category: reporting hook)
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Customer) and isinstance(right, Customer) and op == "==":
        return [
            "Comparing Customer instances:",
            "   vals: {} != {}".format(str(left), str(right)),
        ]
