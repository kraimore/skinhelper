from PIL import Image
import argparse
import glob
input_dir = ""

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Specify input directory")
    args = parser.parse_args()
    if args.input:
        input_dir = args.input
    for file in glob.glob("*@2x.png"):
        img = Image.open(file)
        (width, height) = (img.width // 2, img.height // 2)
        img_resized = img.resize((width, height))
        img_resized.save(file.replace("@2x",""))

