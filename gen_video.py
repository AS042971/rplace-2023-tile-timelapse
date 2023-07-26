import argparse
import csv
from io import BytesIO

import requests
from PIL import Image
from alive_progress import alive_bar


def clipImage(index: int, id: str, url: str, left: int, upper: int, right: int, lower: int, out: str):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    cropped = image.crop((left, upper, right, lower))
    cropped.save(f'{out}/{index:05}.png')

def genVideo(frame: str, left: int, upper: int, right: int, lower: int, out: str):
    csv_path = f'./data/{frame}.csv'
    with open(csv_path, newline='') as f:
        row_count = sum(1 for line in f)
    with open(csv_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        with alive_bar(row_count) as bar:
            for index, row in enumerate(spamreader):
                clipImage(index, row[0], 'https://garlic-bread.reddit.com/media/canvas-images/full-frame/' + row[1], left, upper, right, lower, out)
                bar()

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("frame",
                        help="The frame of the full r/place canvas. Possible values: 0 to 5.")
    parser.add_argument("left",
                        help="The left column index for the clipped image, use reference/{frame}.png to locate.")
    parser.add_argument("upper",
                        help="The upper row index for the clipped image, use reference/{frame}.png to locate.")
    parser.add_argument("right",
                        help="The right column index for the clipped image, use reference/{frame}.png to locate.")
    parser.add_argument("lower",
                        help="The lower row index for the clipped image, use reference/{frame}.png to locate.")
    parser.add_argument("--out", default="./output",
                        help="Output directory for the clipped images")
    args = parser.parse_args()
    genVideo(args.frame, int(args.left), int(args.upper), int(args.right), int(args.lower), args.out)


if __name__ == '__main__':
    main()