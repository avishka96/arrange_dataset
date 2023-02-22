# annotate dataset
import os
import argparse

def create_annotxt(insp_dir):
    ref_dict = {
        "Kicking": 1,
        "Pushing": 2,
        "Handshake": 3,
        "Hi-Five": 4,
        "Hugging": 5,
                }
    anno_test = []
    anno_train = []
    anno_validate = []
    for root, dir, files in os.walk(r"{}".format(insp_dir)):
        if 'test' in root and 'kpts' in root:
            for key in ref_dict:
                if key in root:
                    cat = ref_dict[key]
                    break
            test_row = '{} 1 {} {}\n'.format(root.replace(insp_dir,'')[1:], len(files), cat)
            anno_test.append(test_row)
        elif 'train' in root and 'kpts' in root:
            for key in ref_dict:
                if key in root:
                    cat = ref_dict[key]
                    break
            train_row = '{} 1 {} {}\n'.format(root.replace(insp_dir, '')[1:], len(files), cat)
            anno_train.append(train_row)
        elif 'validate' in root and 'kpts' in root:
            for key in ref_dict:
                if key in root:
                    cat = ref_dict[key]
                    break
            train_row = '{} 1 {} {}\n'.format(root.replace(insp_dir, '')[1:], len(files), cat)
            anno_validate.append(train_row)
    with open('annotation_test.txt','a') as test_file:
        test_file.writelines(anno_test)
    with open('annotation_train.txt', 'a') as test_file:
        test_file.writelines(anno_train)
    with open('annotation_validate.txt', 'a') as test_file:
        test_file.writelines(anno_validate)

if __name__ == "__main__":
    praser = argparse.ArgumentParser()
    praser.add_argument('--viddir', type=str, required=True, help='directory to inspect')
    args = praser.parse_args()

    create_annotxt(args.viddir)

