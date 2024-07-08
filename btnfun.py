from extract import PersonCID
from tkinter import filedialog, Tk, Entry, Button,Toplevel ,messagebox,Label,END,Listbox
from pprint import pprint
import arabic_reshaper
import numpy as np
from snip import SnipImage
import time , re , cv2
import clipboard
import sqlite3
from PIL import Image, ImageTk
from notification import Notification
import threading
from bidi.algorithm import get_display
# from snip import Snip # Ensure 'start' is imported correctly from 'snip'

personcid = PersonCID()


def toggle_image_visibility(canvas, item_id, duration, interval,window):
    # Toggle the visibility of the specified image every interval for the duration
    end_time = window.after(duration, lambda: canvas.itemconfig(item_id, state='hidden'))

    def blink():
        current_state = canvas.itemcget(item_id, 'state')
        new_state = 'normal' if current_state == 'hidden' else 'hidden'
        canvas.itemconfig(item_id, state=new_state)

        # Check if the end time has passed
        scheduled_tasks = window.tk.call('after', 'info')
        if any(str(end_time) == str(task[0]) for task in scheduled_tasks):
            window.after(interval, blink)

    blink()

class AutocompleteEntry(Entry):
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self._completion_list = []
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.listbox = None
        self.bind('<KeyRelease>', self.handle_keyrelease)
        self.bind('<FocusOut>', self.hide_listbox)

    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list)
        self._hits = []
        self._hit_index = 0
        self.position = 0

    def autocomplete(self):
        text = self.get()
        if text == '':
            self._hits = []
        else:
            self._hits = [item for item in self._completion_list if item.lower().startswith(text.lower())]
        self.update_listbox(self._hits)

    def handle_keyrelease(self, event):
        if event.keysym in ('BackSpace', 'Left', 'Right', 'Up', 'Down', 'Return'):
            return
        self.autocomplete()

    def update_listbox(self, hits):
        if self.listbox:
            self.listbox.destroy()
        if hits:
            self.listbox = Listbox(self.master)
            self.listbox.bind('<<ListboxSelect>>', self.on_listbox_select)
            self.listbox.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
            for item in hits:
                self.listbox.insert(END, item)

    def on_listbox_select(self, event):
        if self.listbox:
            self.delete(0, END)
            self.insert(0, self.listbox.get(self.listbox.curselection()))
            self.listbox.destroy()
            self.listbox = None

    def hide_listbox(self, event):
        if self.listbox:
            self.listbox.destroy()
            self.listbox = None
  
def load_data_from_db():
    conn = sqlite3.connect("dataCID.db")
    cursor = conn.cursor()
    cursor.execute("SELECT cin FROM persons")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]      

def fill_data_from_db(entries, cin):
    conn = sqlite3.connect("dataCID.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM persons WHERE cin = ?", (cin,))
    person = cursor.fetchone()
    conn.close()

    if person:
        entries_dict = {
            entries[0]: person[0],  # nom
            entries[1]: person[1],  # nom Ar
            entries[2]: person[2],  # prenom
            entries[3]: person[3],  # prenom Ar
            entries[4]: person[6],  # adresse front
            entries[6]: person[10], # CINE
            entries[7]: person[9],  # Expire date
            entries[8]: person[8],  # Date birth
            entries[9]: person[12], # father name
            entries[11]: person[13],# mother name
            entries[13]: person[14],# adresse in french (Back)
            entries[14]:person[7], # adresse back in ar
            entries[15]: person[5], # etatCivil number
            entries[16]: person[4], # sexe
        }

        for entry, value in entries_dict.items():
            entry.delete(0, END)
            entry.insert(0, value)
   
def fill_data(canvas,image_46,entries,window):
    path_img = filedialog.askopenfilename(filetypes=[("Image File", '.jpg .png')])
    if not path_img:
        return  # If no file is selected, exit the function

    personcid.filterData(path_img)

    entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, entry_7, entry_8, entry_9, entry_10, entry_11, entry_12, entry_13, entry_14, entry_15, entry_16, entry_17 = entries

    entries_dict = {
        entry_1: personcid.nom,  # nom
        entry_2: personcid.nomAr,  # nom Ar
        entry_3: personcid.prenom,  # prenom
        entry_4: personcid.prenomAr,  # prenom Ar
        entry_5: personcid.adresseFront,  # adresse front
        entry_7: personcid.cin,  # CINE
        entry_8: personcid.dateExpCID,  # Expire date
        entry_9: personcid.dateNaiss,  # Date birth
        entry_10: personcid.fatherName,  # father name
        # entry 11 search
        entry_12: personcid.motherName,  # mother name
        # entry 13 mother name in arabic
        entry_14: personcid.adresseBack,  # adresse in french (Back)
        # enrty_15 adresse ar back
        entry_16: personcid.etatCivil,  # etatCivil number
        entry_17: personcid.sexe,  # sexe
        # entry 18 number length
        #entry 19 number found in snip
        # entry 20 father name in arabic
    }

    # Fill entries with data
    for entry, value in entries_dict.items():
        entry.delete(0, 'end')
        if value is not None:
            entry.insert(0, value)

    # Handle Arabic address separately
    entry_15.delete(0, 'end')
    if personcid.adresseAr is not None:
        reshaped_text = arabic_reshaper.reshape(personcid.adresseAr)
        bidi_text = get_display(reshaped_text)
        entry_15.insert(0, bidi_text)
    toggle_image_visibility(canvas, image_46, 1000, 500,window)
    # Print the properties of personcid for debugging purposes
    pprint(vars(personcid))

