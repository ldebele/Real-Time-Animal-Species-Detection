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
        ('./data/images/train/leopard', './data/labels/train/leopard'),
        ('./data/images/train/lion', './data/labels/train/lion'),
        ('./data/images/train/panda', './data/labels/train/panda'),
        ('./data/images/train/rhino', './data/labels/train/rhino'),
        ('./data/images/train/zebra', './data/labels/train/zebra')
    ])
    def test_len_images_labels(self, IMG_DIR, LABEL_DIR):
        images = [file[:-4] for file in os.listdir(IMG_DIR)]
        labels = [file[:-4] for file in os.listdir(LABEL_DIR)]
        self.assertEqual(len(images), len(labels))


    @parameterized.expand([
        ('./data/images/train/buffalo', './data/labels/train/buffalo'),
        ('./data/images/train/cheetah', './data/labels/train/cheetah'),
        ('./data/images/train/elephant', './data/labels/train/elephant'),
        ('./data/images/train/fox', './data/labels/train/fox'),
        ('./data/images/train/jaguar', './data/labels/train/jaguar'),
        ('./data/images/train/leopard', './data/labels/train/leopard'),
        ('./data/images/train/lion', './data/labels/train/lion'),
        ('./data/images/train/panda', './data/labels/train/panda'),
        ('./data/images/train/rhino', './data/labels/train/rhino'),
        ('./data/images/train/zebra', './data/labels/train/zebra')
    ])
    def test_images_labels_contain_same_file(self, IMG_DIR, LABEL_DIR):
        images = [file[:-4] for file in os.listdir(IMG_DIR)]
        labels = [file[:-4] for file in os.listdir(LABEL_DIR)]
        self.assertEqual(set(images), set(labels))


if __name__ == '__main__':
    unittest.main()