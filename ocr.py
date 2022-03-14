from pytesseract import Output
import pytesseract, cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

im = cv2.imread("images/code1.jpg")
results = pytesseract.image_to_string(im, lang = 'eng')

print("-" * 40)
print(
    'Results from tesseract: \n'
    f'{results}'
)
print("-" * 40)

results_list = results.replace(" ", "").split("\n")
final_list = list(filter(None, results_list))

print(
    'Final list of strings: \n'
    f'{final_list}')
print("-" * 40)