import glob
import os
import random
import sys
import random
import math
import json
from collections import defaultdict

import cv2
from PIL import Image
import numpy as np
from scipy.ndimage.filters import rank_filter

def process_image_without_save(im, scale=1):
    # edges = cv2.Canny(np.asarray(im), 100, 200)
    im2 = cv2.bilateralFilter(im, 9, 25, 175)


if __name__ == "__main__":
    sample_path = 'samples/bc_ref/r_1.jpg'