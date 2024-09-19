from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import object_detection as od  # Assuming this is the detection module
import threading
import cv2
import imageio


class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Traffic Signal Violation Detection System")
        self.pack(fill=BOTH, expand=1)

        # Initialize attributes
        self.filename = None
        self.img = None
        self.tkimage = None
        self.result = None

        # Set up the menu
        self.create_menu()

        # Canvas to display images
        self.canvas = Canvas(self, width=800, height=600)
        self.canvas.pack()

    def create_menu(self):
        # Creating a menu bar
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        # File menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Exit", command=self.client_exit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Analyze menu
        analyze_menu = Menu(menu_bar, tearoff=0)
        analyze_menu.add_command(label="Region of Interest", command=self.process_image_threaded)
        menu_bar.add_cascade(label="Analyze", menu=analyze_menu)

    def open_file(self):
        # Open a file dialog to select an image
        self.filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png")])
        if self.filename:
            try:
                # Open and display the image
                self.img = Image.open(self.filename)
                self.tkimage = ImageTk.PhotoImage(self.img)
                self.canvas.create_image(0, 0, anchor=NW, image=self.tkimage)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open image: {e}")

    def client_exit(self):
        self.master.quit()

    def process_image_threaded(self):
        if self.filename:
            # Run image processing in a separate thread to avoid freezing the GUI
            threading.Thread(target=self.process_image).start()
        else:
            messagebox.showerror("Error", "No image selected. Please open an image file first.")

    def process_image(self):
        try:
            # Load the image using OpenCV for processing
            img_cv = cv2.imread(self.filename)
            # Perform object detection (assuming this function exists in 'object_detection' module)
            self.result = od.detect_violations(img_cv)

            # Update the GUI with the processed result (if applicable)
            result_image_path = "output/result.jpg"  # Assuming the result gets saved here
            result_img = Image.open(result_image_path)
            self.tkimage = ImageTk.PhotoImage(result_img)
            self.canvas.create_image(0, 0, anchor=NW, image=self.tkimage)

            messagebox.showinfo("Info", "Image processed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image: {e}")


# Main function to run the GUI
def main():
    root = Tk()
    root.geometry("800x600")
    app = Window(master=root)
    root.mainloop()


if __name__ == "__main__":
    main()
