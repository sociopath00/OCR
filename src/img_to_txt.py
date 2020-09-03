import cv2
from pytesseract import Output
import pytesseract
from imutils import paths
from config import *
import pandas as pd
import os
import re


def ocr_data():
    images = paths.list_images(PROCESSED_DATA)

    text = []
    ids = []
    for i in images:
        img = cv2.imread(i)
        results = pytesseract.image_to_data(img, output_type=Output.DICT)

        # print(results["text"])
        # cv2.imshow("image", rgb)
        # cv2.waitKey(0)

        ids.append(os.path.basename(i))
        text.append(" ".join(results["text"]))

    df = pd.DataFrame({"images": ids, "text": text})
    return df


def get_data(data:pd.DataFrame):
    pattern = "\d{2}/\d{2}/\d{2,4}"
    pattern1 = "\d{2}-\d{2}-\d{2,4}"
    pattern2 = "\d+\.\d+"

    # df = pd.read_csv(data)
    df = pd.DataFrame(data)

    def find_dates(x):
        y = re.findall(pattern, x)
        if y:
            return y[0]
        else:
            y = re.findall(pattern1, x)
        return y

    def find_amount(x):
        y = re.findall(pattern2, x)
        if y:
            return max(y)
        else:
            return 0

    df["date"] = df["text"].apply(find_dates)
    df["total"] = df["text"].apply(find_amount)

    df.to_csv("final_output.csv", index=False)
    return df
