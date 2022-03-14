from pytesseract import Output
import pytesseract, cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

im = cv2.imread("images/code1.jpg")
results = pytesseract.image_to_string(im, lang = 'eng')

results_list = results.replace(" ", "").split("\n")
print(results_list)

for item in results_list:
    if item == "":
        results_list.remove(item)

print(results_list)