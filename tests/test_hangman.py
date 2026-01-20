import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Hangman import Hangman

class TestHangman(unittest.TestCase):
    
    def test_random(self):
        # Mock randint to return 0, which corresponds to index 0 of the input list
        with patch('Hangman.Hangman.randint', return_value=0):
            result = Hangman.random(['A', 'B'])
            self.assertEqual(result, 'a') # It calls .lower()

    def test_close(self):
        # close replaces alpha chars with '-', leaves others
        self.assertEqual(Hangman.close("abc"), ["-", "-", "-"])
        self.assertEqual(Hangman.close("a b"), ["-", " ", "-"])
        self.assertEqual(Hangman.close("123"), ["1", "2", "3"])

    def test_find_index(self):
        self.assertEqual(Hangman.find_index("banana", "a"), [1, 3, 5])
        self.assertEqual(Hangman.find_index("banana", "z"), [])

    @patch('Hangman.Hangman.clear')
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('Hangman.Hangman.playgames')
    def test_menu_options(self, mock_play, mock_print, mock_input, mock_clear):
        # Test option 2 (random sentence)
        mock_input.side_effect = ['2', 'b'] # 2 then b to return
        Hangman.menu()
        mock_play.assert_called_once()
        
    @patch('Hangman.Hangman.clear')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_menu_quit(self, mock_print, mock_input, mock_clear):
        mock_input.side_effect = ['q']
        with self.assertRaises(SystemExit):
            Hangman.menu()

if __name__ == '__main__':
    unittest.main()
