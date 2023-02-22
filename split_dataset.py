# This script splits NTU Dataset to Train, Test, Validation
# NTU Total videos in an action class = 948
# Train : Test : Validate = 8 : 2 : 2
# Train : Test : Validate (without replication) = 4 : 1 : 1

'''
Input
----
dataset path

Required structure
------------------
dataset/train/action/*.avi
dataset/test/action/*.avi
dataset/validate/action/*.avi
'''

import argparse
import glob
import os
from shutil import copyfile

def create_dirstruct(rootdir, dirname):
    try:
        os.makedirs(rootdir + '/test/' + dirname)
    except FileExistsError:
        pass
    try:
        os.makedirs(rootdir + '/train/' + dirname)
    except FileExistsError:
        pass
    try:
        os.makedirs(rootdir + '/validate/' + dirname)
    except FileExistsError:
        pass

def run_split(action, rootdir):
    cam_orientation = list(range(1, 4))
    action_dir = os.path.basename(action)
    create_dirstruct(rootdir, action_dir)
    for orient in range(len(cam_orientation)):
        count = 1
        for vid_file in glob.glob(f'{action}/**/*C00{str(cam_orientation[orient])}*R001*.avi', recursive=True):
            if count <= 4:
                copyfile(r'{}'.format(vid_file), r'{}/{}/{}/{}'.format(rootdir, 'train', action_dir,
                                                                       os.path.basename(vid_file)))
                copyfile(r'{}'.format(vid_file), r'{}/{}/{}/{}'.format(rootdir, 'train', action_dir,
                                                                       os.path.basename(vid_file).replace('R001',
                                                                                                          'R002')))
            elif count == 5:
                copyfile(r'{}'.format(vid_file), r'{}/{}/{}/{}'.format(rootdir, 'test', action_dir,
                                                                       os.path.basename(vid_file)))
                copyfile(r'{}'.format(vid_file), r'{}/{}/{}/{}'.format(rootdir, 'test', action_dir,
                                                                       os.path.basename(vid_file).replace('R001',
                                                                                                          'R002')))
            elif count == 6:
                copyfile(r'{}'.format(vid_file), r'{}/{}/{}/{}'.format(rootdir, 'validate', action_dir,
                                                                       os.path.basename(vid_file)))
                copyfile(r'{}'.format(vid_file), r'{}/{}/{}/{}'.format(rootdir, 'validate', action_dir,
                                                                       os.path.basename(vid_file).replace('R001',
                                                                                                          'R002')))
                count = 0
            else:
                print(f'Bad use of count variable. count = {count}')
            count += 1


if __name__ == "__main__":
    praser = argparse.ArgumentParser()
    praser.add_argument('--action', required=True, type=str, help='dir holding action videos')
    praser.add_argument('--rootdir', default='dataset', type=str, help='root dir which stores train,test,validate')
    args = praser.parse_args()

    #print(len(glob.glob(f'{args.action}/**/*{args.setup}*.avi' , recursive=True)))

    run_split(args.action, args.rootdir)

