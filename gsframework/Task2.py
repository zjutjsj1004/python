from BaseTask import BaseTask
import os

class Task2(BaseTask):
    def __init__(self):
        super(Task2, self).__init__()
        
    def pre_check(self):
        # Implement pre-check logic for Task2
        if not os.path.exists("output1.txt"):
            print("Error: Output file 'output1.txt' not found for Task2.")
            return False
        return True

    def exec(self):
        # Implement execution logic for Task2
        print("Executing Task2")
        return True

    def post_check(self):
        # Implement post-check logic for Task2
        print("Post-check for Task2")
        return True
