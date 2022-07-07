class BowlingGame:
    '''A Class to Run the Back-end of a Bowling game Scoring System
    
    Attributes
    ----------
    rolls : array int
        an Array to store the number of pins dropped for each ball. 
    '''

    def __init__(self):
        """Constructor, creates new array for each game"""
        self.rolls=[]

    def roll(self,pins):
        """Simulates a Ball roll in game.
        
        Control to ensure pins downed is within valid range"""
        if pins > 10:
            pins = 10
        elif pins < 0:
            pins = 0

        self.rolls.append(pins)

    def score(self):
        """Manages Game scoring.

        goes through rollIndex Array and calculates score of 
        a complete game. 
        Determines if Frame is Strike, Spare or Ordinary to
        add Scores accordingly.
        """
        result = 0
        rollIndex=0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strike_score(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
                rollIndex +=2
        return result

    #return boolean is strike?
    def isStrike(self, rollIndex):
        """Checks if current rolls[] index value equals 10 pins in the first ball of current frame == STRIKE"""
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        """Checks if sum of current + next rolls[] index values equal 10 pins for both balls of current frame == SPARE"""
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10

    def strike_score(self,rollIndex):
        """Returns 10 + score for next 2 balls"""
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        """Returns 10 + Score for first ball of next frame"""
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        """returns Score for both balls in current Frame"""
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
