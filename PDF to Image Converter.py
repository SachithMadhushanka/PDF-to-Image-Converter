import fitz
import os
import tkinter as tk
from tkinter import filedialog, messagebox

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

    def select_file(self):
        self.filepath = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])

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

root = tk.Tk()
app = PDFConverterApp(root)
root.mainloop()
