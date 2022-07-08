import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        """Called at the start of every Test, resets the Rolls array"""
        self.game = BowlingGame.BowlingGame()

    def tearDown(self):
        """called to the end of every test,  prints rolls[] values to output"""
        print(self.game.rolls)
        print("result= " + str(self.game.score()) + "\n")

    def test_GutterGame(self):
        """simulate a Game with 100% gutter balls"""
        for i in range(0, 20):
            self.game.roll(0)
        assert self.game.score()==0

    def testAllOnes(self):
        """simulate a game with each ball dropping one pin"""
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)

    def testOneSpare(self):
        """simulates a game with a Spare in the first frame and"""
        self.game.roll(5)
        self.assertEqual(self.game.score(), 5)
        self.game.roll(5)
        self.assertEqual(self.game.score(), 10)
        self.game.roll(3)
        self.assertEqual(self.game.score(), 16)
        self.rollMany(0,17)
        assert self.game.score()==16

    def testOneStrike(self):
        """simulates a game with a Strike in first round"""
        self.game.roll(10)
        self.assertEqual(self.game.score(), 10)
        self.game.roll(4)
        self.assertEqual(self.game.score(), 18)
        self.game.roll(3)
        self.rollMany(0,16)
        assert  self.game.score()==24

    def testPerfectGame(self):
        """Simulates a Strike for each ball roll of a game"""
        self.rollMany(10,12)
        self.assertEqual(self.game.score(), 300)

    def testALLSpares(self):
        """Simulates a Game where every ball roll knocks down 5 pins, resulting in a Spare for each frame"""
        self.rollMany(5,21)
        self.assertEqual(self.game.score(), 150)
        assert self.game.score()==150
        
    def rollMany(self, pins, roll):
        """simulate multiple ball rolls with specified number of pins dropped"""
        for i in range(roll):
            self.game.roll(pins)

    def testTooFewPins(self):
        """tests input below expected range"""
        self.rollMany(-1,20)
        assert self.game.score()==0
    
    def testTooManyPins(self):
        """tests input above expected range"""
        self.rollMany(11,22)
        assert self.game.score()==300

    print(setUp.__doc__)
    help(BowlingGame)

if __name__ == '__main__':
    """run Unit Tests"""
    print('running tests')
    unittest.main()
    