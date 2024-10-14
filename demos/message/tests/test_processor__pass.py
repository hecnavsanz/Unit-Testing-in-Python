from modules.processor__pass import reverse


def test_reverse():
    r = reverse("Unit Testing")
    assert r == "gnitseT tinU"
