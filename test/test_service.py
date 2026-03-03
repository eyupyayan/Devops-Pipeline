from app.service import make_greeting

def test_make_greeting():
    result = make_greeting("Batman")
    assert "message" in result
    assert result["message"] == "Hello, Batman!"
    assert "time_utc" in result