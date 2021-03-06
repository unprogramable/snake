import numpy as np
import cv2

class Board(object):
    """window or page or board game"""

    def __init__(self, size=[(0, 0), (60, 80)], title='Simple Snake', bg=0, fg=1):
        # board size
        self.size = size
        # board title
        self.title = title
        # background color
        self.bg = bg
        # forground color
        self.fg = fg
        # - create board array(numpy zeros) (60, 80)
        self.board = np.zeros(self.size[1], np.uint8)
        # background set
        self.clear()


    # clear board with background
    def clear(self):
        # - Clear all items with bg
        self.board[:] = self.bg

    # show board with title (scale x)
    def show(self, scale=10):
        h , w  = self.size[1]
        # show board
        cv2.namedWindow(self.title, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.title, w*scale, h*scale)
        cv2.imshow(self.title, self.board)

    # draw a point in board
    def draw(self, positions, is_draw):
        # chenge color to gray scale
        color = self.fg if is_draw else self.bg
        if type(positions) == list:
            for position in positions:
                self.board[position] = color
        else:
            self.board[positions] = color

    # return free sections in board
    def free(self, revert=False):
        free_block = self.fg if revert else self.bg
        return list(zip(*np.where(self.board == free_block)))
