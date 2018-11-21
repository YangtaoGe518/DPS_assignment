''' Implement an AI to play tetris '''
from random import Random
from te_settings import Direction

class AutoPlayer():
    ''' A very simple dumb AutoPlayer controller '''
    def __init__(self, controller):
        self.controller = controller
        self.rand = Random()

    def next_move(self, gamestate):
        ''' next_move() is called by the game, once per move.
            gamestate supplies access to all the state needed to autoplay the game.'''
        direction = 0
        rotation = 0
        """ we need to do some thing to get the best direction and rotation
            replace here with some functions (algorithm)  """

        gamestate.move(direction)  # we need to figure out the best direction
        gamestate.move(rotation)   # we need to figure out the best rotation

    def random_next_move(self, gamestate):
        ''' make a random move and a random rotation.  Not the best strategy! '''
        rnd = self.rand.randint(-1, 1)
        if rnd == -1:
            direction = Direction.LEFT
        elif rnd == 1:
            direction = Direction.RIGHT
        if rnd != 0:
            gamestate.move(direction)
        rnd = self.rand.randint(-1, 1)
        if rnd == -1:
            direction = Direction.LEFT
        elif rnd == 1:
            direction = Direction.RIGHT
        if rnd != 0:
            gamestate.rotate(direction)
        gamestate.print_block_tiles()
        blockType = gamestate.get_falling_block_type()
        print (blockType)
        # get a whole overview
        """ print ("new frame")
        gamestate.print_tiles() """
    
    def make_clones(self, gamestate):
        for pos in range (0,10): # 10 columns here --- 9 movements
            for rot in range (0,4): # 4 states of rotation ---3 rotations
                testgs = gamestate.clone()
                score = self.try_move(testgs, pos, rot)

                """ here need pass all the parameters that you need in the test
                    gamestate e.g. score, position rotation, all of them make a
                    cloned game i.e. have the same values in all parameter
                """
         
    def try_move(self, gamestate, target_pos, target_rot):
        """ trymove function is where we test different situations 
            in other words, it is not actually moving 
        """
        # here we obtain a tuple contain the current block position and angle
        x,_ = gamestate.get_falling_block_position()
        angle = gamestate.get_falling_block_angle()
        #here is a movement of position to target position
        if x < target_pos:
            gamestate.move(Direction.RIGHT)
        elif x > target_pos:
            gamestate.move(Direction.LEFT)

        #here is a rotation of angle to target rotation
        if angle < target_rot:
            gamestate.move(Direction.RIGHT) # clockwised 
        elif angle > target_rot:
            gamestate.move(Direction) # anti-clockwised
        
        #here is to update the cloned game (NOT in real game)
        is_land = gamestate.update()
        if is_land:
            return self.score_position(gamestate)
        return self.try_move(gamestate,target_pos,target_rot) # recursion until landed 

    def score_position(self, gamestate):
        pass
        

        
                    


        
