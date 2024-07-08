from tkinter import Label ,Button,Frame  
from PIL import Image, ImageTk

class Notification(Frame):
    def __init__(self, master, width, height, bg, image, text, close_img, img_pad, text_pad, font, y_pos):
        super().__init__(master, bg=bg, width=width, height=height)
        self.pack_propagate(0)

        self.y_pos = y_pos

        self.master = master
        self.width = width

        right_offset = 8

        self.cur_x = self.master.winfo_width()
        self.x = self.cur_x - (self.width + right_offset)

        img_label = Label(self, image=image, bg=bg)
        img_label.image = image
        img_label.pack(side="left", padx=img_pad[0])

        message = Label(self, text=text, font=font, bg=bg, fg="black")
        message.pack(side="left", padx=text_pad[0])

        close_btn = Button(self, image=close_img, bg=bg, relief="flat", command=self.hide_animation, cursor="hand2")
        close_btn.image = close_img
        close_btn.pack(side="right", padx=5)

        self.place(x=self.cur_x, y=y_pos)

    def show_animation(self):
        if self.cur_x > self.x:
            self.cur_x -= 1
            self.place(x=self.cur_x, y=self.y_pos)
            self.after(1, self.show_animation)
        else:
            self.after(800, self.hide_animation)  # Wait for 3 seconds before hiding the notification

    def hide_animation(self):
        if self.cur_x < self.master.winfo_width():
            self.cur_x += 1
            self.place(x=self.cur_x, y=self.y_pos)
            self.after(1, self.hide_animation)