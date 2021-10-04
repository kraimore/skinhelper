from PIL import Image
import argparse
import glob
import os
input_dir = ""

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Specify input directory")
    args = parser.parse_args()
    if args.input:
        input_dir = args.input
    print(os.path.join(input_dir))
    input_dir.strip('"')
    print(os.path.join(input_dir.strip('"')))
    for file in glob.glob(os.path.join(input_dir.strip('"')) + "\\" + "*@2x.png"):
        img = Image.open(file)
        if img.width > 1 and img.height > 1:
            (width, height) = (img.width // 2, img.height // 2)
            img_resized = img.resize((width, height))
            print(input_dir + file.replace("@2x",""))
            img_resized.save(file.replace("@2x",""))
