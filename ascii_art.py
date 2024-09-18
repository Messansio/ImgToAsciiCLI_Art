# Install the required libraries: pip install pillow click
# How to run the script: python ascii_art.py <image_path> --width <width>
# made by Messansio
import click
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 32] for pixel in pixels])
    return ascii_str

def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}.")
        print(e)
        return

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index:(index + img_width)] for index in range(0, ascii_str_len, img_width)])

    print(ascii_img)

@click.command()
@click.argument('image_path')
@click.option('--width', default=100, help='Width of the ASCII art')
def cli(image_path, width):
    """Convert an image to ASCII art."""
    convert_image_to_ascii(image_path, width)

if __name__ == "__main__":
    cli()