import os


def path_to_dir(file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    res_dir = os.path.join(os.path.dirname(current_dir), 'resources')
    path_to_file = os.path.join(res_dir, file)
    return path_to_file




