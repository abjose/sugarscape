
"""
Agents for the sugarscape.
"""

import numpy as np

# make lots of agents, each with more abilities? Or just make it 
# very easy to disable abilities?

# for making UIDs...sorta dumb, but simpler than an AgentFactory class.
agent_count = 0

class Agent:

    def __init__(self, environment, r, c):
        # get name (hex(agent_count)[2:]) and increment global count
        global agent_count
        self.name = hex(agent_count)[2:]
        agent_count += 1

        # environment to inhabit
        self.env = environment
        self.r, self.c = r, c
        # place self in environment
        self.move(r, c)

        # sugar endowment
        self.sugar = np.random.randint(5,26)
        # metabolism
        self.sugar_metabolism = np.random.randint(1,5)
        # vision
        self.vision = np.random.randint(1,7)
        
    def move(self, r, c):
        # only move if target is empty
        if self.env.field[r, c] != "":
            print "Trying to move to occupied cell, aborting."
            return
        # otherwise move from current position to desired position
        self.env.field[self.r, self.c] = ""
        self.env.field[r, c] = self.name
        self.r, self.c = r, c

    def eat(self, ):
        # take sugar at given spot and add to own sugar score
        self.sugar += self.env.sugar[self.r,self.c,0]
        self.env.sugar[self.r,self.c,0] = 0

    def live(self, ):
        # update attributes
        self.sugar -= self.sugar_metabolism
        if self.sugar <= 0:
            print 'WOE IS ME!!'
            # remove self from simulation
            self.env.kill_agent(self)

    def greedy_strategy(self, ):
        # find best spot
        # TODO: modify s.t. if many good spots, go to closest
        best_sugar = -1
        best_spot = None
        for r,c in self.env.get_neighborhood(self.r, self.c, self.vision):
            s = self.env.sugar[r,c,0]
            if s > best_sugar:
                best_sugar = s
                best_spot = r,c

        # move there and eat sugar
        self.move(*best_spot)
        self.eat()
        

    def tick(self):
        self.greedy_strategy()
        self.live()
    
    def get_color(self):
        pass


if __name__=='__main__':
    a = Agent(1,1,1)
    b = Agent(1,1,1)
    b = Agent(1,1,1)
    b = Agent(1,1,1)
    b = Agent(1,1,1)

    print agent_count
