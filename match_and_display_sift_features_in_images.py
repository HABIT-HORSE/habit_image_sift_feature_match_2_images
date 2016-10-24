'''
Author:  Steve North
Author URI:  http://www.cs.nott.ac.uk/~pszsn/
License: AGPLv3 or later
License URI: http://www.gnu.org/licenses/agpl-3.0.en.html
Can: Commercial Use, Modify, Distribute, Place Warranty
Can't: Sublicence, Hold Liable
Must: Include Copyright, Include License, State Changes, Disclose Source

Copyright (c) 2016, The University of Nottingham
'''

from PIL import Image
from pylab import *
from vlfeat_interface import *

root_path_A = "./inputA"
root_path_B = "./inputB"

# Next line controls whether it outputs 3 images (1 and 2 are the input images with features overlaid) or just the matches image.
showSIFTfeatureImages = True

for filename in os.listdir(root_path_A):
  if ".sift" in filename:
    featuresA = filename
  if ".jpg" in filename or ".JPG" in filename or ".pgm" in filename or ".PGM" in filename:
    imageA = filename

for filename in os.listdir(root_path_B):
  if ".sift" in filename:
    featuresB = filename
  if ".jpg" in filename or ".JPG" in filename or ".pgm" in filename or ".PGM" in filename:
    imageB = filename
	
l,d = read_features_from_file(root_path_A + "/" + featuresA)
im = array(Image.open(root_path_A + "/" + imageA))
if showSIFTfeatureImages:
  figure()
  plot_features(im,l,True)

l2,d2 = read_features_from_file(root_path_B + "/" + featuresB)
im2 = array(Image.open(root_path_B + "/" + imageB))
if showSIFTfeatureImages:
  figure()
  plot_features(im2,l2,True)

m = match_twosided(d,d2)
figure()
plot_matches(im,im2,l,l2,m)

show()