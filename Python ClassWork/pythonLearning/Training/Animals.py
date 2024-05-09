class Animals:
    def __init__(self, name, legs, tail):
        self.__name = name
        self.__legs = legs 
        self.__tail = tail
        
    @property
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def set_name(self, value):
        self.__name = value
  
    @property
    def get_legs(self):
        return self.__legs 
    
    @get_legs.setter
    def set_legs(self, value):
        self.__legs = value
        
    @property
    def get_tail(self):
        return self.__tail
    
    @get_tail.setter
    def set_tail(self, value):
        self.__tail = value

    def displayA(self):
        return self.get_name, self.get_tail, self.__legs


# ani = Animals('Tiger', 4, 1)
# print(ani.displayA())
