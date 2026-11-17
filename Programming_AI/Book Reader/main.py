import pytesseract
import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import Image


def select_file():
    # 1. Create a hidden root window to prevent an empty GUI from popping up
    root = tk.Tk()
    root.withdraw() 
    
    # 2. Define allowed file extensions
    file_types = [
        ("Image files", "*.png;*.jpg;*.jpeg"),
        ("All files", "*.*")
    ]
    
    # 3. Open the dialog box
    file_path = filedialog.askopenfilename(
        title="Select a File",
        initialdir="/Users/yomitha/Downloads",
        filetypes=file_types
    )
    
    # 4. Process the selected path
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("User cancelled the selection.")

    return file_path  # Return the selected file path for further processing

if __name__ == "__main__":
    img_path = select_file()
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # ty: ignore[no-matching-overload]
    # thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
    boxes = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    for i in range(len(boxes['text'])):
        if int(boxes['conf'][i]) > 20: # confidence filter
            x, y, w, h = boxes['left'][i], boxes['top'][i], boxes['width'][i], boxes['height'][i]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, boxes['text'][i], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    # cv2.rectangle(img, (boxes['left'][0], boxes['top'][0]), (boxes['left'][0] + boxes['width'][0], boxes['top'][0] + boxes['height'][0]), (0, 255, 0), 2)
    cv2.imshow("Gray Image", img) 
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        
    
    text = pytesseract.image_to_string(img, lang='eng')
    print(f"\nExtracted text:\n{text}")