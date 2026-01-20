import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tebak_angka import tebak_angka

class TestTebakAngka(unittest.TestCase):

    def test_number_generator_logic(self):
        # If number is provided (not 0), checks logic.
        # But wait, number_generator has complex logic with user input loops if conditions fail.
        # Let's test the simple success case: number=0 -> generates random.
        
        with patch('tebak_angka.tebak_angka.randint', return_value=50):
            res = tebak_angka.number_generator(1, 100, 5, 0)
            # returns first, last, percobaan, number
            self.assertEqual(res, (1, 100, 5, 50))

    @patch('tebak_angka.tebak_angka.clear')
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('tebak_angka.tebak_angka.game')
    def test_menu_options(self, mock_game, mock_print, mock_input, mock_clear):
        # Option 2: 1-10
        mock_input.side_effect = ['2']
        tebak_angka.menu()
        mock_game.assert_called_once()
        args, _ = mock_game.call_args
        # args should be output of number_generator(1, 10, 3) which is (1, 10, 3, random_val)
        self.assertEqual(args[0], 1)
        self.assertEqual(args[1], 10)
        self.assertEqual(args[2], 3)
    
    @patch('tebak_angka.tebak_angka.clear')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_menu_quit(self, mock_print, mock_input, mock_clear):
        mock_input.side_effect = ['q']
        with self.assertRaises(SystemExit):
            tebak_angka.menu()

if __name__ == '__main__':
    unittest.main()
