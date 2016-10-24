habit_image_sift_feature_match_2_images

Author:  Steve North
Author URI:  http://www.cs.nott.ac.uk/~pszsn/
License: AGPLv3 or later
License URI: http://www.gnu.org/licenses/agpl-3.0.en.html
Can: Commercial Use, Modify, Distribute, Place Warranty
Can't: Sublicence, Hold Liable
Must: Include Copyright, Include License, State Changes, Disclose Source

Copyright (c) 2016, The University of Nottingham

This utility will compare the SIFT features for two images, displaying both images, with lines plotted between any matching features.

SIFT features should be robust to scaling, rotation, viewpoint changes and illumination.

Each of the input directories (inputA and inputB) should contain an image file and its associated extracted SIFT features file.

Dependencies: 

Usage: 

Seems to work best for:
SIFT file < 500k
JPG < 100k

File format for SIFT files:
Features are separated by a newline character (LF or \n).
Values within a feature are separated by a space.

Known issues:


