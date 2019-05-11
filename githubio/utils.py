import os
import shutil

from git import Repo


def update_github_io(local_path, git_url, create=True):
    # check if there is anyfile in path
    if not os.path.exists(local_path):
        if create:
            os.mkdir(local_path)
        else:
            raise ValueError('The provided local_path does not exist!')
    
    if len(os.listdir(local_path)) > 0:
        print('The local path is not empty. Current files will be removed.')
        for file_object in os.listdir(local_path):
            file_object_path = os.path.join(local_path, file_object)
            if os.path.isfile(file_object_path):
                os.unlink(file_object_path)
            else:
                shutil.rmtree(file_object_path)
            print('Removed: {}!'.format(file_object_path))
        print('Done with clear up the directory.')
    
    print('Cloning repository({}) to {}.'.format(git_url, local_path))
    Repo.clone_from(git_url, local_path)
    print('Done')
