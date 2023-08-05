import os
import glob
import logging
from PIL import Image


RAW_DIR = './data/raw'

# Instantiate logger
logging.basicConfig(filename="./log/preprocess.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def is_normalized(bound_box_dim):
    return 0.0 <= bound_box_dim <= 1.0


def to_yolo_format(label, img_width, img_height):
    """
        Args:
            label:
            img_width: int
            img_heith: int
        
        Returns:
            yolo_format: str
    """
    # class labels
    class_labels = {
            "buffalo": 0,
            "elephant": 1,
            "rhino": 2,
            "zebra": 3,
            "cheetah": 4,
            "fox": 5,
            "jaguar": 6,
            "leopard": 7,
            "lion": 8,
            "panda": 9,
        }


    # Extract the values
    class_label = class_labels[label[0].lower()]
    x_min = label[1]
    y_min = label[2]
    x_max = label[3]
    y_max = label[4]

    # Calculate the center coordinates and dimensions of the bounding box
    center_x = (x_min + x_max) / 2
    center_y = (y_min + y_max) / 2
    width = x_max - x_min
    height = y_max - y_min

    # Normalize the coordinates
    norm_center_x = center_x / img_width
    norm_center_y = center_y / img_height 
    norm_width = width / img_width 
    norm_height = height / img_height

    # Format the YOLO string
    yolo_format = f"{class_label} {norm_center_x:.6f} {norm_center_y:.6f} {norm_width:.6f} {norm_height:.6f}"
    logging.info("Completed Pascal.")

    return yolo_format


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