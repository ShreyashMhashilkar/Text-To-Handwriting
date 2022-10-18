import pywhatkit as pwk
import cv2

def convert_text(text):
    pwk.text_to_handwriting(text, save_to="handwriting.png")


if __name__=="__main__":
    text = input("Enter text : ")
    convert_text(text)
