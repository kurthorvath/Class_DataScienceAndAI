from app.hello import hello


def test_hello():
    assert hello("Azure") == "Hello, Azure!"


def test_default_hello():
    assert hello() == "Hello, World!"
