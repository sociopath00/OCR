import pandas as pd
import re
from config import *
import argparse
import cv2
from .preprocess import SimplePreprocessor


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])



