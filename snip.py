from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageGrab, ImageEnhance, ImageTk
import time 

class SnipImage:
    def __init__(self, root):
        self.root = root
        self.canvas = None
        self.background = None
        self.overlay = None
        self.background_image = None
        self.overlay_image = None
        self.captured_image = None 
        self.start = None
        self.end_x = None
        self.end_y = None
        self.drawn = False

    def startsnip(self):

        self.background = ImageGrab.grab()
        time.sleep(0.3)

        # Create a semi-transparent dark overlay
        self.overlay = Image.new("RGBA", self.background.size, (0, 0, 0, 200))

        # Convert the overlay to an ImageTk.PhotoImage object
        self.overlay_image = ImageTk.PhotoImage(self.overlay)
        self.background_image = ImageTk.PhotoImage(self.background)

        # Create a canvas with the background image
        self.canvas = Canvas(self.root, width=self.background.width, height=self.background.height, highlightthickness=0, cursor="crosshair")
        self.canvas.pack(fill=BOTH, expand=True)

        # Display the background image and the overlay
        self.canvas.create_image(0, 0, anchor=NW, image=self.background_image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.overlay_image)

        # Bind mouse events to the canvas
        self.canvas.bind('<ButtonPress-1>', self.on_start)
        self.canvas.bind('<B1-Motion>', self.on_grow)
        self.canvas.bind('<ButtonRelease-1>', self.end_capture)

    def on_start(self, event):
        self.start = event
        self.drawn = True

    def on_grow(self, event):
        if self.drawn:
            self.canvas.delete("rectangle")

        x0, y0 = self.start.x, self.start.y
        x1, y1 = event.x, event.y

        # Handle dragging in any direction
        self.canvas.create_rectangle(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1), outline="white", width=1, tags="rectangle")
        self.apply_brightness(x0, y0, x1, y1)

    def end_capture(self, event):
        self.end_x = event.x
        self.end_y = event.y
        self.capture_screen()

    def capture_screen(self):
        self.captured_image = ImageGrab.grab(bbox=(min(self.start.x, self.end_x), min(self.start.y, self.end_y), max(self.start.x, self.end_x), max(self.start.y, self.end_y)))
        self.root.destroy()
    
    def get_captured_image(self):
        return self.captured_image

    def apply_brightness(self, x0, y0, x1, y1):
        # Get the region inside the drawn rectangle
        region = self.background.crop((min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))
        enhancer = ImageEnhance.Brightness(region)
        region_bright = enhancer.enhance(1)  # Increase brightness (adjust as needed)

        # Create a temporary image for the overlay with the bright region
        temp_overlay = self.overlay.copy()
        temp_overlay.paste(region_bright, (min(x0, x1), min(y0, y1)))

        # Update the overlay on the canvas
        self.overlay_image = ImageTk.PhotoImage(temp_overlay)
        self.canvas.create_image(0, 0, anchor=NW, image=self.overlay_image)
        self.canvas.lift("rectangle")  # Ensure the rectangle is on top
        
