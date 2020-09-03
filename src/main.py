from config import *
from .preprocess import SimplePreprocessor
from .img_to_txt import ocr_data, get_data


# Load preprocessor clas
sp = SimplePreprocessor(DATA)

# apply preprocessing on images,
sp.preprocess(thresh=True, blur=True)

# fetch text from images
df = ocr_data()

# parse data to get data and Amount
df = get_data(df)

# print output dataframe which contains image name and Total amount
print(df)













