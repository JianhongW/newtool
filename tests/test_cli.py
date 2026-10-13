from newtool.cli import health


def test_health_returns_ok():
    result = health()

    assert result["status"] == "ok"
    assert result["python_package"] == "newtool"
