''' Implement an AI to play tetris '''
from random import Random
from te_settings import Direction

# global constants:
maxRow = 20
maxColumn = 10

heightWeight = - 0.51006
scoreWeight = 0.760666
holesWeight = - 0.35663
bumpinessWeight = - 0.184483

class AutoPlayer():
    ''' A very simple dumb AutoPlayer controller '''
    def __init__(self, controller):
        self.controller = controller
        self.rand = Random()

    def next_move(self, gamestate):
        ''' next_move() is called by the game, once per move.
            gamestate supplies access to all the state needed to autoplay the game.'''
        # self.random_next_move(gamestate)
   
        position, angle = self.cloned_game(gamestate)
    
        x, _ = gamestate.get_falling_block_position()
        r = gamestate.get_falling_block_angle()

        self.real_move(gamestate, x, r, position, angle)

        
    def random_next_move(self, gamestate):
        ''' make a random move and a random rotation.  Not the best strategy!
            but I use it to test the gamestate functions '''
        rnd = self.rand.randint(-1, 1)
        if rnd == -1:
            direction = Direction.LEFT
        elif rnd == 1:
            direction = Direction.RIGHT
        if rnd != 0:
            gamestate.move(direction)
        """     print("mov: " + str(direction)) #get current movement
        else:
            print("mov: 0 ") """

        rnd = self.rand.randint(-1, 1)
        if rnd == -1:
            direction = Direction.LEFT
        elif rnd == 1:
            direction = Direction.RIGHT
        if rnd != 0:
            gamestate.rotate(direction)
        """     print("rot: " + str(direction)) #get current rotation  
        else:
            print("rot: 0") """

        # print single block    
        """ gamestate.print_block_tiles() """
        # print type
        """ blockType = gamestate.get_falling_block_type()
        print (blockType) """
        # get a whole overview
        """ print ("new frame")
        gamestate.print_tiles() """
        # print the tiles
        """ tilescopy = gamestate.get_tiles()
        print(tilescopy) """
        # print the score
        """ score = gamestate.get_score()
        print(score) """ 
        #print the position
        #the position is the top left of the boundbox 
        """ pos = gamestate.get_falling_block_position()
        print(pos) """ 
        #print the angle
        """ ang = gamestate.get_falling_block_angle()
        print(ang) """

    def cloned_game(self, gamestate):
        """ make 40 copies of clones """
        _max_score = 0
        for pos in range (0,10): # 10 columns here --- 9 movements
            for rot in range (0,4): # 4 states of rotation ---3 rotations
                testgs = gamestate.clone(True)
                score = self.try_move(testgs, pos, rot)
                if score > _max_score:
                    _max_score = score
                    position = pos
                    angle = rot
        print (score)
        return position, angle


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
            gamestate.rotate(Direction.RIGHT) # clockwised 
        elif angle > target_rot:
            gamestate.rotate(Direction.LEFT) # anti-clockwised
        
        #here is to update the cloned game (NOT in real game)
        is_land = gamestate.update()
        if is_land:
            return self.score_position(gamestate)
        return self.try_move(gamestate,target_pos,target_rot) # recursion until landed 

    def real_move(self, gamestate, pos, rot, position, angle):
        if pos < position:
            gamestate.move(Direction.RIGHT)
        elif pos > position:
            gamestate.move(Direction.LEFT)
        if rot < angle:
            gamestate.rotate(Direction.RIGHT) # clockwised 
        elif rot > angle:
            gamestate.rotate(Direction.LEFT) # anti-clockwised 

    def score_position(self, gamestate):
        """ here is the function to get the score for every cloned gamestate
        
            we consider three perspectives:
            * height
            * how many holes
            * Variance (not now)
        """ 
        # the simplest way:
        # _score = gamestate.get_score()

        # more complex way:
        gamescore = gamestate.get_score()
        aggregate = self.get_aggregate_height(gamestate)
        bumpiness = self.get_bumpiness(gamestate)
        holes = self.get_holes(gamestate)

        score = heightWeight * aggregate + scoreWeight * gamescore + bumpinessWeight * bumpiness + holesWeight * holes
        return score    

    def get_aggregate_height(self, gamestate):
        total = 0
        for c in range (0, maxColumn):
            _columnHeight = self.get_column_height(gamestate,c)
            total = total + _columnHeight
        # print(total)
        return total
    
    def get_bumpiness(self, gamestate):
        total = 0
        for c in range (0, maxColumn - 1):
            _columnHeight1 = self.get_column_height(gamestate, c)
            _columnHeight2 = self.get_column_height(gamestate, c+1)
            _bumpiness = abs(_columnHeight1 - + _columnHeight2)
            total = total + _bumpiness
        # print(total)
        return total

    def get_column_height(self, gamestate, column):
        """ the helper function of get_aggregate and bumpness """
        _tilescopy = gamestate.get_tiles()
        count = 0
        for r in range (0, maxRow):
            if _tilescopy[r][column] != 0:
                count = count + 1
        columnHeight = count
        # print(columnHeight)
        return columnHeight
    

    def get_holes(self, gamestate):
        _tilescopy = gamestate.get_tiles()
        count = 0        
        for c in range (0, maxColumn):
            hole = False
            for r in range (0, maxRow):
                if (_tilescopy[r][c] != 0):
                    hole = True
                elif (_tilescopy[r][c] == 0 and hole):
                    count = count + 1
        # print (count)            
        return count
    
    def is_line(self, tilescopy):
        pass

    def convert_into_num(self, gamestate):
        """ the helper funtion of is_line """
        _tilescopy = gamestate.get_tiles()
        for r in range (0, maxRow):
            for c in range (0, maxColumn):
                pass
                
                        


                

        

        
                    


        
