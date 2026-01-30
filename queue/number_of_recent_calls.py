from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.recent = deque()
        

    def ping(self, t):
        self.recent.append(t)
        while self.recent[0] < t - 3000: #find the oldest ping
            self.recent.popleft()
        return len(self.recent)
