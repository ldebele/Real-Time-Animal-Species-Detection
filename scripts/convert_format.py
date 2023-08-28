import os
import glob
import logging
from PIL import Image


RAW_DIR = './data/raw'


logging.basicConfig(
            filename="./logs/log.log", 
            filemode='w', 
            level=logging.INFO, 
            format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
        )


def pascal_to_yolo(label_path):
    """
        Args:
            label_path: location of labels
    """

    # retrieve image path
    img_path = label_path.replace(".txt", ".jpg")

    if not os.path.exists(img_path):
        img_path = label_path.replace(".txt", ".JPG")

    # Read the images
    try:
        img = Image.open(img_path)
        width, height = img.size
    except:
       logging.warning("Image is not found")


    # read the labels
    with open(label_path, 'r') as f:
        labels = f.readlines()

    bbox_cordinates = []

    for label in labels:
        label = label.strip().split(" ")
        # convert the string into float
        label = [float(item) if item.replace(".", "", 1).isdigit() else item for item in label]

        # check the bounding box dimension is normalized
        is_normalize = all(list(map(is_normalized, label[1:])))


        if is_normalize:
            return
        else:
            yolo_format = convert_bbox_to_yolo(label, width, height)
            bbox_cordinates.append(yolo_format)

    with open(label_path, 'w') as f:
        for label in bbox_cordinates:
            f.write(f"{str(label)}\n")



def is_normalized(bound_box_dim):
    return 0.0 <= bound_box_dim <= 1.0



def convert_bbox_to_yolo(label, img_width, img_height):
    """
        Args:
            label: list       -> pascal format label
            img_width: int    -> image width
            img_heith: int    -> image height
        
        Returns:
            yolo_format: str   -> yolo format label
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
            "tiger": 7,
            "lion": 8,
            "panda": 9
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

    return yolo_format




if __name__ == "__main__":
    animals = os.listdir(RAW_DIR)

    for animal in animals:
        path_labels = glob.glob(f'{RAW_DIR}/{animal.lower()}/*.txt')
        for path_label in path_labels:
            pascal_to_yolo(path_label)
    
    logging.info("Save the YOLO format into a .txt file.")
    logging.info("Successfully completed the conversion from Pascal format to YOLO format.")

      
