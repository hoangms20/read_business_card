import glob
import os
import random
import sys
import random
import math
import json
from collections import defaultdict
from typing import Counter

import cv2
from PIL import Image
import numpy as np
from scipy.ndimage.filters import rank_filter

def process_image_without_save(im, scale=1):
    # edges = cv2.Canny(np.asarray(im), 100, 200)
    im2 = cv2.bilateralFilter(im, 9, 25, 175)

def dilation(ary, N, iterations):
    """Dilate using an NxN '+' sign shape. ary is np.uint8."""
    kernel = np.zeros((N, N), dtype=np.uint8)
    kernel[int((N - 1) / 2), :] = 1
    dilated_image = cv2.dilate(ary / 255, kernel, iterations=iterations)

    kernel = np.zeros((N, N), dtype=np.uint8)
    kernel[:, int((N - 1) / 2)] = 1
    dilated_image = cv2.dilate(dilated_image, kernel, iterations=iterations)
    return dilated_image


if __name__ == "__main__":

    image_size = 500
    sample_path = 'samples/bc_ref/r_1.jpg'

    img = cv2.imread(sample_path)

    orig_width, orig_height, _ = img.shape

    # Make image smaller for faster processing
    scale = orig_width / image_size
    resized_img = cv2.resize(img, (image_size, int(orig_height / scale + 1)), None)

    im2 = cv2.bilateralFilter(resized_img, 9, 25, 175)

    edges = cv2.Canny(im2, 100, 200)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    borders = []
    area = edges.shape[0] * edges.shape[1]
    for i, c in enumerate(contours):
        x, y, w, h = cv2.boundingRect(c)
        if w * h > 0.5 * area:
            borders.append((i, x, y, x + w - 1, y + h - 1))

    borders.sort(key=lambda i_x1_y1_x2_y2: (i_x1_y1_x2_y2[3] - i_x1_y1_x2_y2[1]) * (i_x1_y1_x2_y2[4] - i_x1_y1_x2_y2[2]))


    count = 21
    #dilation = 5
    n = 1
    while count > 16:
        n = n + 1
        dilated_image = dilation(edges, N=3, iterations=n)
        abc = dilated_image.copy()
        dilated_image = dilated_image.astype(np.uint8)
        contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        count = len(contours)
    
    print(len(contours))
    print(len(hierarchy))

    cv2.imshow('dilated_image', abc)
    cv2.imshow('edges', edges)
    cv2.imshow('img2', im2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()