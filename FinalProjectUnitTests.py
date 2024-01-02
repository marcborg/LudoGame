import unittest
from FinalProject import LudoGame

class TestFinalProject(unittest.TestCase):
    
    # Tests given by instructor

    def test1(self):
        players = ['A','B','C','D']
        turns = [('A', 6),('A', 1),('B', 6),('B', 2),('C', 6),('C', 3),('D', 6),('D', 4)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['1', 'H', '16', 'H', '31', 'H', '46', 'H'])
    
    def test2(self):
        players = ['A','B']
        turns = [('B', 6),('B', 4),('B', 5),('B', 4),('B', 4),('B', 3),('B', 4),('B', 5),('B', 4),('B', 4),('B', 5),('B', 4),('B', 1),('B', 4),('B', 5),('B', 5),('B', 5)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['H', 'H', 'B6', 'H'])

    def test3(self):
        players = ['A','B']
        turns = [('A', 6),('A', 3),('A', 6),('A', 3),('A', 6),('A', 5),('A', 4),('A', 6),('A', 4)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['28', '28', 'H', 'H'])

    def test4(self):
        players = ['A','C']
        turns = [('A', 6),('A', 4),('A', 4),('A', 4),('A', 5),('A', 6),('A', 4),('A', 6),('A', 4),('A', 6),('A', 6),('A', 6),('A', 4),('A', 6),('A', 6),('C', 6),('C', 4)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['33', 'H', '32', 'H'])

    def test5(self):
        players = ['A','B']
        turns = [('A', 6),('A', 4),('A', 4),('A', 4),('A', 5),('A', 6),('A', 4),('A', 6),('A', 4),('A', 6),('A', 6),('A', 4),('A', 6),('A', 4),('A', 6),('A', 6),('A', 4),('A', 6),('A', 6),('A', 4),('A', 6),('A', 6),('A', 4),('A', 6),('A', 3),('A', 6),('B', 6),('A', 6)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['E', 'E', 'R', 'H'])
    
    def test6(self):
        players = ['A','B']
        turns = [('A', 6),('A', 2),('A', 2),('A', 6),('A', 4),('A', 5),('A', 4),('A', 4),('B', 6),('B', 3),('A', 6),('A', 3)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['3', 'H', '17', 'H'])

    def test7(self):
        players = ['A','B']
        turns = [('A', 6),('A', 4),('A', 5),('A', 4),('A', 4),('A', 4),('A', 5),('A', 4),('A', 5),('A', 5),('A', 3),('A', 5),('A', 3),('A', 6)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['A1', 'R', 'H', 'H'])

    def test8(self):
        players = ['A','B']
        turns = [('A', 6),('A', 4),('A', 5),('A', 4),('A', 4),('A', 4),('A', 5),('A', 4),('A', 5),('A', 5),('A', 3),('A', 5),('A', 5),('A', 6),('A', 5),('A', 5),('A', 3),('B', 6),('B', 3),('A', 4)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['E', '13', '17', 'H'])

    def test9(self):
        players = ['A','B']
        turns = [('A', 6),('A', 4),('A', 4),('A', 4),('A', 6),('A', 5),('A', 3),('B', 6),('B', 2),('A', 2),('A', 4)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['16', '10', 'H', 'H'])

    # Tests designed to strictly test one player moving, in this case player A

    def test10(self):
        # tests to see if token p moves to the R space name
        players = ['A']
        turns = [('A', 6)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['R', 'H'])

    def test11(self):
        # tests to see if token q moves to the R space name after p already did
        players = ['A']
        turns = [('A', 6), ('A', 6)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['R', 'R'])

    def test12(self):
        # tests to see if token p moves first and into the 3rd space
        players = ['A']
        turns = [('A', 6), ('A', 6), ('A', 3)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['3', 'R'])

    def test13(self):
        # tests to see if token q moves into the 4th space since it's further away from the end
        players = ['A']
        turns = [('A', 6), ('A', 6), ('A', 3), ('A', 4)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['3', '4'])

    def test14(self):
        # tests to see if token p moves into the fourth space to set up pieces moving together
        players = ['A']
        turns = [('A', 6), ('A', 6), ('A', 3), ('A', 4), ('A', 1)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['4', '4'])

    def test15(self):
        # tests to see if token p and q move in unison after stacking on each other
        players = ['A']
        turns = [('A', 6), ('A', 6), ('A', 3), ('A', 4), ('A', 1), ('A', 5)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['9', '9'])

    def test16(self):
        # tests to see to get token p enters the safe zone
        players = ['A']
        turns = [('A', 6), ('A', 6), ('A', 3), ('A', 4), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['A3', '49'])

    def test17(self):
        # tests to see to get token p enters the safe zone and hits the end after rolling perfect end even though token q if further
        players = ['A']
        turns = [('A', 6), ('A', 6), ('A', 3), ('A', 4), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 4)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['E', '49'])

    def test18(self):
        # tests to see to get token p finishes, and token q gets stacked back after overshooting the E space
        players = ['A']
        turns = [('A', 6), ('A', 6), ('A', 3), ('A', 4), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 4), ('A', 5), ('A', 5)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['E', 'A5'])

    def test19(self):
        # tests to see to get token p and q stack in safe zone and finish together
        players = ['A']
        turns = [('A', 6), ('A', 6), ('A', 3), ('A', 4), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 3), ('A', 4)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['E', 'E'])

    def test20(self):
        # tests to see to get token p and q stack in safe zone, bounce back together after overshooting the E space
        players = ['A']
        turns = [('A', 6), ('A', 6), ('A', 3), ('A', 4), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 3), ('A', 5)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['A6', 'A6'])

    def test21(self):
        # tests to see to get token p and q stack in safe zone, bounce back together after overshooting the E space, and then finish together
        players = ['A']
        turns = [('A', 6), ('A', 6), ('A', 3), ('A', 4), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 3), ('A', 5), ('A', 1)]
        game = LudoGame()
        current_tokens_space = game.play_game(players, turns)
        self.assertEqual(current_tokens_space, ['E', 'E'])


if __name__ == '__main__':    
  unittest.main()