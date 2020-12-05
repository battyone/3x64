class Settings:
    def __init__(self, size: int=9, max_time_to_rotate: int=50, score_to_level: int=50):
        self.size               : int = size
        self.max_time_to_rotate : int = max_time_to_rotate
        self.score_to_level     : int = score_to_level
