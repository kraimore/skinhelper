from PIL import Image
import argparse
import os.path


img_input = ""
img_output = ""
n = 0
f = 0
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "Specify input image (i.e followpoint.png)")
    parser.add_argument("-o", "--output", help = "Specify output image (i.e. followpoint-)")
    parser.add_argument("-n", "--number", help = "Specify image count")
    parser.add_argument("-f", "--first", help="Specify first image number (default: 0)")
    args = parser.parse_args()

    if args.input:
        img_input = args.input
    if args.output:
        img_output = args.output
        i = 0
    else:
        img_output = args.input.replace(".png", "") + "-"
        i = 1
    if args.first:
        f = int(args.first)
    if args.number:
        n  = int(args.number) + f - 1
    img = Image.open(img_input)
    while n >= f:
        if i == 1:
            img.save(img_output + str(n) + ".png")
        else:
            img.save(os.path.dirname(img_input)  + "\\" + img_output + str(n) + ".png")
        n = n - 1
