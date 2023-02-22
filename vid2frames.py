import os
import cv2
import glob
import argparse

"""
Given individual video files (mp4, webm) on disk, creates a folder for
every video file and saves the video's RGB frames as jpeg files in that
folder.

It can be used to turn video dataset, which comes as 
many ".avi" or ".mp4" files, into a folder with ".jpeg" files for each frame.
Uses multithreading to extract frames faster.

Modify the two filepaths at the bottom and then run this script.

Use below command in your directory before running this script to remove .DS_Store files
    find . -name '.DS_Store' -type f -delete
"""

def video_to_rgb(video_filename, out_dir, resize_shape):
    file_template = 'frame_{:05d}.jpg'
    reader = cv2.VideoCapture(video_filename)
    success, frame, = reader.read()  # read first frame

    count = 1
    while success:
        out_filepath = os.path.join(out_dir, file_template.format(count))
        frame = cv2.resize(frame, resize_shape)
        cv2.imwrite(out_filepath, frame)
        success, frame = reader.read()
        count += 1

def dir2frames(dataset, outdir, width, height):
    for video_filename in glob.glob(f'{dataset}/**/*.avi', recursive=True):
        print(video_filename)
        out_name = video_filename[len(dataset)+1:len(video_filename)-4] #remove datasets and .avi from video_filename
        #print(out_name)
        out_dir = outdir + '/'+ str(out_name)
        try:
            os.makedirs(out_dir)
        except FileExistsError:
            print("File already exists")
        resize_shape = (width, height)
        #print(out_dir)
        video_to_rgb(video_filename, out_dir, resize_shape)


if __name__ == '__main__':
    praser = argparse.ArgumentParser()
    praser.add_argument('--dataset', type=str, required=True, help='dataset path')
    praser.add_argument('--width', type=int, default=960, help='img width')
    praser.add_argument('--height', type=int, default=540, help='img height')
    praser.add_argument('--outdir', type=str, default='dataset_frames', help='output dir name')
    args = praser.parse_args()

    dir2frames(args.dataset, args.outdir, args.width, args.height)


