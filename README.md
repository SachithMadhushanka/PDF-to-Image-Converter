# PDF to Image Converter

## Overview

The PDF to Image Converter is a simple tool to convert each page of a PDF file into separate image files (PNG format). This application is built using Python and utilizes the `PyMuPDF` (also known as `fitz`) library to read PDF files and convert each page into images.

## Features

- Select a PDF file to convert.
- Convert each page of the PDF into separate PNG images.
- Display progress during conversion.
- Display a message box upon completion or error.

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- PyMuPDF (fitz)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/pdf-to-image-converter.git
   cd pdf-to-image-converter
   ```

2. **Install the required Python packages:**
   ```bash
   pip install PyMuPDF
   ```

## Usage

1. **Run the application:**
   ```bash
   python pdf_converter_app.py
   ```

2. **Use the application:**
   - Click the "Select File" button to choose a PDF file.
   - Click the "Convert" button to start converting the selected PDF file.
   - The application will create separate PNG images for each page of the PDF in the same directory as the PDF file.
   - Progress will be displayed in the title bar of the application window.
   - Upon completion or error, a message box will be displayed.

## Script Explanation

### Importing Libraries
```python
import fitz
import os
import tkinter as tk
from tkinter import filedialog, messagebox
```
- **fitz**: Used to read PDF files and convert pages into images.
- **os**: Used for file path manipulation and directory creation.
- **tkinter**: Used for the graphical user interface.
- **filedialog** and **messagebox**: Used for file selection and displaying messages.

### PDFConverterApp Class
#### Initialization
```python
class PDFConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("PDF to Image Converter")

        self.label = tk.Label(master, text="Select a PDF file to convert:")
        self.label.pack()

        self.button = tk.Button(master, text="Select File", command=self.select_file)
        self.button.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.pack()

        self.filepath = None
```
- Initializes the main window with a title, label, and buttons for file selection and conversion.

#### File Selection
```python
def select_file(self):
    self.filepath = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])
```
- Opens a file dialog to select a PDF file and stores the selected file path.

#### Conversion
```python
def convert(self):
    if not self.filepath:
        messagebox.showerror("Error", "Please select a PDF file.")
        return

    try:
        output_dir = os.path.splitext(self.filepath)[0]
        os.makedirs(output_dir, exist_ok=True)
        doc = fitz.open(self.filepath)
        total_pages = doc.page_count
        for pg in range(total_pages):
            page = doc[pg]
            pix = page.get_pixmap()
            output_path = os.path.join(output_dir, f"page_{pg+1}.png")
            pix.save(output_path, "png")
            # Update progress
            self.master.title(f"Converting... {pg+1}/{total_pages} pages")
            self.master.update_idletasks()
        doc.close()
        messagebox.showinfo("Conversion Complete", f"PDF to image conversion complete! {total_pages} pages converted.")
        self.master.title("PDF to Image Converter")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        self.master.title("PDF to Image Converter")
```
- Checks if a file is selected. If not, shows an error message.
- Creates a directory with the same name as the PDF file to store the converted images.
- Opens the PDF file, retrieves the total number of pages, and iterates through each page.
- Converts each page into a PNG image and saves it in the output directory.
- Displays progress in the title bar of the application window.
- Upon completion or error, displays a message box with the relevant information.

### Main Loop
```python
root = tk.Tk()
app = PDFConverterApp(root)
root.mainloop()
```
- Creates the main application window and starts the Tkinter event loop.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
