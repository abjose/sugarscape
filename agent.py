
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
        self.move_self(r, c)

        # sugar endowment
        self.sugar = 5
        # metabolism
        self.metabolism = 1
        # vision
        self.vision = 3
        
    def move_self(self, r, c):
        # move from current position to desired position
        #if self.name in self.env.field[self.r][self.c].agents:
        #    self.env.field[self.r][self.c].agents.remove(self.name)
        #self.env.field[r][c].agents.append(self.name)
        #self.r, self.c = r, c
        pass

    def tick(self):
        pass
    
    def get_color(self):
        pass


if __name__=='__main__':
    a = Agent(1,1,1,1)
    b = Agent(1,1,1,1)
    b = Agent(1,1,1,1)
    b = Agent(1,1,1,1)
    b = Agent(1,1,1,1)

    print agent_count
