import argparse

from imgprocalgs.algorithms.utilities import Image, create_empty_image

OUTPUT_FILENAME = "negative.jpg"


def make_negative(image_path: str, dest_path: str):
    image = Image(image_path)
    width, height = image.get_size()
    output = create_empty_image(width, height)
    output_pixels = output.load()
    for x in range(width):
        for y in range(height):
            red, green, blue = image.pixels[x, y]
            output_pixels[x, y] = (255 - red, 255 - green, 255 - blue)

    output.save(dest_path)


def parse_args():
    parser = argparse.ArgumentParser(description='Negative algorithm')
    parser.add_argument("--src", type=str, help="Source file path.")
    parser.add_argument("--dest", type=str, help="Destination file path.", default='data/')
    return parser.parse_args()


def main():
    args = parse_args()
    make_negative(args.src, args.dest)
