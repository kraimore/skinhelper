from PIL import Image
import argparse


img_input = ""
img_output = ""
n = 0
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "Specify input image (i.e followpoint.png)")
    parser.add_argument("-o", "--output", help = "Specify output image (i.e. followpoint-)")
    parser.add_argument("-n", "--number", help = "Specify image count")
    args = parser.parse_args()

    if args.input:
        img_input = args.input
    if args.output:
        img_output = args.output
    if args.number:
        n = int(args.number)
    img = Image.open(img_input)
    while n >= 0:
        img.save(img_output + str(n) + ".png")
        n = n - 1




