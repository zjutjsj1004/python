from abc import ABC, abstractmethod

class BaseTask(ABC):
    def __init__(self,config_dict):
        self.config = config_dict 
        pass
    
    def pre_check(self):
        pass

    def exec(self):
        pass

    def post_check(self):
        pass
