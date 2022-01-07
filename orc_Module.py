from PIL import Image
import pytesseract
import os

def main():
    a =pytesseract.pytesseract.tesseract_cmd = r'tesseract'
    #指定tesseract.exe執行檔位置
    img = Image.open(r'/mnt/c/vscode_project/wzu_OCR/image/ocr_test2.png') #圖片檔案位置
    text = pytesseract.image_to_string(img, lang='eng') #讀英文
    text1 = pytesseract.image_to_string(img, lang='chi_sim') #簡體中文
    text2 = pytesseract.image_to_string(img, lang='chi_tra') #繁體中文
    print(text)
    # print(text1)
    # print(text2)
if __name__ == '__main__':
    main()