# Unit tests for CNN model
import unittest
from src.computer_vision.cnn_model import PlantDiseaseCNN

class TestCNNModel(unittest.TestCase):
    def test_model_init(self):
        model = PlantDiseaseCNN()
        self.assertIsNotNone(model)
        # TODO: Add more tests

if __name__ == '__main__':
    unittest.main()
