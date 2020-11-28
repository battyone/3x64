class Stats:
    def __init__(self):
        self.start_time : int = None
        self.play_time  : int = 0
        self.score      : int = 0
        self.get_level  : int = lambda: 1 + self.score // 100
