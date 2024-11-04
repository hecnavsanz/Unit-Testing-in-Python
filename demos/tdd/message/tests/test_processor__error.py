from modules.processor__error import reverse


def test_reverse():
    r = reverse("Unit Testing")
    assert r == "gnitseT tinU"
