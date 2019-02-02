from ImageLoader import ImageLoader


class ImageHolder:
    EMPTY_PIECE_PATH = 'pieces/empty_piece.png'
    BLACK_PIECE_PATH = 'pieces/black_piece.png'
    RED_PIECE_PATH = 'pieces/red_piece.png'

    def __init__(self):
        self.empty_piece_image = ImageLoader.load_image(self.EMPTY_PIECE_PATH)
        self.black_piece_image = ImageLoader.load_image(self.BLACK_PIECE_PATH)
        self.red_piece_image = ImageLoader.load_image(self.RED_PIECE_PATH)
