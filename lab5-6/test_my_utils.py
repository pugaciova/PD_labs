import unittest
import my_utils
from unittest.mock import patch

class TestMyUtils(unittest.TestCase):
    def test_get_current_date(self):
        current_date = my_utils.get_current_date()
        self.assertIsNotNone(current_date)

    def test_list_files_in_directory(self):
        directory_path = "."  # Текущая директория
        files = my_utils.list_files_in_directory(directory_path)
        self.assertIsInstance(files, list)

class TestDisplayImage(unittest.TestCase):
    @patch('builtins.print')  
    def test_display_image_with_valid_path(self, mock_print):
        image_path = "C:\\pd_labs\\dataset\\zebra\\0000.jpg"  
        my_utils.display_image(image_path)
        mock_print.assert_not_called()  


if __name__ == "__main__":
    unittest.main()
