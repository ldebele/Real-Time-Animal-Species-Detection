import os
import glob
import logging
from PIL import Image


RAW_DIR = './data/raw'

# Instantiate logger
logging.basicConfig(filename="./log/preprocess.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def is_normalized(bound_box_dim):
    return 0.0 <= bound_box_dim <= 1.0



def convert_to_yolo(label_path):
    """
        Args:
            label: 
    """

    # Read the images
    try:
        img_path = label_path.replace(".txt", ".jpg")
        img = Image.open(img_path)
    except:
        img_path = label_path.replace(".txt", ".JPG")
        img = Image.open(img_path)
        
    width, height = img.size

    # read the labels
    with open(label_path, 'r') as f:
        label = f.readline().strip().split(" ")


    # convert the string into float
    label = [float(item) if item.replace(".", "", 1).isdigit() else item for item in label]

    # check the bounding box dimension is normalized
    is_normalize = all(list(map(is_normalized, label[1:])))


    if is_normalize:
        return
    else:
        yolo_format = to_yolo_format(label, width, height)

        logging.info("save yolo format into txt file.")
        with open(label_path, 'w') as f:
            f.write(yolo_format)



if __name__ == "__main__":
    animals = os.listdir(RAW_DIR)

    for animal in animals:
        labels = glob.glob(f'{RAW_DIR}/{animal.lower()}/*.txt')
        for label in labels:
            convert_to_yolo(label)
        # map(convert_to_yolo, labels)