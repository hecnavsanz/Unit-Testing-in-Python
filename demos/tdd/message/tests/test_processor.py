from modules.processor import reverse, toUpper


def test_reverse_1():
    r = reverse("Unit Testing")
    assert r == "gnitseT tinU"


def test_reverse_2():
    r = reverse("Functional Testing")
    assert r == "gnitseT lanoitcnuF"


def test_toUpper():
    u = toUpper("Unit Testing")
    assert u == "UNIT TESTING"
    u = toUpper("Functional Testing")
    assert u == "FUNCTIONAL TESTING"
