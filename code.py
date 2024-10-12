import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

path = ("C:\\Users\\kolah\\Downloads\\img handwriting.jpg")
img = cv.imread(path, 0)
blurred = cv.GaussianBlur(img,(5,5),0) 
edged = cv.Canny(blurred, 30, 150)
contours, hierarchy = cv.findContours(edged, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
x, y, w, h = cv.boundingRect(cnt)
maxX = 0
firstX = x
firstY = y
firstH = h
firstW = w
rect = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
deviations = [] 
for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    if((x > maxX) and ( (y < (firstY + 15)) and (y > (firstY -15)) )):
        maxX = x
        maxW = w


for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    if((y < (firstY + 15)) and (y > (firstY -15)) ):
        deviations.append(((firstY) - (y)))
        deviations.append(((firstY+firstH) - (y+h)))
        
print(sum(deviations) / len(deviations))
cv.line(img, tuple((firstX, firstY+firstH)), tuple(( (maxX + maxW), (firstY+firstH))),(0,255,0),2)
cv.imshow("Bounding Rectangle", img)
cv.waitKey(0)
cv.destroyAllWindows()






img = cv.imread(path, 0)
blurred = cv.GaussianBlur(img,(5,5),0) 
edged = cv.Canny(blurred, 30, 150)
contours, hierarchy = cv.findContours(edged, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


right_aligment_counter = 0
left_aligment_counter = 0

for cnt in contours:
    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    box = np.int64(box)
    cv.drawContours(img,[box],0,(0,0,255),2)
    x1 = (box[0])[0]
    y1 = (box[0])[1]

    x2 = (box[1])[0]
    y2 = (box[1])[1]

    x4 = (box[3])[0]
    y4 = (box[3])[1]


    
    d = math.sqrt( ((x2 - x1)**2) + ((y2 - y1)**2))
    e = math.sqrt( ((x4 - x1)**2) + ((y4 - y1)**2))

    # if the left most point and the top point is the larger edge than it means it is right leaning
    if(d > e):
        right_aligment_counter += 1
    
    
    # if the left most point and the bottom point is the larger edge than it means it is left leaning
    if(e > d):
        left_aligment_counter += 1


 # if there is more right leaning letter therefore it is a right leaning word
if(right_aligment_counter > left_aligment_counter):
    print("right:Sociable ,responsive, intrested in others,friendly")

 # if there is more left leaning letter therefore it is a left leaning word
if(right_aligment_counter < left_aligment_counter):
    print("left:Resrved, observant,self-reliant,non-intrusive")

# if there equal of left leaning and right leaning letters than the word aligned
if(right_aligment_counter == left_aligment_counter):
    print("veritical:practical, independent,controlled,self-suffcient")





def analyze_image(path):
    
    img = cv.imread(path, cv.IMREAD_GRAYSCALE)

    
    baseline_values = img[-1, :]

    
    differences = np.diff(baseline_values)

    
    positive_count = np.sum(differences > 0)
    negative_count = np.sum(differences < 0)

    if positive_count > negative_count:
        return "Ascending"
    elif positive_count < negative_count:
        return "Descending"
    else:
        return "Straight"

if __name__ == "__main__":
     

    
    baseline_analysis = analyze_image(path)
    print("Baseline analysis:", baseline_analysis)

    
    if baseline_analysis == "Ascending":
        print("Optimistic, Upbeat, Positive Attitude, Ambitious, Hopeful")
    elif baseline_analysis == "Descending":
        print("Tired, Overwhelmed, Pessimistic, not Hopeful")
    else:
        print("Wavering, Lacks definite direction, Emotionally unsettled, Unpredictable")




def analyze_image(path):
    
    img = cv.imread(path, cv.IMREAD_GRAYSCALE)


    img_blur = cv.GaussianBlur(img, (5, 5), 0)

    
    _, thresh_img = cv.threshold(img_blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)


    threshold_value = cv.threshold(img_blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[0]

    return threshold_value

if __name__ == "__main__":
      

    
    threshold_value = analyze_image(path)
    print("Threshold value:", threshold_value)

    
    if threshold_value > 150:
        print("HEAVY PRESSURE: Have very deep and enduring feelings and feel situations intensely")
    else:
        print("LIGHT PRESSURE: can endure traumatic experiences without being seriously affected.")




def analyze_image(path):
    
    img = cv.imread(path)


    text = pytesseract.image_to_string(img)

    
    num_uppercase = sum(1 for char in text if char.isupper())
    num_lowercase = sum(1 for char in text if char.islower())
    total_letters = len(text)

    
    uppercase_ratio = num_uppercase / total_letters
    lowercase_ratio = num_lowercase / total_letters

    
    if uppercase_ratio < 1.0:
        return "Big letters"
    elif lowercase_ratio < 0.2:
        return "Small letters"
    else:
        return "Average letters"

if __name__ == "__main__":
      

    
    paragraph_analysis = analyze_image(path)
    print("Paragraph analysis:", paragraph_analysis)

    
    if paragraph_analysis == "Big letters":
        print("Likes being noticed and stands out of crowd")
    elif paragraph_analysis == "Small letters":
        print("Introspective, not seeking attention, modest")
    else:
        print("Adaptable, fits into crowd and confident")

    
    

