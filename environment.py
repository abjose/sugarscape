
"""
Simulated environment.
"""

import numpy as np
from random import shuffle

from agent import Agent



"""
TODO
- ADD SOME UTILITY GRAPHING FUNCTIONALITY
- COULD START WRITING PAPER - TALK ABOUT CURRENT STATE AS BASICALLY 
  WITHOUT MORAL CHOICE
- MAKE SURE ITS REALLY EASY TO LOAD UP THIS CURRENT STATE / I.E. MAKE THIS A 
  KIND OF AGENT THAT CAN JUST BE CHOSEN AND WILL BEHAVE LIKE THIS...
- add age....other stuff from sugarscape page
- make rules s.t. can even modify stuff like "eat sugar..."
-- have utility just be another rule?? but like a 'required' rule?
- modify sugar caps to have some kind of distribution...
- maybe have environment construct proper viewer...have get_viewer?
- Make 'sight' and 'stride' different variables? So can see/communicate with 
  stuff far away maybe, but maybe only move a little

"""



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
        # set current sugar
        self.sugar[:,:,0] = 5#np.random.randint(0, 25, (s, s))
        # set grow-back rate
        self.sugar[:,:,1] = 0#np.random.randint(1, 5, (s, s))
        # set sugar max
        self.sugar[:,:,2] = 5 #500
        # add sugar growback interval? would need counter and actual interval...

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

    def kill_agent(self, agent):
        # remove an agent from the simulation
        # remove from field
        self.field[agent.r, agent.c] = ""
        # remove dict entry
        del self.agents[agent.name]

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

        # add in agent dots
        for name,agent in self.agents.items():
            r, c = agent.r, agent.c
            m[r,c,0] = 0
            m[r,c,1] = 255
            m[r,c,2] = 0
        
        return m

    def get_viewer(self, pixel_size):
        return Viewer(pixel_size,pixel_size, 
                      self.side*pixel_size,self.side*pixel_size)


if __name__=='__main__':
    
    from viewer import Viewer

    e = Environment(250)
    v = e.get_viewer(1)
    
    for _ in range(500):
        e.add_agent()

    t = 0
    while True:
        print 'tick', t
        t += 1
        e.tick()
        v.display(e.get_color_matrix())
        #raw_input()
    
