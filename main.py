import cv2
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#pip install opencv-python
#pip install Pillow
#pip install matplotlib

class PunktoperatorenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Punktoperatoren Anwendung")
        self.root.geometry("1400x1200")

        self.cap = cv2.VideoCapture(0)

        # Initialisiere die Verarbeitungsfunktionen mit Standardfunktionen
        self.processing_function_main = lambda rgb_image: rgb_image
        self.processing_function_second = lambda rgb_image: rgb_image

        # Aktiver Button
        self.active_button = None

        # Erstelle Histogramm-Figuren und Canvas-Objekte für Originalbbild und Punktoperatoren
        self.fig_main, self.ax_main = plt.subplots()
        self.canvas_main = FigureCanvasTkAgg(self.fig_main, master=self.root)
        self.canvas_main_widget = self.canvas_main.get_tk_widget()
        self.canvas_main_widget.grid(row=2, column=0, padx=10, pady=10)

        self.fig_second, self.ax_second = plt.subplots()
        self.canvas_second = FigureCanvasTkAgg(self.fig_second, master=self.root)
        self.canvas_second_widget = self.canvas_second.get_tk_widget()
        self.canvas_second_widget.grid(row=2, column=1, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        self.button_style_inactive = {'bg': 'white', 'fg': 'black'}
        self.button_style_active = {'bg': 'blue', 'fg': 'white'}

        # Frame für die Buttons
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # "Original" Button
        self.original_button = tk.Button(
            button_frame, text="Original", command=self.apply_original_processing, **self.button_style_inactive)
        self.original_button.pack(side=tk.LEFT)

        # "Grau" Button
        self.grey_button = tk.Button(
            button_frame, text="Grau", command=self.apply_grey_processing, **self.button_style_inactive)
        self.grey_button.pack(side=tk.LEFT)

        # "Negativ" Button
        self.negative_button = tk.Button(
            button_frame, text="Negativ", command=self.apply_negative_processing, **self.button_style_inactive)
        self.negative_button.pack(side=tk.LEFT)

        #Hier weitere Buttons anlegen zum Darstellen    <-----------------------------------------------------------------
        #genauso wie oben runterkopieren und namen umändern - Albert 
        #Zum Beispiel für eine Punktoperation a:
        # "a" Button
        #self.a_button = tk.Button(
        #    button_frame, text="a", command=self.apply_a_processing, **self.button_style_inactive)
        #self.negative_button.pack(side=tk.LEFT)







        # Label für das Originalvideo
        self.label = tk.Label(self.root)
        self.label.grid(row=1, column=0, padx=10, pady=10)

        # Label für das zweite Video (Punktoperatoren)
        self.label_original = tk.Label(self.root)
        self.label_original.grid(row=1, column=1, padx=100, pady=10)  

        self.update_feed()

    def apply_original_processing(self):
        if self.active_button != self.original_button:
            self.set_active_button(self.original_button)
            self.set_processing_function(self.apply_original)
            self.update_button_style()

    def apply_grey_processing(self):
        if self.active_button != self.grey_button:
            self.set_active_button(self.grey_button)
            self.set_processing_function(self.apply_grey)
            self.update_button_style()

    def apply_negative_processing(self):
        if self.active_button != self.negative_button:
            self.set_active_button(self.negative_button)
            self.set_processing_function(self.apply_negative)
            self.update_button_style()

    #Nun geben wir den Buttons auch Logik    <-----------------------------------------------------------------
    #Beispiel wieder für a
    #def apply_a_processing(self):
    #    if self.active_button != self.a_button:
    #        self.set_active_button(self.a_button)
    #        self.set_processing_function(self.apply_a)
    #        self.update_button_style()





    def set_active_button(self, button):
        if self.active_button:
            self.active_button.config(**self.button_style_inactive)
        self.active_button = button
        self.active_button.config(**self.button_style_active)

    def set_processing_function(self, processing_function):
        self.processing_function_second = processing_function

    def apply_original(self, rgb_image):
        return rgb_image

    def apply_grey(self, rgb_image):
        return cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

    def apply_negative(self, rgb_image):
        return 255 - rgb_image
    
    #Hier legt ihr noch die richtige Funktion für den Punktoperator an    <-----------------------------------------------------------------
    #Wieder am Beispiel für a
    #def apply_a(self, rgb_image):
    #    return rgb_image
    # halt nicht rgb_image sondern das bearbeitete Bild zurückgeben - Albert






    def update_button_style(self):
        pass  # Stil wird nun in set_active_button gesetzt

    def update_feed(self):
        ret, frame = self.cap.read()
        if ret:
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Verarbeitung für das Originalvideo
            processed_image_main = self.processing_function_main(rgb_image)

            # Verkleinere das Bild für das Originalvideo
            small_image_main = cv2.resize(processed_image_main, (640, 480))
            img_main = Image.fromarray(small_image_main)
            img_tk_main = ImageTk.PhotoImage(image=img_main)
            self.label.img = img_tk_main
            self.label.config(image=img_tk_main)

            # Berechne und zeichne Histogramm für Originalvideo
            hist_main = cv2.calcHist([processed_image_main], [0], None, [256], [0, 256])
            self.ax_main.clear()
            self.ax_main.plot(hist_main)
            self.ax_main.set_title('Histogramm Originalvideo')
            self.canvas_main.draw()

            # Verarbeitung für das zweite Video 
            processed_image_second = self.processing_function_second(rgb_image)

            # Verkleinere das Bild für das zweite Video
            small_image_second = cv2.resize(processed_image_second, (640, 480))
            img_second = Image.fromarray(small_image_second)
            img_tk_second = ImageTk.PhotoImage(image=img_second)
            self.label_original.img = img_tk_second
            self.label_original.config(image=img_tk_second)

            # Berechne und zeichne Histogramm für das zweite Video 
            hist_second = cv2.calcHist([processed_image_second], [0], None, [256], [0, 256])
            self.ax_second.clear()
            self.ax_second.plot(hist_second)
            self.ax_second.set_title('Histogramm Punktoperator')
            self.canvas_second.draw()

            if self.root and self.root.winfo_exists():
                self.root.after(10, self.update_feed)

    def on_closing(self):
        self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PunktoperatorenApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()