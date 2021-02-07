import random

class Object:
    def __repr__(self):
        return '<%s>' % getattr(self,'__name__',self.__class__.__name__)
   

class Agent(Object):
    def __init__(self):
        def program(percept):abstract
        self.program=program

loc_A,loc_B,loc_C,loc_D='A','B','C','D'
        
class vaccumEnvironment():

    def __init__(self):
        self.status={ loc_A:random.choice(['Clean','Dirty']),loc_B:random.choice(['Clean','Dirty']),loc_C:random.choice(['Clean','Dirty']),loc_D:random.choice(['Clean','Dirty'])
                      }
        
    def add_object(self,object,location=None):
        object.location=location or self.default_location(object)

    def default_location(self,object):
        return random.choice([loc_A,loc_B,loc_C,loc_D])

    def percept(self,agent):
        return (agent.location,self.status[agent.location])

    def execute_action(self,agent,action):
        if action=='Right' : agent.location=loc_B
        elif action=='Down': agent.location=loc_C
        elif action=='Left': agent.location=loc_A
        elif action=='Down': agent.location=loc_D
        elif action=='Up': agent.location=loc_A
        elif action=='Right': agent.location=loc_D
        elif action=='Left': agent.location=loc_C
        elif action=='Up': agent.location=loc_B
        elif action=='Suck':
           # if self.status[agent.location]=='Dirty',
            self.status[agent.location]='Clean'
      
class tableDrivenAgent(Agent):

    def __init__(self,table):
        Agent.__init__(self)
        percepts=[]

        def program(percept):
            percepts.append(percept)
            print(percepts)
            action=table.get(tuple(percepts))
            print('Agent perceives ', percept, ' and does ', action)
            return action

        self.program=program



