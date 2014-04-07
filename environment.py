
"""
Simulated environment.
"""

import numpy as np

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
        # consider enclosing this in a function?
        self.sugar = np.zeros((s, s, 3))
        # set current
        self.sugar[:,:,0] = 0#np.random.randint(0, 25, (s, s))
        # set rate
        self.sugar[:,:,1] = np.random.randint(1, 5, (s, s))
        # set max
        self.sugar[:,:,2] = 500

    def tick_resources(self, ):
        # maybe keep a list of resources to shorter if have lots?
        self.sugar[:,:,0] = np.minimum(self.sugar[:,:,0]+self.sugar[:,:,1],
                                       self.sugar[:,:,2])

    def tick(self, ):
        # tick everything
        self.tick_resources()

    def add_agent(self, ):
        # UPDATE
        # add an agent to a random location?
        #r, c = np.random.randint(0, self.side, 2)
        #a = Agent(self, uuid1().bytes, r, c)
        pass

    def get_neighborhood(self, r, c, d, include_self=True):
        # get a d-diameter Von Neumann neighborhood, return as list of Patches
        # first constrain bounds
        pass

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
    
    t = 0

    while True:
        print 'tick', t
        t += 1
        e.tick()
        v.display(e.get_color_matrix())

