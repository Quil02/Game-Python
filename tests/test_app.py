import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add project root to sys.path so we can import App
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import App

class TestApp(unittest.TestCase):

    @patch('App.clear')
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('App.hangman_menu')
    def test_main_menu_option_1(self, mock_hangman, mock_print, mock_input, mock_clear):
        # Setup input to select '1' then 'q'
        mock_input.side_effect = ['1', 'q']
        
        with self.assertRaises(SystemExit):
            App.main_menu()
            
        mock_hangman.assert_called_once()

    @patch('App.clear')
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('App.tebak_angka_menu')
    def test_main_menu_option_2(self, mock_tebak, mock_print, mock_input, mock_clear):
        mock_input.side_effect = ['2', 'q']
        with self.assertRaises(SystemExit):
            App.main_menu()
        mock_tebak.assert_called_once()

    @patch('App.clear')
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('App.bgk_menu')
    def test_main_menu_option_3(self, mock_bgk, mock_print, mock_input, mock_clear):
        mock_input.side_effect = ['3', 'q']
        with self.assertRaises(SystemExit):
            App.main_menu()
        mock_bgk.assert_called_once()
    
    @patch('App.clear')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main_menu_option_q(self, mock_print, mock_input, mock_clear):
        mock_input.side_effect = ['q']
        
        # Expect sys.exit() to be called
        with self.assertRaises(SystemExit):
            App.main_menu()

if __name__ == '__main__':
    unittest.main()