def tableDrivenVaccumAgent():
    table = {
              ((loc_A,'Clean'),):'Right',
              ((loc_A,'Dirty'),):'Suck',
              ((loc_B,'Clean'),):'Left',
              ((loc_B,'Dirty'),):'Suck',
              ((loc_A,'Clean'),):'Down',
               ((loc_C,'Clean'),):'Right',
              ((loc_C,'Dirty'),):'Suck',
              ((loc_D,'Clean'),):'Left',
              ((loc_D,'Dirty'),):'Suck',
              ((loc_C,'Clean'),):'Up',
               ((loc_D,'Clean'),):'Up',
              (('A', 'Clean'), ('C', 'Clean')):'Right',
              (('C', 'Clean'), ('A', 'Clean')):'Right',
              (('A', 'Clean'), ('C', 'Clean')):'Up',
              (('C', 'Clean'), ('A', 'Clean')):'Down',
              (('C', 'Clean'), ('A', 'Dirty')):'Suck',
              (('B', 'Clean'), ('A', 'Dirty')):'Suck',
              (('D', 'Clean'), ('A', 'Dirty')):'Suck',
              (('A', 'Clean'), ('A', 'Dirty')):'Suck',
              (('C', 'Clean'), ('B', 'Dirty')):'Suck',
              (('B', 'Clean'), ('B', 'Dirty')):'Suck',
              (('D', 'Clean'), ('B', 'Dirty')):'Suck',
              (('A', 'Clean'), ('B', 'Dirty')):'Suck',
              (('C', 'Clean'), ('C', 'Dirty')):'Suck',
              (('B', 'Clean'), ('C', 'Dirty')):'Suck',
              (('D', 'Clean'), ('C', 'Dirty')):'Suck',
              (('A', 'Clean'), ('C', 'Dirty')):'Suck',
              (('C', 'Clean'), ('D', 'Dirty')):'Suck',
              (('B', 'Clean'), ('D', 'Dirty')):'Suck',
              (('D', 'Clean'), ('D', 'Dirty')):'Suck',
              (('A', 'Clean'), ('D', 'Dirty')):'Suck',
              (('D', 'Clean'), ('A', 'Clean')):'Right',
              (('D', 'Clean'), ('A', 'Clean')):'Down',
              (('C', 'Clean'), ('A', 'Clean')):'Right',
              (('C', 'Clean'), ('A', 'Clean')):'Down',
              (('B', 'Clean'), ('A', 'Clean')):'Right',
              (('B', 'Clean'), ('A', 'Clean')):'Down',
              ((loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Clean'), (loc_B, 'Clean')): 'Left',
              ((loc_A, 'Clean'), (loc_B, 'Clean')): 'Down',
              ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
              ((loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
               ((loc_C, 'Clean'), (loc_C, 'Clean')): 'Right',
              ((loc_C, 'Clean'), (loc_D, 'Clean')): 'Left',
              ((loc_C, 'Clean'), (loc_D, 'Clean')): 'Up',
              ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
              ((loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
              
              ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Dirty'), (loc_B, 'Clean')): 'Left',
              ((loc_A, 'Dirty'), (loc_B, 'Dirty')): 'Right',
              ((loc_A, 'Dirty'), (loc_A, 'Dirty')): 'Suck',
              ((loc_C, 'Dirty'), (loc_C, 'Clean')): 'Right',
              ((loc_C, 'Dirty'), (loc_D, 'Clean')): 'Left',
              ((loc_C, 'Dirty'), (loc_D, 'Dirty')): 'Right',
              ((loc_C, 'Dirty'), (loc_C, 'Dirty')): 'Suck',

              ((loc_B, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_B, 'Clean'), (loc_B, 'Clean')): 'Left',
              ((loc_B, 'Clean'), (loc_B, 'Dirty')): 'Right',
              ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',
              ((loc_D, 'Clean'), (loc_C, 'Clean')): 'Right',
              ((loc_D, 'Clean'), (loc_D, 'Clean')): 'Left',
              ((loc_D, 'Clean'), (loc_D, 'Dirty')): 'Right',
              ((loc_D, 'Clean'), (loc_C, 'Dirty')): 'Suck',
              
              ((loc_B, 'Dirty'), (loc_A, 'Clean')): 'Right',
              ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
              ((loc_B, 'Dirty'), (loc_B, 'Dirty')): 'Right',
              ((loc_B, 'Dirty'), (loc_A, 'Dirty')): 'Suck',
              ((loc_D, 'Dirty'), (loc_C, 'Clean')): 'Right',
              ((loc_D, 'Dirty'), (loc_D, 'Clean')): 'Left',
              ((loc_D, 'Dirty'), (loc_D, 'Dirty')): 'Right',
              ((loc_D, 'Dirty'), (loc_C, 'Dirty')): 'Suck',


              
              ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
              ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Clean')): 'Down',
             ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
               ((loc_B, 'Clean'), (loc_B, 'Clean'), (loc_B, 'Clean')): 'Left',
              ((loc_B, 'Clean'), (loc_B, 'Clean'), (loc_B, 'Dirty')): 'Suck',
              ((loc_B, 'Clean'), (loc_B, 'Clean'), (loc_B, 'Clean')): 'Down',
               ((loc_C, 'Clean'), (loc_C, 'Clean'), (loc_C, 'Clean')): 'Right',
              ((loc_C, 'Clean'), (loc_C, 'Clean'), (loc_C, 'Dirty')): 'Suck',
              ((loc_C, 'Clean'), (loc_C, 'Clean'), (loc_C, 'Clean')): 'Up',
              ((loc_D, 'Clean'), (loc_D, 'Clean'), (loc_D, 'Clean')): 'Left',
              ((loc_D, 'Clean'), (loc_D, 'Clean'), (loc_D, 'Dirty')): 'Suck',
              ((loc_D, 'Clean'), (loc_D, 'Clean'), (loc_D, 'Clean')): 'Up',

              ((loc_A, 'Clean'), (loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
              ((loc_A, 'Clean'), (loc_A, 'Dirty'), (loc_A, 'Clean')): 'Down',
             ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
               ((loc_B, 'Clean'), (loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
              ((loc_B, 'Clean'), (loc_B, 'Clean'), (loc_B, 'Dirty')): 'Suck',
              ((loc_B, 'Clean'), (loc_B, 'Dirty'), (loc_B, 'Clean')): 'Down',
               ((loc_C, 'Clean'), (loc_C, 'Dirty'), (loc_C, 'Clean')): 'Right',
              ((loc_C, 'Clean'), (loc_C, 'Clean'), (loc_C, 'Dirty')): 'Suck',
              ((loc_C, 'Clean'), (loc_C, 'Dirty'), (loc_C, 'Clean')): 'Up',
              ((loc_D, 'Clean'), (loc_D, 'Dirty'), (loc_D, 'Clean')): 'Left',
              ((loc_D, 'Clean'), (loc_D, 'Clean'), (loc_D, 'Dirty')): 'Suck',
              ((loc_D, 'Clean'), (loc_D, 'Dirty'), (loc_D, 'Clean')): 'Up',
              (('D', 'Clean'), ('A', 'Clean'), ('A', 'Clean')): 'Right',
              (('D', 'Clean'), ('A', 'Clean'), ('A', 'Clean')): 'Down',
              (('C', 'Dirty'), ('C', 'Clean'), ('B', 'Clean')): 'Left',
              (('C', 'Dirty'), ('C', 'Clean'), ('B', 'Clean')): 'Down',
              (('D', 'Dirty'), ('D', 'Clean'), ('B', 'Clean')): 'Left',
               (('D', 'Dirty'), ('D', 'Clean'), ('B', 'Clean')): 'Down',
              (('C', 'Dirty'), ('C', 'Clean'), ('A', 'Clean')): 'Right',
              (('C', 'Dirty'), ('C', 'Clean'), ('A', 'Clean')): 'Down',
              (('D', 'Dirty'), ('D', 'Clean'), ('A', 'Dirty')):'Suck',
              (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Dirty')):'Suck',
              (('A', 'Clean'), ('C', 'Clean'), ('B', 'Clean')):'Left',
              (('A', 'Clean'), ('C', 'Clean'), ('B', 'Clean')):'Down',
              (('D', 'Dirty'), ('D', 'Clean'), ('A', 'Clean')):'Right',
              (('D', 'Dirty'), ('D', 'Clean'), ('A', 'Clean')):'Down',
              (('B', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')):'Right',
              (('B', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')):'Down',
              (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Dirty')):'Suck',
              (('B', 'Dirty'), ('B', 'Clean'), ('B', 'Dirty')):'Suck',
              (('B', 'Dirty'), ('B', 'Clean'), ('C', 'Dirty')):'Suck',
              (('B', 'Dirty'), ('B', 'Clean'), ('D', 'Dirty')):'Suck',
              (('A', 'Clean'), ('C', 'Clean'), ('A', 'Clean')):'Right',
              (('A', 'Clean'), ('C', 'Clean'), ('A', 'Clean')):'Down',
              (('A', 'Clean'), ('C', 'Clean'), ('C', 'Clean')):'Right',
              (('A', 'Clean'), ('C', 'Clean'), ('C', 'Clean')):'Up',
              (('A', 'Clean'), ('C', 'Clean'), ('D', 'Clean')):'Left',
              (('A', 'Clean'), ('C', 'Clean'), ('D', 'Clean')):'Up',
              (('A', 'Clean'), ('C', 'Clean'), ('D', 'Dirty')):'Suck',
              (('A', 'Clean'), ('C', 'Clean'), ('C', 'Dirty')):'Suck',
              (('A', 'Clean'), ('C', 'Clean'), ('B', 'Dirty')):'Suck',
              (('A', 'Clean'), ('C', 'Clean'), ('A', 'Dirty')):'Suck',
              (('C', 'Dirty'), ('C', 'Clean'), ('B', 'Dirty')): 'Suck',
              (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Dirty')): 'Suck',
              (('D', 'Dirty'), ('D', 'Clean'), ('B', 'Dirty')): 'Suck',
              (('A', 'Clean'), ('C', 'Dirty'), ('C', 'Clean')): 'Right',
               (('A', 'Clean'), ('C', 'Dirty'), ('C', 'Clean')): 'Up',
              (('B', 'Clean'), ('A', 'Clean'), ('B', 'Clean')): 'Left',
               (('B', 'Clean'), ('A', 'Clean'), ('B', 'Clean')): 'Down',
              (('D', 'Clean'), ('A', 'Clean'), ('C', 'Dirty')): 'Suck',
              (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Clean')): 'Left',
              (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Clean')): 'Down',
              (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Clean')):'Right',
              (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Clean')):'Down',
              (('C', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')):'Right',
              (('C', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')):'Down',
              (('D', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')):'Right',
              (('D', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')):'Down',
              (('C', 'Clean'), ('A', 'Clean'), ('C', 'Clean')):'Right',
              (('C', 'Clean'), ('A', 'Clean'), ('C', 'Clean')):'Up',
              (('D', 'Clean'), ('A', 'Clean'), ('C', 'Clean')):'Right',
              (('D', 'Clean'), ('A', 'Clean'), ('C', 'Clean')):'Up',
              (('A', 'Clean'), ('B', 'Clean'), ('C', 'Clean'), ('D', 'Clean')):'Turn Off',
              (('A', 'Clean'), ('B', 'Clean'), ('D', 'Clean'), ('C', 'Clean')):'Turn Off',
              (('B', 'Clean'), ('A', 'Clean'), ('D', 'Clean'), ('C', 'Clean')):'Turn Off',
              (('B', 'Clean'), ('D', 'Clean'), ('A', 'Clean'), ('C', 'Clean')):'Turn Off',
              (('A', 'Clean'), ('C', 'Clean'), ('B', 'Clean'), ('D', 'Clean')):'Turn Off',
              (('A', 'Clean'), ('D', 'Clean'), ('C', 'Clean'), ('B', 'Clean')):'Turn Off',
              (('B', 'Clean'), ('A', 'Clean'), ('C', 'Clean'), ('D', 'Clean')):'Turn Off',
              (('B', 'Clean'), ('D', 'Clean'), ('C', 'Clean'), ('A', 'Clean')):'Turn Off',
              (('B', 'Clean'), ('A', 'Clean'), ('B', 'Clean'), ('B', 'Clean')):'Left',
              (('B', 'Clean'), ('A', 'Dirty'), ('A', 'Clean'), ('C', 'Dirty')): 'Suck',
              (('D', 'Dirty'), ('D', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')):'Right',
              (('D', 'Dirty'), ('D', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')):'Down',
              (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Clean'), ('A', 'Clean')):'Right',
              (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Clean'), ('A', 'Clean')):'Down',
              (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Dirty'), ('B', 'Clean')): 'Left',
              (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Dirty'), ('B', 'Clean')): 'Down',
              (('D', 'Dirty'), ('D', 'Clean'), ('A', 'Clean'), ('C', 'Clean')):'Right',
              (('D', 'Dirty'), ('D', 'Clean'), ('A', 'Clean'), ('C', 'Clean')):'Up',
              (('C', 'Dirty'), ('C', 'Clean'), ('B', 'Clean'), ('C', 'Clean')):'Right',
               (('C', 'Dirty'), ('C', 'Clean'), ('B', 'Clean'), ('C', 'Clean')):'Up',
              (('A', 'Clean'), ('C', 'Dirty'), ('C', 'Clean'), ('A', 'Clean')):'Right',
              (('A', 'Clean'), ('C', 'Dirty'), ('C', 'Clean'), ('A', 'Clean')):'Down',
              (('C', 'Clean'), ('A', 'Clean'), ('C', 'Clean'), ('C', 'Clean')):'Right',
              (('C', 'Clean'), ('A', 'Clean'), ('C', 'Clean'), ('C', 'Clean')):'Up',
              (('D', 'Dirty'), ('D', 'Clean'), ('A', 'Clean'), ('C', 'Dirty')): 'Suck',
              (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Clean'), ('C', 'Dirty')): 'Suck',
              (('D', 'Clean'), ('A', 'Dirty'), ('A', 'Clean'), ('A', 'Clean')): 'Right',
              (('D', 'Clean'), ('A', 'Dirty'), ('A', 'Clean'), ('A', 'Clean')): 'Down',
              (('B', 'Clean'), ('A', 'Dirty'), ('A', 'Clean'), ('C', 'Clean')): 'Right',
              (('B', 'Clean'), ('A', 'Dirty'), ('A', 'Clean'), ('C', 'Clean')): 'Up',
              (('C', 'Dirty'), ('C', 'Clean'), ('B', 'Dirty'), ('B', 'Clean')):'Left',
              (('C', 'Dirty'), ('C', 'Clean'), ('B', 'Dirty'), ('B', 'Clean')):'Down',
              (('D', 'Clean'), ('A', 'Clean'), ('C', 'Clean'), ('C', 'Clean')): 'Right',
              (('D', 'Clean'), ('A', 'Clean'), ('C', 'Clean'), ('C', 'Clean')): 'Up',
              (('D', 'Clean'), ('A', 'Clean'), ('C', 'Clean'), ('A', 'Clean')): 'Right',
              (('D', 'Clean'), ('A', 'Clean'), ('C', 'Clean'), ('A', 'Clean')): 'Down',
              (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')): 'Right',
              (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Dirty'), ('A', 'Clean')): 'Down',
              (('C', 'Clean'), ('A', 'Clean'), ('C', 'Clean'), ('A', 'Clean')):'Right',
              (('C', 'Clean'), ('A', 'Clean'), ('C', 'Clean'), ('A', 'Clean')):'Down',
              (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Clean'), ('C', 'Dirty')): 'Suck',
              (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Clean'), ('C', 'Clean')): 'Right',
              (('B', 'Dirty'), ('B', 'Clean'), ('A', 'Clean'), ('C', 'Clean')): 'Up',
              (('B', 'Clean'), ('A', 'Clean'), ('B', 'Clean'), ('C', 'Clean')):'Right',
              (('B', 'Clean'), ('A', 'Clean'), ('B', 'Clean'), ('C', 'Clean')):'Up',

             
            }
    print("Table Driven Vaccum Agent\n")
    return tableDrivenAgent(table)
Tagent=tableDrivenVaccumAgent()
env=vaccumEnvironment()
env.add_object(Tagent)
for _ in range(4):
    action=Tagent.program(env.percept(Tagent))
    env.execute_action(Tagent,action)
class reflexVaccumAgent(Agent):
    
    def __init__(self):
        Agent.__init__(self)        

        def program(percept):
            location=percept[0]
            status=percept[1]


            if status=='Dirty': action= 'Suck'
            elif location==loc_A: action= 'Right'
            elif location==loc_B: action= 'Left'
            elif location==loc_B: action= 'Down'
            elif location==loc_A: action= 'Right'
            elif location==loc_C: action= 'Right'
            
            elif location==loc_D: action= 'Left'
            elif location==loc_C: action= 'Up'
            elif location==loc_D: action= 'Down'
           



            percept=(location,status)
            print('Agent perceives ', percept, ' and does ', action)

            return action
        
            
            
        self.program=program
print("\nReflex Vaccum Agent\n")
Tagent=reflexVaccumAgent()
env=vaccumEnvironment()
env.add_object(Tagent)

for _ in range(4):
    action=Tagent.program(env.percept(Tagent))
    env.execute_action(Tagent,action)





        
class modelBasedVaccumAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        
        model={loc_A:None,loc_B:None,loc_C:None,loc_D:None}

        def program(percept):
            location=percept[0]
            status=percept[1]
            
            model[location]=status

            if model[loc_A]==model[loc_B]==model[loc_C]==model[loc_D]: action= 'none'
            elif status=='Dirty': action= 'Suck'
            elif location==loc_A: action= 'Right'
            elif location==loc_B: action= 'Left'
            elif location==loc_B: action= 'Down'
            elif location==loc_A: action= 'Right'
            elif location==loc_C: action= 'Right'
            
            elif location==loc_D: action= 'Left'
            elif location==loc_C: action= 'Up'
            elif location==loc_D: action= 'Down'
            
            

            percept=(location,status)
            print('Agent perceives ', percept, ' and does ', action)

            return action                    
            
        self.program=program


print("\nModel Based Vaccum Agent\n")

Tagent=modelBasedVaccumAgent()
env=vaccumEnvironment()
env.add_object(Tagent)

for _ in range(4):
    action=Tagent.program(env.percept(Tagent))
    env.execute_action(Tagent,action)




