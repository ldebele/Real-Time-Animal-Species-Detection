import os
import unittest
from parameterized import parameterized



class TestData(unittest.TestCase):
        
    @parameterized.expand([
        ('./data/images/train/buffalo', './data/labels/train/buffalo'),
        ('./data/images/train/cheetah', './data/labels/train/cheetah'),
        ('./data/images/train/elephant', './data/labels/train/elephant'),
        ('./data/images/train/fox', './data/labels/train/fox'),
        ('./data/images/train/jaguar', './data/labels/train/jaguar'),
        ('./data/images/train/tiger', './data/labels/train/tiger'),
        ('./data/images/train/lion', './data/labels/train/lion'),
        ('./data/images/train/panda', './data/labels/train/panda'),
        ('./data/images/train/rhino', './data/labels/train/rhino'),
        ('./data/images/train/zebra', './data/labels/train/zebra'),
    ])
    def test_images_labels_contain_same_file(self, IMG_DIR, LABEL_DIR):
        images = [file[:-4] for file in os.listdir(IMG_DIR)]
        labels = [file[:-4] for file in os.listdir(LABEL_DIR)]
        
        # test labels and images contains the same files.
        self.assertEqual(set(images), set(labels))

        # test labels and images have the same length
        self.assertEqual(len(images), len(labels))

        # test no duplicate images and labels
        self.assertEqual(len(set(images)), len(images))
        self.assertEqual(len(set(labels)), len(labels))


    @parameterized.expand([
        ('./data/images/val/buffalo', './data/images/test/buffalo'),
        ('./data/images/val/cheetah', './data/images/test/cheetah'),
        ('./data/images/val/elephant', './data/images/test/elephant'),
        ('./data/images/val/fox', './data/images/test/fox'),
        ('./data/images/val/jaguar', './data/images/test/jaguar'),
        ('./data/images/val/tiger', './data/images/test/tiger'),
        ('./data/images/val/lion', './data/images/test/lion'),
        ('./data/images/val/panda', './data/images/test/panda'),
        ('./data/images/val/rhino', './data/images/test/rhino'),
        ('./data/images/val/zebra', './data/images/test/zebra'),
    ])
    def test_val_test_contains_different_file(self, VAL_DIR, TEST_DIR):
        val_img = [file[:-4] for file in os.listdir(VAL_DIR)]
        test_img = [file[:-4] for file in os.listdir(TEST_DIR)]
        found = [valimg for valimg in val_img if all(valimg == testimg for testimg in test_img)]

        self.assertEqual(len(found), 0)
        



if __name__ == '__main__':
    unittest.main()
