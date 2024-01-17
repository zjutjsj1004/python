from abc import ABC, abstractmethod
from utils.Utils import Utils

class BaseTask(ABC):
    def __init__(self,config_dict):
        self.config = config_dict 
        self.status = Utils.TASK_INIT
        pass
    
    def pre_check(self):
        pass

    def exec(self):
        pass

    def post_check(self):
        pass

    def update_status(self, task_status):
        self.status = task_status

    def run(self):
        if self.pre_check():
            self.exec()

            if not self.post_check():
                self.update_status(Utils.TASK_EXEC_FAIL)
                return
            else:
                self.update_status(Utils.TASK_SUCCESS)
        else:
            self.update_status(Utils.TASK_CHECK_FAIL)
        return
