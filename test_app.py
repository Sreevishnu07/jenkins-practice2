from app import count_errors, error_rate


def test_count_errors_basic():
    logs = [
        "INFO Start",
        "ERROR Something failed",
        "ERROR Another failure"
    ]
    assert count_errors(logs) == 2


def test_count_errors_no_errors():
    logs = [
        "INFO Start",
        "INFO Running"
    ]
    assert count_errors(logs) == 0


def test_error_rate():
    logs = [
        "INFO Start",
        "ERROR Fail",
        "INFO Continue",
        "ERROR Crash"
    ]
    assert error_rate(logs) == 0.5


def test_empty_logs():
    logs = []
    assert error_rate(logs) == 0