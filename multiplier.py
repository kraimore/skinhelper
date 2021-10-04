from PIL import Image
import argparse
import os.path
import glob


img_input = ""
img_output = ""
n = 0
f = 0
hd = ""
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "Specify input image (i.e followpoint.png)")
    parser.add_argument("-o", "--output", help = "Specify output image (i.e. followpoint)")
    parser.add_argument("-n", "--number", help = "Specify image count")
    parser.add_argument("-f", "--first", help = "Specify first image number (default: 0)")
    parser.add_argument("-hd", action="store_true", help=  "Specifies that the elements are HD sized (@2x)")
    args = parser.parse_args()

    if args.input:
        img_input = args.input
    if args.hd:
        hd = "@2x"
    if args.output:
        img_output = args.output
        i = 0
    else:
        img_output = args.input.replace(".png", "")
        i = 1
    if args.first:
        f = int(args.first)
    if args.number:
        n  = int(args.number) + f - 1
    img = Image.open(img_input)
    while n >= f:
        if i == 1:
            img.save(img_output.strip("@2x") + "-" + str(n) + hd + ".png")
        else:
            if ":\\" in img_input:

                img.save(os.path.dirname(img_input) + "\\" + img_output + "-" + str(n) + hd + ".png")
            else:
                img.save(os.path.dirname(img_input) + img_output + "-" + str(n) + hd + ".png")
        n = n - 1
