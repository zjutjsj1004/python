from BaseTask import BaseTask
import os

class Task3(BaseTask):
    def __init__(self):
        super(Task3, self).__init__()
        
    def pre_check(self):
        # Implement pre-check logic for Task3
        if not os.path.exists("output2.txt"):
            print("Error: Output file 'output2.txt' not found for Task3.")
            return False
        return True

    def exec(self):
        # Implement execution logic for Task3
        print("Executing Task3")
        return True

    def post_check(self):
        # Implement post-check logic for Task3
        print("Post-check for Task3")
        return True
