import tkinter as tk
from tkinter import filedialog

def select_file():
    # 1. Create a hidden root window to prevent an empty GUI from popping up
    root = tk.Tk()
    root.withdraw() 
    
    # 2. Define allowed file extensions
    file_types = [
        ("Text files", "*.txt"),
        ("CSV files", "*.csv"),
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

if __name__ == "__main__":
    select_file()
