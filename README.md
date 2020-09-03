# Problem Statement
From restaurant bill images, find out date and Total Amount using Computer Vision.


# Approach/Steps
- We will store image data in a directory **data**

- Using `SimplePreprocessor` class we'll read the images and
  apply preprocessing steps like resizing the image, thresholding
  and blurring the image.
  
  *Note: We can choose above steps by setting parameter `True`*
  
- `ocr_data` function from `img_to_txt.py` fetches the text data from image
  using `tesseract`

- `get_data` function parse dates and amount from the text retrieved
   from `ocr_data` and save data into DataFrame
   

# Future Scope
- We can ask user to take a photo with all 4 corners and using 
  ORB algorithm and Hamming method to align images properly
  which will yield better result
  
- We can add few more preprocessing steps like Morphological operations

- We can train DeepLearning model instead of tesseract 
  to get text from the image
  
- We can use *Entity Extractors* like NER instead of RegEx to extract
  date and Amount