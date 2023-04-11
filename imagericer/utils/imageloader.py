from ImageGoNord import GoNord
import ntpath

class ImageLoader:
    ''' A class to load pillow images

    Args:
        image_src (str): dir of the image.
    '''
    def __init__(self, image_src: str) -> None:
        self.image_src = image_src
        self.handler = GoNord()
        self.out, self.file = ntpath.split(self.image_src)

    def load_image(self):
        '''Loads the image from the source.

        Return:
            image: the image loaded
        '''
        self.image = self.handler.open_image(self.image_src)
        return self.image

