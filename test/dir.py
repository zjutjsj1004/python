import os

print(os.path.abspath('/data/gocpplua/python'))

print(os.path.abspath(os.path.join('/data/gocpplua/python', '..')))


_, list_path=os.path.split('/data/gocpplua/python')
print(list_path)

