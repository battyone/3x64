from random import randint
from .settings import Settings
from .stats import Stats

class State:
    def __init__(self, settings: Settings, stats: Stats):
        self.__settings : Settings   = settings
        self.__stats    : Stats      = stats
        self.board      : [[chr]]    = self.get_default_board()
        self.cur_blocks : [chr, chr] = [self.get_random_block() for _ in range(2)]
        self.cur_pos    : (int, int) = self.get_default_pos()
        self.paused     : bool       = True

    def get_default_board(self) -> [[chr]]:
        size = self.__settings.size
        return [
            [' ' for x in range(size)]
                 for y in range(size)
        ]

    def get_default_pos(self) -> (int, int):
        return (self.__settings.size // 2, 0)

    def get_random_block(self) -> chr:
        return str(randint(0, self.__settings.color_count))

    def is_avaliable(self, x: int, y: int) -> bool:
        size = self.__settings.size
        return 0 <= x < size and \
               0 <= y < size and \
               self.board[y][x] is ' '

    def move_left(self):
        x, y = self.cur_pos
        if self.is_avaliable(x-1, y):
            self.cur_pos = (x-1, y)

    def move_right(self):
        x, y = self.cur_pos
        if self.is_avaliable(x+1, y):
            self.cur_pos = (x+1, y)

    def move_down(self):
        x, y = self.cur_pos
        if self.is_avaliable(x, y+1):
            self.cur_pos = (x, y+1)
        else:
            self.__place_block()

    def __place_block(self):
        x, y = self.cur_pos
        self.board[y][x] = self.cur_blocks.pop(0)
        self.__start_new_block()
        self.__check_lines()

    def __start_new_block(self):
        self.cur_blocks.append(self.get_random_block())
        self.cur_pos = self.get_default_pos()

    def __check_lines(self):
        to_delete = list(self.__check_rows()) + \
                    list(self.__check_cols())
        self.__stats.score += len(to_delete)
        for x, y in to_delete:
            self.board[y][x] = ' '

    def __check_rows(self) -> [(int, int)]:
        for y in range(len(self.board)):
            row = self.board[y]
            for x in State.__get_blocks_to_delete(row):
                yield (x, y)

    def __check_cols(self) -> [(int, int)]:
        for x in range(len(self.board)):
            col = [self.board[y][x] for y in range(len(self.board))]
            for y in State.__get_blocks_to_delete(col):
                yield (x, y)

    @staticmethod
    def __get_blocks_to_delete(array) -> [(int, int)]:
        to_delete = []
        start, block, count = 0, array[0], 0

        for i, cur_block in enumerate(array):
            if cur_block == block:
                count += 1
            else:
                if State.__is_good_chain(block, count):
                    to_delete += list(range(start, start+count))
                start, block, count = i, cur_block, 1

        if State.__is_good_chain(block, count):
            to_delete += list(range(start, start+count))

        return to_delete

    @staticmethod
    def __is_good_chain(block:chr, count:int) -> bool:
        return count > 2 and block != ' ' and block != '0'
