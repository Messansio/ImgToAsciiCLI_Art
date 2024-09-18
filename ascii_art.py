# Install the required libraries: pip install pillow click
# How to run the script: python ascii_art.py <imagePath> --width <width>
# made by Messansio
import click
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resizeImage(image, newWidth=100):
    width, height = image.size
    aspectRatio = height / width
    newHeight = int(aspectRatio * newWidth)
    resizedImage = image.resize((newWidth, newHeight))
    return resizedImage

def grayify(image):
    grayscaleImage = image.convert("L")
    return grayscaleImage

def pixelsToAscii(image):
    pixels = image.getdata()
    asciiStr = "".join([ASCII_CHARS[pixel // 32] for pixel in pixels])
    return asciiStr

def imgToAscii(imagePath, newWidth=100):
    try:
        image = Image.open(imagePath)
    except Exception as e:
        print(f"Unable to open image file {imagePath}.")
        print(e)
        return

    image = resizeImage(image, newWidth)
    image = grayify(image)
    asciiStr = pixelsToAscii(image)

    imgWidth = image.width
    asciiStrLen = len(asciiStr)
    asciiImg = "\n".join([asciiStr[index:(index + imgWidth)] for index in range(0, asciiStrLen, imgWidth)])

    print(asciiImg)

@click.command()
@click.argument('imagePath')
@click.option('--width', default=100, help='Width of the ASCII art')
def cli(imagePath, width):
    """Convert an image to ASCII art."""
    imgToAscii(imagePath, width)

if __name__ == "__main__":
    cli()