import argparse
from split_dataset import *
from vid2frames import *
from gen_annotate_txt import *

if __name__ == "__main__":
    praser = argparse.ArgumentParser()
    praser.add_argument('--directory', required=True, type=str, help='directory to run')
    praser.add_argument('--splitdir', default='dataset', type=str, help='root dir which stores train,test,validate')
    praser.add_argument('--framesdir', default='dataset_frames', type=str, help='directory storing video frames')
    praser.add_argument('--resize_width', default=1920, type=int, help='frame resize width')
    praser.add_argument('--resize_height', default=1080, type=int, help='frame resize height')
    args = praser.parse_args()

    run_split(args.directory, args.splitdir)
    dir2frames(args.splitdir, args.framesdir, args.resize_width, args.resize_height)
    create_annotxt(args.framesdir)

