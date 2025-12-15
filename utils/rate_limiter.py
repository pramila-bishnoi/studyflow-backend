import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests=20, window_seconds=60):
        self.max_requests = max_requests
        self.window = window_seconds
        self.requests = defaultdict(list)

    def is_allowed(self, user):
        now = time.time()
        self.requests[user] = [
            t for t in self.requests[user] if now - t < self.window
        ]

        if len(self.requests[user]) >= self.max_requests:
            return False

        self.requests[user].append(now)
        return True
