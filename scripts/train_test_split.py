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



def split_images_labels(all_files, subfile, names, img_destination, label_destination=None):
    """
        Args:
            img_destination:
            label_destination:
            all_files: list    ->
            subfile: list         ->
            type: str          ->
    """

    data = [file for file in all_files if file[:3] in subfile]

    images = [img for img in data if img.endswith(".jpg")]
    labels = [label for label in data if label.endswith(".txt")]

    # Copy files to the respective folders
    try:
        for img in images:
            IMG_DIR = os.path.join(RAW_DIR, f"{names}/{img}")
            shutil.copy(IMG_DIR, img_destination)
    except:
        print("Unable to save the images")

    try:
        for label in labels:
            LABEL_DIR = os.path.join(RAW_DIR, f"{names}/{label}")
            shutil.copy(LABEL_DIR, label_destination)
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
    split_images_labels(os.listdir(DATA_PATH), train_sets, name, TRAIN_IMG_PATH, TRAIN_LABEL_PATH,)  # For training set
    split_images_labels(os.listdir(DATA_PATH), val_sets, name, VAL_IMG_PATH, VAL_LABEL_PATH)  # For validation set
    split_images_labels(os.listdir(DATA_PATH), test_sets, name, TEST_IMG_PATH)  # For test set
    

if __name__ == "__main__":
    # set split ratio
    split_ratio = [0.8, 0.15]  # 80% train, 15% validation, 5% test

    # 
    train_test_split("buffalo", split_ratio)
    train_test_split("elephant", split_ratio)
    train_test_split("rhino", split_ratio)
    train_test_split("zebra", split_ratio)

