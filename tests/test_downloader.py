from downloader import validate_date

def test_validate_date_valid():
    """Test that valid dates return True."""
    assert validate_date("2023-01-01", "2023-12-31") is True

def test_validate_date_invalid():
    """Test that invalid date formats return False."""
    assert validate_date("2023/01/01", "2023-12-31") is False

