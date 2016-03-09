import os

def MyRemoveFolderContent( top ):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            print os.path.join(root, name)
            # os.remove( os.path.join(root, name))

        for name in dirs:
            print os.path.join(root, name)
            # os.rmdir(os.path.join(root, name))