
"""
Simulated environment.
"""

import numpy as np
from random import shuffle

from agent import Agent


class Environment:
    
    def __init__(self, s):
        # use yaml or something to load configuration?
        # size
        self.side = s
        
        # for 'placing' agents
        self.field = np.chararray((s, s), itemsize=5)
        # a dictionary for associating strings with agent objects
        self.agents = dict()

        # keep track of resources as vectors of (current, rate, max)
        # consider enclosing this in a function
        self.sugar = np.zeros((s, s, 3))
        # set current
        self.sugar[:,:,0] = 0#np.random.randint(0, 25, (s, s))
        # set rate
        self.sugar[:,:,1] = np.random.randint(1, 5, (s, s))
        # set max
        self.sugar[:,:,2] = 500

    def tick_resources(self, ):
        # maybe keep a list of resources to make shorter if have lots?
        self.sugar[:,:,0] = np.minimum(self.sugar[:,:,0]+self.sugar[:,:,1],
                                       self.sugar[:,:,2])

    def tick(self, ):
        # tick everything
        self.tick_resources()
        # update agents in random order
        agents = [agent for name,agent in self.agents.items()]
        shuffle(agents)
        for agent in agents:
            agent.tick()

    def add_agent(self, ):
        # add an agent to a random location?
        r, c = np.random.randint(0, self.side, 2)
        a = Agent(self, r, c)
        self.agents[a.name] = a
        # VERIFY WON'T GET MODIFIED...

    def get_neighborhood(self, r, c, d): #, include_self=True):
        # get a distance-d Von Neumann neighborhood around (r,c)
        # more efficient way to do this?
        hood = []
        for i in range(-d,d+1):
            for j in range(-d,d+1):
                if abs(i)+abs(j) <= d and not (i == 0 and j == 0):
                    # wrap around for torus
                    hood.append(((r+i)%self.side, (c+j)%self.side))
        # shuffle so not always looking at same place first
        shuffle(hood)
        return hood

    def get_color_matrix(self):
        # return numpy matrix representation of colors of field
        m = np.ones((self.side, self.side, 3), dtype=np.int)
        l = (self.sugar[:,:,0] / self.sugar[:,:,2]) * 255
        # better way to do this?
        m[:,:,0] = l
        m[:,:,1] = l
        m[:,:,2] = l
        #m[:,:,:] = np.dstack([l,l,l]) # much slower...
        return m


if __name__=='__main__':
    
    from viewer import Viewer

    e = Environment(500)
    v = Viewer(1,1, e.side,e.side)
    
    for _ in range(10):
        e.add_agent()

    t = 0
    while True:
        print 'tick', t
        t += 1
        e.tick()
        v.display(e.get_color_matrix())
    
