import os
import shutil
import random


BASE_DIR = '../data'
RAW_DIR = os.path.join(BASE_DIR, 'raw')
TRAIN_IMG_PATH = os.path.join(BASE_DIR, 'train/images')
TRAIN_LABEL_PATH = os.path.join(BASE_DIR, 'train/labels')
VAL_IMG_PATH = os.path.join(BASE_DIR, 'val/images')
VAL_LABEL_PATH = os.path.join(BASE_DIR, 'val/labels')
TEST_IMG_PATH = os.path.join(BASE_DIR, 'test/images')


def split_images_labels(all_files, subfile, name, IMG_DIR, LABEL_DIR=None):
    """
        Args:
            all_files: list   
            subfile: list         
            names: str
            IMD_DIR: str
            LABED_DIR: str
    """

    data = [file for file in all_files if file[:3] in subfile]

    images = [img for img in data if img.endswith(".jpg")]
    labels = [label for label in data if label.endswith(".txt")]

    # create directory if not created
    os.makedirs(IMG_DIR, exist_ok=True)
    os.makedirs(IMG_DIR, exist_ok=True)

    # Copy files to the respective folders
    if IMG_DIR:
        # create directory
        os.makedirs(f"{IMG_DIR}/{name}", exist_ok=True)
        destination = os.path.join(IMG_DIR, name)
        try:
            for img in images:
                IMG_DIR = os.path.join(RAW_DIR, f"{name}/{img}")
                shutil.copy(IMG_DIR, destination)
        except:
            print("Unable to save the images")

    if LABEL_DIR:
        # create directory
        os.makedirs(f"{LABEL_DIR}/{name}", exist_ok=True)
        destination = os.path.join(LABEL_DIR, name)
        try:
            for label in labels:
                LABEL_DIR = os.path.join(RAW_DIR, f"{name}/{label}")
                shutil.copy(LABEL_DIR, destination)
        except:
            print("Unable to save the labels.")


def train_test_split(name, split_ratio, sample=110):
    """
        Args:
            name: str
            split_ratio: list
    """
    # set to the raw data path
    DATA_PATH = os.path.join(RAW_DIR, name)
    files = [filename[:3] for filename in os.listdir(DATA_PATH) if filename.endswith(".txt")]

    # shuffle the data
    random.seed(42)
    random.shuffle(files)

    # randomly takes sample images
    files = random.sample(files, sample)

    # Calculate the split sizes based on the split ratio
    train_size = int(sample * split_ratio[0])
    val_size = int(sample * split_ratio[1])


    # split into train, validation and test set
    train_sets = files[:train_size]
    val_sets = files[train_size:train_size + val_size]
    test_sets = files[train_size+val_size:]

    # split and save the dataset into images and labels
    split_images_labels(os.listdir(DATA_PATH), train_sets, name, TRAIN_IMG_PATH, TRAIN_LABEL_PATH)  # For training set
    split_images_labels(os.listdir(DATA_PATH), val_sets, name, VAL_IMG_PATH, VAL_LABEL_PATH)  # For validation set
    split_images_labels(os.listdir(DATA_PATH), test_sets, name, TEST_IMG_PATH)  # For test set
    

if __name__ == "__main__":
    # set split ratio
    split_ratio = [0.8, 0.15]  # 80% train, 15% validation, 5% test

    # split the raw data into train, validation and test sets.
    train_test_split("buffalo", split_ratio)
    train_test_split("elephant", split_ratio)
    train_test_split("rhino", split_ratio)
    train_test_split("zebra", split_ratio)

