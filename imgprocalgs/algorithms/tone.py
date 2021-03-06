import argparse
import functools
from imgprocalgs.algorithms.utilities import Image, create_empty_image, ImageData, get_greyscale
from imgprocalgs.visualisation.server import App


def make_sepia(image_path: str, dest_path: str, factor: int):
    image = Image(image_path)
    width, height = image.get_size()
    output = create_empty_image(width, height)
    output_pixels = output.load()
    for x in range(width):
        for y in range(height):
            red, green, blue = image.pixels[x, y]
            grey_red = int(get_greyscale(red, green, blue))
            grey_green = int(get_greyscale(red, green, blue))
            grey_blue = int(get_greyscale(red, green, blue))

            output_pixels[x, y] = (grey_red + 2 * factor, grey_green + factor, grey_blue)

    output.save(dest_path)


make_sepia_5 = functools.partial(make_sepia, 'tests/data/desert.jpg', 'data/desert_sepia_5.jpg', factor=5)
make_sepia_10 = functools.partial(make_sepia, 'tests/data/desert.jpg', 'data/desert_sepia_10.jpg', factor=10)
make_sepia_20 = functools.partial(make_sepia, 'tests/data/desert.jpg', 'data/desert_sepia_20.jpg', factor=20)
make_sepia_30 = functools.partial(make_sepia, 'tests/data/desert.jpg', 'data/desert_sepia_30.jpg', factor=30)
make_sepia_40 = functools.partial(make_sepia, 'tests/data/desert.jpg', 'data/desert_sepia_40.jpg', factor=40)
make_sepia_50 = functools.partial(make_sepia, 'tests/data/desert.jpg', 'data/desert_sepia_50.jpg', factor=50)
make_sepia_60 = functools.partial(make_sepia, 'tests/data/desert.jpg', 'data/desert_sepia_60.jpg', factor=60)


def example(app: App):
    make_sepia_5()
    make_sepia_10()
    make_sepia_20()
    make_sepia_30()
    make_sepia_40()
    make_sepia_50()
    make_sepia_60()

    data = {
        'title': 'Sepia algorithm',
        'header': 'Sepia algorithm with following factors: 5, 10, 20, 30, 40, 50, 60',
        'image_data': [
            ImageData("Factor: 5", "desert_sepia_5.jpg"),
            ImageData("Factor: 10", "desert_sepia_10.jpg"),
            ImageData("Factor: 20", "desert_sepia_20.jpg"),
            ImageData("Factor: 30", "desert_sepia_30.jpg"),
            ImageData("Factor: 40", "desert_sepia_40.jpg"),
            ImageData("Factor: 50", "desert_sepia_50.jpg"),
            ImageData("Factor: 60", "desert_sepia_60.jpg"),
        ]
    }
    app.register_route("/", template_name="main_page.html", **data)


def parse_args():
    parser = argparse.ArgumentParser(description='Tone algorithms')
    parser.add_argument("--src", type=str, help="Source file path.")
    parser.add_argument("--dest", type=str, help="Destination file path.", default='data/')
    parser.add_argument("--factor", type=int, help="Sepia factor value")
    parser.add_argument("--example", type=bool, help="Show example", default=False)
    parser.add_argument("--visualize", type=bool, help="Open visualization in webbrowser", default=False)
    return parser.parse_args()


def main():
    args = parse_args()
    app = App()
    if args.example:
        example(app)
        app.run_server('127.0.0.1', 8000, open_webiste=args.visualize)
    else:
        make_sepia(args.src, args.dest, args.factor)


if __name__ == "__main__":
    app = App()
    example(app)
    app.run_server("127.0.0.1", 8001, open_webiste=True)
