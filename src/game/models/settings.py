class Settings:
    def __init__(self, size: int=9, color_count: int=4,
                 max_time_to_rotate: int=100, time_decrease_step: int=5):
        self.size               : int = size
        self.color_count        : int = color_count
        self.max_time_to_rotate : int = max_time_to_rotate
        self.time_decrease_step : int = time_decrease_step
