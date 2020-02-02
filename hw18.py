#!/usr/bin/python3
import argparse
from PIL import Image


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Creates thumbnail pictures')

    parser.add_argument('photos', metavar='N', type=str, nargs='+', help='input photos')
    parser.add_argument('-s', help='choose output image size, format : {width}x{height}', type=str, required=True)

    args = parser.parse_args()

    width, height = dict(args._get_kwargs())["s"].split("x")
    width = int(width)
    height = int(height)
    
    for fname in args.photos:
        img = Image.open(fname)
        img.thumbnail((width, height))

        # creating new file name
        dot_index = fname.rfind(".")
        if dot_index == -1:
            name, ext = fname, ".jpg"
        else:
            name, ext = fname[:dot_index], fname[dot_index:]
        save_path = name + "_thumbnail" + ext

        img.save(save_path)
        print(f"Image {fname} saved in {save_path} with size {width} x {height}")