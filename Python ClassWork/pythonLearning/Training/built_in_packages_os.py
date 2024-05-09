import os

files = os.listdir('.')
print("Files in the current directory:", files)

if not os.path.exists('my_directory'):
    os.mkdir('my_directory')
    print("Directory 'my_directory' created.")

if os.path.exists('my_file.txt'):
    os.remove('my_file.txt')
    print("File 'my_file.txt' removed.")

python_path = os.getenv('PYTHONPATH')
print("PYTHONPATH:", python_path)

path1 = 'C:\\Users\\Administrator\\Desktop\\Python Atomotive testing\\ClassWork\\pythonLearning\\Training'
path2 = 'my_file.txt'
full_path = os.path.join(path1, path2)
print("Full path:", full_path)

absolute_path = os.path.abspath('my_directory')
print("Absolute path of 'my_directory':", absolute_path)
