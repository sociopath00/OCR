import cv2
from imutils import paths
from config import *
import os


class SimplePreprocessor:
    def __init__(self, images:str, height:int=512, width:int=512):
        self.height = height
        self.width = width
        self.images = images

    def preprocess(self, resize:bool=False, thresh:bool=False, blur:bool=False,):
        """
        :param resize: resize the image if set True
        :param thresh: apply thresholding if set True
        :param blur: apply gaussian blur if set True
        :return:
        """
        # load images
        images = paths.list_images(self.images)

        for i in images:
            # read each image and convert it into grayscale
            img = cv2.imread(i)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # resize the image if flag is True
            if resize:
                gray = cv2.resize(gray, (self.height, self.width))

            # Use thresholding to convert image into binary
            if thresh:
                gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

            # remove noise using Gaussian Blur
            if blur:
                gray = cv2.GaussianBlur(gray, (3, 3), 0)

            # write the grayscale image to disk as a temporary file so we can apply OCR to it
            filename = os.path.basename(i)
            filename = os.path.join(PROCESSED_DATA, filename)
            cv2.imwrite(filename, gray)

        return


if __name__ == "__main__":
    sp = SimplePreprocessor(DATA)
    sp.preprocess()
