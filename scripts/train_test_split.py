import os
import shutil
import random


BASE_DIR = '../data'
RAW_DIR = os.path.join(BASE_DIR, 'raw')


def images_labels_split(all_files, subfile, name, mode):
    """
        Args:
            all_files: list   
            subfile: list         
            names: str
            mode: str
    """

    # select file names from all files.
    data = [file for file in all_files if file[:3] in subfile]

    images = [img for img in data if img.endswith(".jpg")]
    labels = [label for label in data if label.endswith(".txt")]   

    # Copy files to the respective folders
    # create directory if not created
    IMG_DIR = os.path.join(BASE_DIR, f'images/{mode}/{name}')
    os.makedirs(IMG_DIR, exist_ok=True)
    try:
        for img in images:
            RAW_IMG_DIR = os.path.join(RAW_DIR, f"{name}/{img}")
            shutil.copy(RAW_IMG_DIR, IMG_DIR)
    except:
        print("Unable to save the images")
 
    # create directory if not created
    LABEL_DIR = os.path.join(BASE_DIR, f'labels/{mode}/{name}')
    os.makedirs(LABEL_DIR, exist_ok=True)
    try:
        for label in labels:
            RAW_LABEL_DIR = os.path.join(RAW_DIR, f"{name}/{label}")
            shutil.copy(RAW_LABEL_DIR, LABEL_DIR)
    except:
        print("Unable to save the labels.")


def train_test_split(name, split_ratio, sample=150):
    """
        Args:
            name: str
            split_ratio: list
            sample: int
    """

    # set to the raw data path
    DATA_PATH = os.path.join(RAW_DIR, name)
    files = [filename[:3] for filename in os.listdir(DATA_PATH) if filename.endswith(".txt")]

    # shuffle the data
    random.seed(42)
    random.shuffle(files)

    # randomly takes sample images
    if sample < len(files):
        files = random.sample(files, sample)

    # Calculate the split sizes based on the split ratio
    train_size = int(sample * split_ratio[0])
    val_size = int(sample * split_ratio[1])


    # split into train, validation and test set
    train_sets = files[:train_size]
    val_sets = files[train_size:train_size + val_size]
    test_sets = files[train_size+val_size:]

    # split and save the dataset into images and labels
    images_labels_split(os.listdir(DATA_PATH), train_sets, name, mode="train")  # For training set
    images_labels_split(os.listdir(DATA_PATH), val_sets, name, mode="val")  # For validation set
    images_labels_split(os.listdir(DATA_PATH), test_sets, name, mode="test")  # For test set
    

if __name__ == "__main__":
    # set split ratio
    split_ratio = [0.8, 0.15]  # 80% train, 15% validation, 5% test

    # list all animals
    animals = os.listdir(RAW_DIR)

    for animal in animals:
        # split the raw data into train, validation and test sets.
        train_test_split(animal, split_ratio)
