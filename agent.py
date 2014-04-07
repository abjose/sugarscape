
"""
Agents for the sugarscape.
"""

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
        self.sugar = 5
        # metabolism
        self.metabolism = 1
        # vision
        self.vision = 3
        
    def move(self, r, c):
        # only move if target is empty
        if self.env.field[r, c] != "":
            print "Trying to move to occupied cell, aborting."
            return
        # otherwise move from current position to desired position
        if self.name == self.env.field[self.r, self.c]:
            self.env.field[self.r][self.c] = ""
        self.env.field[r, c] = self.name
        self.r, self.c = r, c

    def eat(self, r, c):
        # take sugar at given spot and add to own sugar score
        self.sugar += self.env.sugar[r,c]
        self.env.sugar[r,c] = 0

    def live(self, ):
        # update attributes...
        pass

    def greedy_strategy(self, ):
        # find best spot
        best_sugar = -1
        best_spot = None
        for r,c in self.env.get_neighborhood(self.r, self.c, self.vision):
            s = self.env.sugar[r,c,0]
            if s > best_sugar:
                best_sugar = s
                best_spot = r,c

        # move there and eat sugar
        self.move(*best_spot)
        self.eat(*best_spot)
        

    def tick(self):
        self.greedy_strategy()
    
    def get_color(self):
        pass


if __name__=='__main__':
    a = Agent(1,1,1)
    b = Agent(1,1,1)
    b = Agent(1,1,1)
    b = Agent(1,1,1)
    b = Agent(1,1,1)

    print agent_count
