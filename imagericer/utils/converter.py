from ImageGoNord import GoNord
from pathlib import Path
from os import (
    listdir,
    getcwd,
    path,
)

class Converter:
    '''Wraper of GoNord class.

    Args:
        image (Pillow image): The image loaded by pillow.
        out_dir (str): Path where the final image will be placed.
        filename (str): Image filename.
        palette_dir Optional(str): Path of the color palette (dir or file).
        prefix Optional(str): Prefix of the final filename.
    '''
    def __init__(self,
                 image,
                 out_dir: str,
                 filename: str,
                 palette_dir='imagericer/palette/',
                 prefix='Riced-') -> None:
        self.handler = GoNord()
        self.prefix = prefix
        self.set_new_image(image, out_dir, filename)

        if palette_dir=='imagericer/palette/': palette_dir = str(Path(__file__).parent.parent.parent) + '/' + palette_dir

        self.load_palette(palette_dir)

    def load_palette(self, palette_dir='imagericer/palette/'):
        '''Loads the color palette, whether dir palette or file.
        
        Args:
            palette_dir (str): Path of the color palette.
        '''
        self.palette_dir = palette_dir
        self.handler.reset_palette()

        if path.isfile(palette_dir):
            self.palette = self.palette
            self.handler.add_color_to_palette(palette_dir)
        elif path.isdir(palette_dir):
            self.handler.set_palette_lookup_path(self.palette_dir)  
            self.palette = listdir(palette_dir)
            for p in self.palette:
                self.handler.add_file_to_palette(p)

    def set_new_image(self, image, out_dir: str, filename: str):
        '''Set new image and direction for a new

        Args:
            image (Pillow image): The image loaded by pillow.
            out_dir Optional[str]: Path where the final image will be placed.
            filename Optional[str]: Image filename.
        '''
        self.image = image
        if out_dir: self.out_dir = out_dir
        if filename: self.filename = filename

    def convert_image(self):
        '''Converts the image and save it in the out_dir path with filename name
        '''
        save_path = f'{self.out_dir}/{self.prefix}{self.filename}'
        self.handler.convert_image(self.image, save_path=save_path)

    def quantize_image(self):
        '''quantize the image and save it in the out_dir path with filename name
        '''
        save_path = f'{self.out_dir}/Q{self.prefix}{self.filename}'
        self.handler.convert_image(self.image, save_path=save_path)
