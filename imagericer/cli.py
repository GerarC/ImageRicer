from .utils.imageloader import ImageLoader
from .utils.converter import Converter
import click

@click.group
def imagericer() -> None:
    '''Application to change image's color palette.
    '''
    pass

@imagericer.command
@click.option('--image_src', '--image', '-i', help='Image dir.')
@click.option('--output', '-o', help='Converted image output dir.')
@click.option('--filename', '-f', help='Name of the final image.')
@click.option('--palette', '-p', help='path to the dir or file of the Palette.')
@click.option('--prefix', help='Prefix of the Image')
@click.option('--avg_method', is_flag=True, help='Enables avg algorithm.')
@click.option('--blur', is_flag=True, help='Enables gaussian blur.')
@click.option('--quant', is_flag=True, help='Quantize the image')
@click.option('--avg_box', type = (int, int), help='Change the avg box (use with avg_method).')
def rice(image_src: str,
         output: str,
         filename: str,
         palette: str,
         prefix: str,
         avg_method: bool,
         blur: bool,
         quant: bool,
         avg_box: tuple) -> None:
    '''Rices an image given a palette.
    '''
    if not image_src:
        click.echo('There is not Image dir.')
        return
    img_loader = ImageLoader(image_src)
    image = img_loader.load_image()
    out_dir = output if output else img_loader.out
    file_name = filename if filename else img_loader.file
    palette_dir = palette if palette else 'imagericer/palette/'
    
    converter = Converter(image, out_dir, file_name, palette_dir)
    if prefix: converter.prefix = prefix
    if blur: converter.handler.enable_gaussian_blur()
    if avg_method:
        converter.handler.enable_avg_algorithm()
        if avg_box: converter.handler.set_avg_box_data(avg_box[0], avg_box[1])

    click.echo('Image ricing')
    if quant: converter.quantize_image()
    else: converter.convert_image()
    click.echo(
        f'{img_loader.file} Image riced.\n' +
        f'Saved on {out_dir}, with {converter.prefix}{file_name} as name'
    )
