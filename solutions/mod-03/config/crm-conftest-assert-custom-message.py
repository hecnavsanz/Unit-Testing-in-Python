# conftest.py configuration file
from models.customer import Customer


# custom assertion message when comparing Customer instances
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Customer) and isinstance(right, Customer) and op == "==":
        return [
            "Comparing Customer instances:",
            "   vals: {} != {}".format(str(left), str(right)),
        ]
