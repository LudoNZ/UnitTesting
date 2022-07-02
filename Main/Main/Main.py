import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    print("testing here...")

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def test_GutterGame(self):
        for i in range(0, 20):
            self.game.roll(0)
        assert self.game.score()==0

    def testAllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)

    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score()==16

    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        assert  self.game.score()==24

    def testPerfectGame(self):
        self.rollMany(10,12)
        assert self.game.score()==300

    def testOneSpare(self):
        self.rollMany(5,21)
        assert self.game.score()==150
        
    def rollMany(self, pins, roll):
        for i in range(roll):
            self.game.roll(pins)

if __name__ == '__main__':
    print('running tests')
    unittest.main()
        