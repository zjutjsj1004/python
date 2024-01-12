from BaseTask import BaseTask
import os

class Task1(BaseTask):
    def __init__(self):
        super(Task1, self).__init__()

    def pre_check(self):
        # Implement pre-check logic for Task1
        return True

    def exec(self):
        # Implement execution logic for Task1
        print("Executing Task1")
        return True

    def post_check(self):
        # Implement post-check logic for Task1
        print("Post-check for Task1")
        return True
