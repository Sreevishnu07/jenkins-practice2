def count_errors(log_lines):
    error_count = 0

    for line in log_lines:
        if "ERROR" in line:
            error_count += 1

    return error_count


def error_rate(log_lines):
    total = len(log_lines)
    if total == 0:
        return 0

    errors = count_errors(log_lines)
    return errors / total


if __name__ == "__main__":
    logs = [
        "INFO Server started",
        "ERROR Database connection failed",
        "INFO Request received",
        "ERROR Timeout occurred"
    ]

    print("Total Errors:", count_errors(logs))
    print("Error Rate:", error_rate(logs))