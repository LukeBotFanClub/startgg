import startgg


def test_client():
    # Still need to decide whether to test against the actual startgg API
    # Or whether I can test using mocks instead to avoid dependence on an external service
    startgg.StartGGClient()
