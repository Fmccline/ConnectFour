from PIL import Image, ImageTk


class ImageLoader:

    @staticmethod
    def load_image(path):
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        return photo

