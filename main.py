import cv2
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class PunktoperatorenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Punktoperatoren Anwendung")
        self.root.geometry("1300x1200")

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
        self.canvas_main_widget.grid(row=3, column=0, padx=2, pady=2)

        self.fig_second, self.ax_second = plt.subplots()
        self.canvas_second = FigureCanvasTkAgg(self.fig_second, master=self.root)
        self.canvas_second_widget = self.canvas_second.get_tk_widget()
        self.canvas_second_widget.grid(row=3, column=1, padx=2, pady=2)

        self.create_widgets()

    def create_widgets(self):
        self.button_style_inactive = {'bg': 'white', 'fg': 'black'}
        self.button_style_active = {'bg': 'blue', 'fg': 'white'}

        # Frame für die Buttons
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=0, column=0, padx=2, pady=2, sticky="nw")

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

        # "Helligkeitsveränderung" Button
        self.helligkeit_button = tk.Button(
            button_frame, text="Helligkeitsveränderung", command=self.apply_helligkeit_processing, **self.button_style_inactive)
        self.helligkeit_button.pack(side=tk.LEFT)

        # "Kontrastveränderung" Button
        self.kontrast_button = tk.Button(
            button_frame, text="Kontrastveränderung", command=self.apply_kontrast_processing, **self.button_style_inactive)
        self.kontrast_button.pack(side=tk.LEFT)

        # "Normalisierung" Button
        self.normalisierung_button = tk.Button(
            button_frame, text="Normalisierung", command=self.apply_normalisierung_processing, **self.button_style_inactive)
        self.normalisierung_button.pack(side=tk.LEFT)

        # "Histogrammausgleich" Button
        self.histogrammausgleich_button = tk.Button(
            button_frame, text="Histogrammausgleich", command=self.apply_histogrammausgleich_processing, **self.button_style_inactive)
        self.histogrammausgleich_button.pack(side=tk.LEFT)

        # Frame für die Buttons2
        button_frame2 = tk.Frame(self.root)
        button_frame2.grid(row=0, column=1, padx=10, pady=2, sticky="nw")

        # "Binarisierung" Button
        self.binarisierung_button = tk.Button(
            button_frame2, text="Binarisierung", command=self.apply_binarisierung_processing, **self.button_style_inactive)
        self.binarisierung_button.pack(side=tk.LEFT)

        # "Gamma-Korrektur" Button
        self.gammakorrektur_button = tk.Button(
            button_frame2, text="Gamma-Korrektur", command=self.apply_gammakorrektur_processing, **self.button_style_inactive)
        self.gammakorrektur_button.pack(side=tk.LEFT)

        # "Truncation" Button
        self.truncation_button = tk.Button(
            button_frame2, text="Truncation", command=self.apply_truncation_processing, **self.button_style_inactive)
        self.truncation_button.pack(side=tk.LEFT)

        # "Clipping" Button
        self.clipping_button = tk.Button(
            button_frame2, text="Clipping", command=self.apply_clipping_processing, **self.button_style_inactive)
        self.clipping_button.pack(side=tk.LEFT)

        # "Otsu" Button
        self.otsu_button = tk.Button(
            button_frame2, text="Otsu", command=self.apply_otsu_processing, **self.button_style_inactive)
        self.otsu_button.pack(side=tk.LEFT)

        # "Logarithmus" Button
        self.logarithmus_button = tk.Button(
            button_frame2, text="Logarithmus", command=self.apply_logarithmus_processing, **self.button_style_inactive)
        self.logarithmus_button.pack(side=tk.LEFT)

        # "Exponential" Button
        self.exponential_button = tk.Button(
            button_frame2, text="Exponential", command=self.apply_exponential_processing, **self.button_style_inactive)
        self.exponential_button.pack(side=tk.LEFT)

        # Frame für Label, Input-Feld und WertebereichHilfe
        input_frame = tk.Frame(self.root)
        input_frame.grid(row=1, column=0, padx=2, pady=2, sticky="nw")

        # Label "Wert"
        label_wert = tk.Label(input_frame, text="Wert:")
        label_wert.grid(row=0, column=0, padx=2, pady=2, sticky="w")

        #Input-Field
        self.input_field = tk.Entry(input_frame)
        self.input_field.grid(row=0, column=1, padx=2, pady=2, sticky="w")

        # Label "Eingabe Wertebereich"
        self.label_hilfe = tk.Label(input_frame, text=" ")
        self.label_hilfe.grid(row=0, column=2, padx=2, pady=2, sticky="w")

        # Label für das Originalvideo
        self.label = tk.Label(self.root)
        self.label.grid(row=2, column=0, padx=2, pady=0)

        # Label für das zweite Video (Punktoperatoren)
        self.label_original = tk.Label(self.root)
        self.label_original.grid(row=2, column=1, padx=10, pady=0) 

        # Frame for additional buttons
        button_frame3 = tk.Frame(self.root)
        button_frame3.grid(row=1, column=1, padx=10, pady=2, sticky="nw")

        # Create color buttons
        self.color_buttons = {}
        self.active_color_button = None

        colors = ["Bunt", "Grau", "Rot", "Grün", "Blau"]

        for color in colors:
            button = tk.Button(button_frame3, text=color, command=lambda c=color: self.set_color_processing(c),
                              **self.button_style_inactive)
            button.grid(row=0, column=len(self.color_buttons), padx=2, pady=2, sticky="w")
            self.color_buttons[color] = button

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

    def apply_helligkeit_processing(self):
        if self.active_button != self.helligkeit_button:
            self.set_active_button(self.helligkeit_button)
            self.set_processing_function(self.apply_helligkeit)
            self.update_button_style()

    def apply_kontrast_processing(self):
        if self.active_button != self.kontrast_button:
            self.set_active_button(self.kontrast_button)
            self.set_processing_function(self.apply_kontrast)
            self.update_button_style()

    def apply_normalisierung_processing(self):
        if self.active_button != self.normalisierung_button:
            self.set_active_button(self.normalisierung_button)
            self.set_processing_function(self.apply_normalisierung)
            self.update_button_style()

    def apply_histogrammausgleich_processing(self):
        if self.active_button != self.histogrammausgleich_button:
            self.set_active_button(self.histogrammausgleich_button)
            self.set_processing_function(self.apply_histogrammausgleich)
            self.update_button_style()

    def apply_binarisierung_processing(self):
        if self.active_button != self.binarisierung_button:
            self.set_active_button(self.binarisierung_button)
            self.set_processing_function(self.apply_binarisierung)
            self.update_button_style()

    def apply_gammakorrektur_processing(self):
        if self.active_button != self.gammakorrektur_button:
            self.set_active_button(self.gammakorrektur_button)
            self.set_processing_function(self.apply_gammakorrektur)
            self.update_button_style()   

    def apply_truncation_processing(self):
        if self.active_button != self.truncation_button:
            self.set_active_button(self.truncation_button)
            self.set_processing_function(self.apply_truncation)
            self.update_button_style()

    def apply_clipping_processing(self):
        if self.active_button != self.clipping_button:
            self.set_active_button(self.clipping_button)
            self.set_processing_function(self.apply_clipping)
            self.update_button_style()

    def apply_otsu_processing(self):
        if self.active_button != self.otsu_button:
            self.set_active_button(self.otsu_button)
            self.set_processing_function(self.apply_otsu)
            self.update_button_style()

    def apply_logarithmus_processing(self):
        if self.active_button != self.logarithmus_button:
            self.set_active_button(self.logarithmus_button)
            self.set_processing_function(self.apply_logarithmus)
            self.update_button_style()

    def apply_exponential_processing(self):
        if self.active_button != self.exponential_button:
            self.set_active_button(self.exponential_button)
            self.set_processing_function(self.apply_exponential)
            self.update_button_style()

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
        if len(rgb_image.shape) == 3 and rgb_image.shape[2] == 3:
            # Convert color image to grayscale
            grey_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
        else:
            # Image is already grayscale
            grey_image = rgb_image


        return grey_image

    def apply_negative(self, rgb_image):
        return 255 - rgb_image
    
    def apply_helligkeit(self, rgb_image):
        try:
            wert = np.clip(int(self.input_field.get()), -255, 255)
        except ValueError:
            wert = 0

        # Wertebereich-Text für das Label aktualisieren
        self.label_hilfe.config(text=f"Wertebereich: -255 >= {wert} >= 255")

       # Normalize the image to the range [0, 1]
        normalized_image = rgb_image / 255.0

        # Add brightness and clip values to the valid range [0, 1]
        brightened_image = np.clip(normalized_image + wert / 255.0, 0, 1)

        # Convert back to the range [0, 255]
        new_image = (brightened_image * 255).astype(np.uint8)

        return new_image

    def apply_kontrast(self, rgb_image):
        try:
            wert = max(0, float(self.input_field.get()))
        except ValueError:
            wert = 1.0

        # Wertebereich-Text für das Label aktualisieren
        self.label_hilfe.config(text=f"Wertebereich: {wert} ( 0.0 <= x <1.0 für Verminderung, 1.0 < x für Erhöhung)")

        # Normalize the image to the range [0, 1]
        normalized_image = rgb_image / 255.0

        # Decide whether to apply contrast enhancement or reduction
        if wert >= 0:
            # Apply contrast adjustment with a center of 0.5 and scale by wert for enhancement
            contrasted_image = np.clip((normalized_image - 0.5) * wert + 0.5, 0, 1)
        else:
            # Apply contrast adjustment with a center of 0.5 and scale by 1/abs(wert) for reduction
            contrasted_image = np.clip((normalized_image - 0.5) / abs(wert) + 0.5, 0, 1)

        # Convert back to the range [0, 255]
        new_image = (contrasted_image * 255).astype(np.uint8)

        return new_image

    def apply_normalisierung(self, rgb_image):
        # Wertebereich-Text für das Label aktualisieren
        self.label_hilfe.config(text=f" ")

        # Normalize the image to the range [0, 1]
        normalized_image = rgb_image / 255.0

        #minimum and maximum values
        minimum=normalized_image.min()
        maximum=normalized_image.max()

        # Calculate Normalization
        normed_image = (normalized_image-minimum)*(1/(maximum-minimum))

        # Convert back to the range [0, 255]
        new_image = (normed_image * 255).astype(np.uint8)

        return new_image

    def apply_histogrammausgleich(self, rgb_image):
        # Wertebereich-Text für das Label aktualisieren
        self.label_hilfe.config(text=f" ")

        # Konvertiere Bild in Graustufen, falls es im Farbmodus vorliegt
        grey_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

        # Wende Histogrammausgleich an
        equalized_image = cv2.equalizeHist(grey_image)

        # Konvertiere wieder zurück in RGB
        equalized_rgb_image = cv2.cvtColor(equalized_image, cv2.COLOR_GRAY2RGB)
        
        return equalized_rgb_image

    def apply_binarisierung(self, rgb_image):
        #get grey image  
        if len(rgb_image.shape) == 3 and rgb_image.shape[2] == 3:
            # Convert color image to grayscale
            grey_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
        else:
            # Image is already grayscale
            grey_image = rgb_image

        # Normalize the image to the range [0, 1]
        normalized_image = grey_image / 255.0

        #entscheidungsgrenze
        try:
            wert = max(0, float(self.input_field.get()))
        except ValueError:
            wert = 0.5
        normalized_plus_image = normalized_image + wert

        # Wertebereich-Text für das Label aktualisieren
        self.label_hilfe.config(text=f"Wertebereich: 0.0 >= {wert} >= 1.0")

        # round it down to 0 or 1
        binary_image = normalized_plus_image.astype(np.uint8)

        # Convert back to the range [0, 255]
        new_image = (binary_image * 255).astype(np.uint8)

        return new_image
    
    def apply_gammakorrektur(self, rgb_image):
        try:
            wert = max(0, float(self.input_field.get()))
        except ValueError:
            wert = 1.0

        # Wertebereich-Text für das Label aktualisieren
        self.label_hilfe.config(text=f"Wertebereich: 0 >= {wert} ")

        # https://lindevs.com/apply-gamma-correction-to-an-image-using-opencv
        try:    
            invGamma = 1.0 / wert
        except ZeroDivisionError:
            invGamma = 1.0 / (wert + 0.00000001) # verhindert Teilung durch 0

        table = [((i / 255) ** invGamma) * 255 for i in range(256)]
        table = np.array(table, np.uint8)
        return cv2.LUT(rgb_image, table)
    
    def apply_truncation(self, rgb_image):
        # Wertebereich-Text für das Label aktualisieren
        self.label_hilfe.config(text=f" ")

        #Führe Truncation für jeden Kanal separat durch
        truncated_image = np.clip(rgb_image, 0, 150)

        return truncated_image

    def apply_clipping(self, rgb_image):
        # Wertebereich-Text für das Label aktualisieren
        self.label_hilfe.config(text=f" ")

        # Clipping für jeden Kanal separat durchführen
        clipped_image = np.clip(rgb_image, 50,200)

        return clipped_image

    def apply_otsu(self, rgb_image):
        # Wertebereich-Text für das Label aktualisieren
        self.label_hilfe.config(text=f" ")

        # Konvertiere Bild in Graustufen
        grey_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

        # Wende Otsus Schwellenwertmethode an
        _, otsu_image = cv2.threshold(grey_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Konvertiere Bild zurück in RGB
        otsu_rgb_image = cv2.cvtColor(otsu_image, cv2.COLOR_GRAY2RGB)

        return otsu_rgb_image

    def apply_logarithmus(self, rgb_image):
        # Wertebereich-Text für das Label aktualisieren
        self.label_hilfe.config(text=f" ")

        # Wende Logartihmus- Transformation für jeden Kanal separat an
        logarithmic_image = np.log1p(rgb_image.astype(np.float32))

        #Konvertiere die Werte zurück in Bereich [0, 255]
        logarithmic_image = (logarithmic_image / logarithmic_image.max()) * 255
        logarithmic_image = logarithmic_image.astype(np.uint8)
        
        return logarithmic_image

    def apply_exponential(self, rgb_image):
        # Wertebereich-Text für das Label aktualisieren
        self.label_hilfe.config(text=f" ")

        # Normalisiere Pixelwerte auf Bereich [0, 1]
        normalized_image = rgb_image / 255.0

        # Wende Exponential-Transformation für jeden Kanal separat an
        exponential_image = np.exp(normalized_image)

        # Konvertiere Werte zurück in Bereich [0, 255]
        exponential_image = (exponential_image / exponential_image.max()) * 255
        exponential_image = exponential_image.astype(np.uint8)

        return exponential_image
    
    def update_button_style(self):
        pass  # Stil wird nun in set_active_button gesetzt

    def set_active_color_button(self, button):
        for color_button in self.color_buttons.values():
            color_button.config(**self.button_style_inactive)
    
        self.active_color_button = button
        self.active_color_button.config(**self.button_style_active)

    def set_color_processing(self, color):
        self.set_active_color_button(self.color_buttons[color])
        self.set_processing_function(lambda rgb_image: self.apply_color_processing(rgb_image, color))
        self.update_button_style()

    def apply_color_processing(self, rgb_image, color):
        if color == "Bunt":
            return rgb_image
        elif color == "Grau":
            if len(rgb_image.shape) == 3 and rgb_image.shape[2] == 3:
                # Convert color image to grayscale
                return cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
            else:
                # Image is already grayscale
                return rgb_image
        elif color == "Rot":
            # Apply red color transformation
            red_image = rgb_image * np.array([1, 0, 0])
            # Ensure the result is of type np.uint8
            return np.clip(red_image, 0, 255).astype(np.uint8)
        elif color == "Grün":
            # Apply green color transformation
            green_image = rgb_image * np.array([0, 1, 0])
            # Ensure the result is of type np.uint8
            return np.clip(green_image, 0, 255).astype(np.uint8)
        elif color == "Blau":
            # Apply blue color transformation
            blue_image = rgb_image * np.array([0, 0, 1])
            # Ensure the result is of type np.uint8
            return np.clip(blue_image, 0, 255).astype(np.uint8)
        
    def set_index(self, color):
        if color == "Bunt":
            return 0
        elif color == "Grau":
            return 0
        elif color == "Rot":
            return 0
        elif color == "Grün":
            return 1
        elif color == "Blau":
            return 2
        else:
            return 0

    def update_feed(self):
        ret, frame = self.cap.read()
        if ret:
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            self.index = 0

            # Apply color processing based on the active color button
            if self.active_color_button:
                color = self.active_color_button["text"]
                rgb_image = self.apply_color_processing(rgb_image, color)
                self.index = self.set_index(color)

            # Verarbeitung für das Originalvideo
            processed_image_main = self.processing_function_main(rgb_image)

            # Verkleinere das Bild für das Originalvideo
            small_image_main = cv2.resize(processed_image_main, (640, 480))
            img_main = Image.fromarray(small_image_main)
            img_tk_main = ImageTk.PhotoImage(image=img_main)
            self.label.img = img_tk_main
            self.label.config(image=img_tk_main)

            # Berechne und zeichne Histogramm für Originalvideo
            hist_main = cv2.calcHist([processed_image_main], [self.index], None, [256], [0, 256])
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
            hist_second = cv2.calcHist([processed_image_second], [self.index], None, [256], [0, 256])
            self.ax_second.clear()
            self.ax_second.plot(hist_second)
            self.ax_second.set_title('Histogramm Punktoperator')
            self.canvas_second.draw()

            if self.root and self.root.winfo_exists():
                self.root.after(10, self.update_feed)

    def on_closing(self):
        self.cap.release()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = PunktoperatorenApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()