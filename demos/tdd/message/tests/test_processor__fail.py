from modules.processor__fail import reverse


def test_reverse():
    r = reverse("Unit Testing")
    assert r == "gnitseT tinU"
