import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bgk import bgk

class TestBgk(unittest.TestCase):

    def test_bot_pilihan(self):
        with patch('bgk.bgk.randint', return_value=0): # 0 -> 'b'
            self.assertEqual(bgk.bot_pilhan(), 'b')

    @patch('bgk.bgk.clear')
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('bgk.bgk.game')
    def test_menu_options(self, mock_game, mock_print, mock_input, mock_clear):
        # Option 2: Score 1, then 'q' to exit
        mock_input.side_effect = ['2', 'q']
        
        with self.assertRaises(SystemExit):
            bgk.menu()
            
        mock_game.assert_called_with(1)

    @patch('bgk.bgk.clear')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_menu_quit(self, mock_print, mock_input, mock_clear):
        mock_input.side_effect = ['q']
        with self.assertRaises(SystemExit):
            bgk.menu()

    @patch('bgk.bgk.clear')
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('bgk.bgk.bot_pilhan')
    @patch('bgk.bgk.option_after_game')
    def test_game_win(self, mock_option, mock_bot, mock_print, mock_input, mock_clear):
        # Player picks 'b', Bot picks 'g' -> Bot wins? Wait.
        # b vs g: g wins (paper covers rock). So Bot wins.
        # We want player to win to test "Selamat Anda Menang".
        # Player 'b' (Batu), Bot 'k' (Gunting). Batu crushes Gunting.
        
        # Scenario: fix_score = 1.
        # Round 1: Player 'b', Bot 'k'. Player score -> 1.
        # Loop checks fix_score == pemain_menang -> Returns.
        
        mock_input.side_effect = ['b'] 
        mock_bot.return_value = 'k'
        mock_option.side_effect = lambda: None # Just return
        
        bgk.game(1)
        
        # Verify appropriate prints or calls
        # We can check if option_after_game was called, meaning game ended.
        mock_option.assert_called_once()

if __name__ == '__main__':
    unittest.main()
