import os
import shutil
import random
import logging


BASE_DIR = './data'
RAW_DIR = os.path.join(BASE_DIR, 'raw')

logging.basicConfig(
            filename="./logs/log.log", 
            filemode='a', 
            level=logging.INFO, 
            format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
        )


def train_test_split(name, split_ratio, sample=150):
    """
        Args:
            name: str               -> name of an animal
            split_ratio: list       -> list of split ratio
            sample: int             -> sample size
    """

    # set to the raw data path
    DATA_PATH = os.path.join(RAW_DIR, name)
    files = [filename[:-4] for filename in os.listdir(DATA_PATH) if filename.endswith(".txt")]

    # shuffle the data
    random.seed(42)
    random.shuffle(files)

    # randomly takes sample images
    if sample >= len(files):
        sample = len(files)
    
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
    logging.info(f"Split the {name} dataset into train, validation and test sets")



def images_labels_split(raw_files, subfile, name, mode):
    """
        Args:
            raw_files: list     -> location of raw files.
            subfile: list       -> list of randomly selected files.
            names: str          -> names of an animal
            mode: str           -> type of sets (train, val, test)
    """

    # select file names from all files.
    data = [file for file in raw_files if file[:-4] in subfile]

    images = [img for img in data if img.endswith(".jpg") | img.endswith(".JPG")]
    labels = [label for label in data if label.endswith(".txt")]  

    # images and labels data mustbe equal.
    assert len(images) == len(labels)

    # Copy files to the respective folders
    # create directory if not created
    IMG_DIR = os.path.join(BASE_DIR, f'images/{mode}/{name}')
    os.makedirs(IMG_DIR, exist_ok=True)
    try:
        for img in images:
            RAW_IMG_DIR = os.path.join(RAW_DIR, f"{name}/{img}")
            shutil.copy(RAW_IMG_DIR, IMG_DIR)
            # logging.info(f"Copy the raw images into {mode} set")
    except:
        logging.warning("Unable to save the images.")
 
    # create directory if not created
    LABEL_DIR = os.path.join(BASE_DIR, f'labels/{mode}/{name}')
    os.makedirs(LABEL_DIR, exist_ok=True)
    try:
        for label in labels:
            RAW_LABEL_DIR = os.path.join(RAW_DIR, f"{name}/{label}")
            shutil.copy(RAW_LABEL_DIR, LABEL_DIR)
            # logging.info(f"Copy the raw labels into {mode} set")
    except:
        logging.warning("Unable to save the labels.")



if __name__ == "__main__":
    # set split ratio
    split_ratio = [0.7, 0.15]  # 70% train, 15% validation, 15% test

    # list all animals
    animals = os.listdir(RAW_DIR)

    for animal in animals:
        # split the raw data into train, validation and test sets.
        train_test_split(animal, split_ratio)

    logging.info("Successfully completed the datasets splitting.")
