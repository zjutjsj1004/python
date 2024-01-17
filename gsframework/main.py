import yaml
from tasks.BaseTask import BaseTask
from tasks.Task1 import Task1
from tasks.Task2 import Task2
from tasks.Task3 import Task3

class SimpleFramework:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def run_tasks(self):
        for task in self.tasks:
            if not task.pre_check():
                break

            if not task.exec():
                print(f"Task execution failed for: {task.command}. Stopping further execution.")
                break

            if not task.post_check():
                print(f"Post-check failed for: {task.command}. Stopping further execution.")
                break

            print("Task completed successfully.")

def load_config(file_path="config.yaml"):
    try:
        with open(file_path, "r") as file:
            config_dict = yaml.safe_load(file)
        return config_dict
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML in configuration file: {e}")

def load_and_add_tasks1(framework, config_dict):
    task_list = config_dict.get("task_list", [])
    for task_name in task_list:
        try:
            # Dynamically import the task module
            task_module = __import__(task_name, globals(), locals(), [task_name], 0)

            # Get the task class directly (assuming the class name matches the file name)
            task_class = getattr(task_module, task_name.capitalize(), None)

            if task_class:
                # Create an instance of the task and add it to the framework
                task_instance = task_class(f"python3 {task_name}.py")
                framework.add_task(task_instance)
            else:
                print(f"Error: Task class not found in module {task_name}.")
        except (ImportError, AttributeError) as e:
            print(f"Error loading task {task_name}: {e}")

def load_and_add_tasks(framework, config_dict):
    task_list = config_dict.get("task_list", [])
    for task_name in task_list:
        try:
            # Dynamically import the task module
            task_module = globals().get(task_name)
            print(task_module)
            if task_module:
                # Get the task class directly (assuming the class name matches the file name)
                    task_instance = globals()[task_name](config_dict)

                    # Create an instance of the task and add it to the framework
                    framework.add_task(task_instance)

            else:
                print(f"Error: Task module {task_name} not found.")
        except (ImportError, AttributeError) as e:
            print(f"Error loading task {task_name}: {e}")


if __name__ == "__main__":
    # 读取配置文件
    config_dict = load_config()

    if config_dict:
        # 创建框架实例
        framework = SimpleFramework()

        # 根据配置添加任务并运行
        load_and_add_tasks(framework, config_dict)

        # 运行任务
        framework.run_tasks()