def del_all(entries):
    personcid.reset()

    # Clear all entry fields
    for entry in entries:
        entry.delete(0, 'end')

def save_to_json(entries):
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filename:
        personcid.save_as_json(entries,filename)

def load_from_json(canvas,image_46,entries,window):
    global personcid
    filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, entry_7, entry_8, entry_9, entry_10, entry_11, entry_12, entry_13, entry_14, entry_15, entry_16, entry_17 = entries

    if filename:
        personcid = PersonCID.load_from_json(filename)
        entries_dict = {
            entry_1: personcid.nom,  # nom
            entry_2: personcid.nomAr,  # nom Ar
            entry_3: personcid.prenom,  # prenom
            entry_4: personcid.prenomAr,  # prenom Ar
            entry_5: personcid.adresseFront,  # adresse front
            entry_7: personcid.cin,  # CINE
            entry_8: personcid.dateExpCID,  # Expire date
            entry_9: personcid.dateNaiss,  # Date birth
            entry_10: personcid.fatherName,  # father name
            # entry 11 search
            entry_12: personcid.motherName,  # mother name
            entry_14: personcid.adresseBack,  # adresse in french (Back)
            entry_16: personcid.etatCivil,  # etatCivil number
            entry_17: personcid.sexe,  # sexe
        }

        for entry, value in entries_dict.items():
            entry.delete(0, 'end')
            if value is not None:
                entry.insert(0, value)
        toggle_image_visibility(canvas, image_46, 1000, 500,window)


def save_to_sqlite(entries):
    global personcid
    personcid.save_to_sqlite(entries,"dataCID.db")

def copyentry(window,entry):
    im = Image.open("assets/frame0/image_46.png")
    im = im.resize((25, 45), Image.Resampling.LANCZOS)
    im = ImageTk.PhotoImage(im)

    cim = Image.open("assets/close1.png")
    cim = cim.resize((25, 45), Image.Resampling.LANCZOS)
    cim = ImageTk.PhotoImage(cim)

    img_pad = (5, 0)
    text_pad = (5, 0)
    if entry.get():
        clipboard.copy(entry.get())
        
        notification = Notification(
                master=window,
                width=300,
                height=50,
                bg="white",
                image=im,
                font=("Righteous", 15 * -1),
                text="Copied successfully",
                close_img=cim,
                img_pad=(10, 10),
                text_pad=(10, 10),
                y_pos=8
            )
        notification.show_animation()
    else:
        notification = Notification(
                master=window,
                width=300,
                height=50,
                bg="white",
                image=cim,
                text="This entry is empty",
                close_img=cim,
                img_pad=(10, 10),
                text_pad=(10, 10),
                font=("Righteous", 15 * -1),
                y_pos=8
            )
        notification.show_animation()






def snipping_tool_thread(window, entries2):
    entry_18, entry_19 = entries2
    if not entry_18.get():
        messagebox.showwarning("Input Error", "Number length cannot be empty.")
        return

    window.iconify()  # Minimize the main window
    time.sleep(0.6)
    print("this : " + entry_18.get() + " and this : " + entry_19.get())
    lenNum = re.compile(f"^[0-9]{{{entry_18.get()}}}$")
    snipping_tool = Toplevel(window)
    snipping_tool.attributes('-fullscreen', True)


    snip_instance = SnipImage(snipping_tool)
    snip_instance.startsnip()
    start_time = time.time()

    def check_destroy():
        if not snipping_tool.winfo_exists():  # Check if an image has been captured
            if snip_instance.get_captured_image():
                end_time = time.time()  # End timing
                duration = end_time - start_time  # Calculate duration
                print(f"Snipping tool window destroyed, restoring main window. Time taken: {duration:.2f} seconds")
                window.deiconify()  # Restore the main window
                captured_image = snip_instance.get_captured_image()
                
                # Convert captured image to OpenCV format
                captured_image_np = np.array(captured_image)
                captured_image_cv = cv2.cvtColor(captured_image_np, cv2.COLOR_RGB2BGR)
                
                text = personcid.dataTextEng(captured_image_cv)
                print(text)
                found_match = False
                for i in text:
                    if lenNum.match(i):
                        print(i)
                        entry_19.insert(0, i)
                        found_match = True
                        break
                if not found_match:
                    messagebox.showwarning("window", "No matching number found in the captured image.")
            else:
                pass
        else:
            try:
                time.sleep(0.3)  # Sleep for a while before checking again
                check_destroy()
            except Exception as e:
                print(f"{e}")
                window.deiconify()
                end_time = time.time()  # End timing
                duration = end_time - start_time
                print(f"time it took {duration}")

    check_destroy()  # Start checking for destruction

def open_snipping_tool(window, entries2):
    threading.Thread(target=snipping_tool_thread, args=(window, entries2,)).start()


# def show_toast(parent, message):
#     toast = Toast(parent, message)