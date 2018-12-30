#renames all files with.jpg to match with root directory's name
import os
import shutil
from shutil import *
from PIL import Image
import pdb

rootdir=r'/Users/mac/Documents/workspace/Scrap'
def rename():
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.jpg'):
                root= os.path.basename(subdir)
                print os.path.join(subdir, file)
                print (root)
                print(file)
                os.rename(os.path.join(subdir, file), os.path.join(subdir, root+file))

#copies .jpg files and stores in certain dir
def copy():
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.jpg'):
                root= os.path.basename(subdir)
                if not os.path.exists('/Users/mac/Documents/workspace/Scrap/all/'+file):
                    copy2(os.path.join(subdir, file), '/Users/mac/Documents/workspace/Scrap/all/')
                else:
                    continue

def resizeAllImages():
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.jpg'):
                img = Image.open(file)
                img = img.resize((570,570),Image.ANTIALIAS)
                img.save(file,optimize=True, quality=85)


def resizeImage():
    import cv2
    desired_size = 570
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.jpg'):
                im_pth = file
                im = cv2.imread(subdir+'/'+im_pth)
                old_size = im.shape[:2] # old_size is in (height, width) format
                ratio = float(desired_size)/max(old_size)
                new_size = tuple([int(x*ratio) for x in old_size])
                # new_size should be in (width, height) format
                im = cv2.resize(im, (new_size[1], new_size[0]))
                delta_w = desired_size - new_size[1]
                delta_h = desired_size - new_size[0]
                top, bottom = delta_h//2, delta_h-(delta_h//2)
                left, right = delta_w//2, delta_w-(delta_w//2)
                color = [256, 256, 256]
                new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
                    value=color)
                cv2.imwrite(subdir+'/'+im_pth,new_im)

if __name__=='__main__':
    resizeImage()
    #resizeAllImages()
    # rename()
    # copy()
