from pathlib import Path
from btnfun import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from fontTools.ttLib import TTFont
import webbrowser


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("991x587")
window.configure(bg = "#FFFFFF")


font = TTFont('fonts/Righteous-Regular.ttf')
font2 = TTFont('fonts/Janna LT Bold.ttf')

font.save
font2.save


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 587,
    width = 991,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    991.0,
    587.0,
    fill="#EFEFEF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    719.0,
    325.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    234.0,
    99.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    187.0,
    293.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    89.0,
    47.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    266.0,
    128.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    524.0,
    126.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    673.0,
    67.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    524.0,
    183.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    482.0,
    352.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    695.0,
    352.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    670.0,
    239.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    670.0,
    296.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    814.0,
    183.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    266.0,
    187.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    266.0,
    365.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    94.0,
    187.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    128.0,
    423.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    95.0,
    365.0,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    180.0,
    245.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    180.0,
    308.0,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    94.0,
    130.0,
    image=image_image_21
)

canvas.create_rectangle(
    386.0,
    391.0,
    723.0,
    565.0,
    fill="#002050",
    outline="")

canvas.create_rectangle(
    732.0,
    391.0,
    969.0,
    565.0,
    fill="#D9D9D9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_snipping_tool(window,entries2),
    relief="flat"
)
button_1.place(
    x=618.0,
    y=413.0,
    width=92.0,
    height=31.916671752929688
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    83.0,
    131.5,
    image=entry_image_1
)
entry_1 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    takefocus=0,
    highlightthickness=0
)
entry_1.place(
    x=20.0,
    y=119.0,
    width=126.0,
    height=23.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    281.5,
    132.5,
    image=entry_image_2
)
entry_2 = Entry(
    font=("Janna LT", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    takefocus=0,
    highlightthickness=0
)
entry_2.place(
    x=222.0,
    y=120.0,
    width=119.0,
    height=23.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    77.5,
    190.5,
    image=entry_image_3
)
entry_3 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    takefocus=0,
    highlightthickness=0
)
entry_3.place(
    x=15.0,
    y=178.0,
    width=125.0,
    height=23.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    283.0,
    190.5,
    image=entry_image_4
)
entry_4 = Entry(
    font=("Janna LT", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=222.0,
    y=178.0,
    width=122.0,
    height=23.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    160.5,
    245.5,
    image=entry_image_5
)
entry_5 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=15.0,
    y=233.0,
    width=291.0,
    height=23.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    199.5,
    309.5,
    image=entry_image_6
)
entry_6 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=54.0,
    y=297.0,
    width=291.0,
    height=23.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    82.5,
    367.5,
    image=entry_image_7
)
entry_7 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=20.0,
    y=355.0,
    width=125.0,
    height=23.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    249.5,
    367.5,
    image=entry_image_8
)
entry_8 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=187.0,
    y=355.0,
    width=125.0,
    height=23.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    108.5,
    426.5,
    image=entry_image_9
)
entry_9 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=16.0,
    y=414.0,
    width=185.0,
    height=23.0
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    34.0,
    97.0,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(
    413.0,
    97.0,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    673.0,
    40.0,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(
    404.0,
    156.0,
    image=image_image_25
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_26.png"))
image_26 = canvas.create_image(
    428.0,
    324.0,
    image=image_image_26
)

image_image_27 = PhotoImage(
    file=relative_to_assets("image_27.png"))
image_27 = canvas.create_image(
    624.0,
    324.0,
    image=image_image_27
)

image_image_28 = PhotoImage(
    file=relative_to_assets("image_28.png"))
image_28 = canvas.create_image(
    440.0,
    210.0,
    image=image_image_28
)

image_image_29 = PhotoImage(
    file=relative_to_assets("image_29.png"))
image_29 = canvas.create_image(
    452.0,
    267.0,
    image=image_image_29
)

image_image_30 = PhotoImage(
    file=relative_to_assets("image_30.png"))
image_30 = canvas.create_image(
    716.0,
    156.0,
    image=image_image_30
)

image_image_31 = PhotoImage(
    file=relative_to_assets("image_31.png"))
image_31 = canvas.create_image(
    69.0,
    216.0,
    image=image_image_31
)

image_image_32 = PhotoImage(
    file=relative_to_assets("image_32.png"))
image_32 = canvas.create_image(
    55.0,
    394.0,
    image=image_image_32
)

image_image_33 = PhotoImage(
    file=relative_to_assets("image_33.png"))
image_33 = canvas.create_image(
    80.0,
    277.0,
    image=image_image_33
)

image_image_34 = PhotoImage(
    file=relative_to_assets("image_34.png"))
image_34 = canvas.create_image(
    45.0,
    158.0,
    image=image_image_34
)

image_image_35 = PhotoImage(
    file=relative_to_assets("image_35.png"))
image_35 = canvas.create_image(
    37.0,
    337.0,
    image=image_image_35
)

image_image_36 = PhotoImage(
    file=relative_to_assets("image_36.png"))
image_36 = canvas.create_image(
    218.0,
    97.0,
    image=image_image_36
)

image_image_37 = PhotoImage(
    file=relative_to_assets("image_37.png"))
image_37 = canvas.create_image(
    232.0,
    158.0,
    image=image_image_37
)

image_image_38 = PhotoImage(
    file=relative_to_assets("image_38.png"))
image_38 = canvas.create_image(
    251.0,
    336.0,
    image=image_image_38
)

image_image_39 = PhotoImage(
    file=relative_to_assets("image_39.png"))
image_39 = canvas.create_image(
    597.0,
    475.0,
    image=image_image_39
)

image_image_40 = PhotoImage(
    file=relative_to_assets("image_40.png"))
image_40 = canvas.create_image(
    546.0,
    431.0,
    image=image_image_40
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: del_all(entries),
    relief="flat"
)
button_2.place(
    x=400.0,
    y=501.0,
    width=310.0,
    height=42.111114501953125
)

canvas.create_rectangle(
    676.0,
    421.0,
    704.9801635742188,
    437.1965789794922,
    fill="#FFFFFF",
    outline="")

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: save_to_sqlite(entries),
    relief="flat"
)
button_3.place(
    x=748.0,
    y=403.0,
    width=205.55905151367188,
    height=42.111114501953125
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: save_to_json(canvas,image_46,entries),
    relief="flat"
)
button_4.place(
    x=748.0,
    y=455.0,
    width=205.55905151367188,
    height=42.111114501953125
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: load_from_json(canvas,image_46,entries,window),
    relief="flat"
)
button_5.place(
    x=748.0,
    y=506.0,
    width=205.55905151367188,
    height=42.111114501953125
)


button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=15.0,
    y=516.0,
    width=330.0,
    height=42.111114501953125
)

image_image_41 = PhotoImage(
    file=relative_to_assets("image_41.png"))
image_41 = canvas.create_image(
    439.0,
    472.0,
    image=image_image_41
)

image_image_42 = PhotoImage(
    file=relative_to_assets("image_42.png"))
image_42 = canvas.create_image(
    442.0,
    430.0,
    image=image_image_42
)

canvas.create_rectangle(
    910.0,
    409.0,
    948.0,
    439.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    910.0,
    461.0,
    948.0,
    491.0,
    fill="#FFFFFF",
    outline="")

image_image_43 = PhotoImage(
    file=relative_to_assets("image_43.png"))
image_43 = canvas.create_image(
    460.0,
    47.0,
    image=image_image_43
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_19),
    relief="flat"
)
button_8.place(
    x=676.0,
    y=460.0,
    width=34.0,
    height=30.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_1),
    relief="flat"
)
button_9.place(
    x=137.0,
    y=115.0,
    width=34.0,
    height=30.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_2),
    relief="flat"
)
button_10.place(
    x=188.0,
    y=117.0,
    width=34.0,
    height=30.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_3),
    relief="flat"
)
button_11.place(
    x=137.0,
    y=172.0,
    width=34.0,
    height=30.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_4),
    relief="flat"
)
button_12.place(
    x=187.0,
    y=173.0,
    width=34.0,
    height=30.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_5),
    relief="flat"
)
button_13.place(
    x=307.0,
    y=230.0,
    width=34.0,
    height=30.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_6),
    relief="flat"
)
button_14.place(
    x=17.0,
    y=295.0,
    width=34.0,
    height=30.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_7),
    relief="flat"
)
button_15.place(
    x=141.0,
    y=350.0,
    width=34.0,
    height=30.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_8),
    relief="flat"
)
button_16.place(
    x=307.0,
    y=350.0,
    width=34.0,
    height=30.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_9),
    relief="flat"
)
button_17.place(
    x=201.0,
    y=407.0,
    width=34.0,
    height=30.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_10),
    relief="flat"
)
button_18.place(
    x=623.0,
    y=111.0,
    width=36.0,
    height=30.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_12),
    relief="flat"
)
button_19.place(
    x=622.0,
    y=166.0,
    width=36.0,
    height=30.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_14),
    relief="flat"
)
button_20.place(
    x=914.0,
    y=224.0,
    width=36.0,
    height=30.0
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_15),
    relief="flat"
)
button_21.place(
    x=916.0,
    y=280.0,
    width=36.0,
    height=30.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_16),
    relief="flat"
)
button_22.place(
    x=543.0,
    y=335.0,
    width=36.0,
    height=30.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_17),
    relief="flat"
)
button_23.place(
    x=752.0,
    y=337.0,
    width=36.0,
    height=30.0
)

canvas.create_rectangle(
    910.0,
    514.0,
    948.0,
    544.0,
    fill="#FFFFFF",
    outline="")

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    506.5,
    132.5,
    image=entry_image_10
)
entry_10 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#B0C3FF",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=388.0,
    y=120.0,
    width=237.0,
    height=23.0
)

entry_image_11 = PhotoImage(file="assets/frame0/entry_11.png")  # Update with your image path
entry_bg_11 = canvas.create_image(
    655.5,
    65.5,
    image=entry_image_11
)

# Create the autocomplete entry
entry_11 = AutocompleteEntry(
    window,
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=571.0,
    y=53.0,
    width=169.0,
    height=23.0
)
entry_11.set_completion_list(load_data_from_db())

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    506.5,
    187.5,
    image=entry_image_12
)
entry_12 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#B0C3FF",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=388.0,
    y=175.0,
    width=237.0,
    height=23.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    829.5,
    188.5,
    image=entry_image_13
)
entry_13 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#B0C3FF",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=711.0,
    y=176.0,
    width=237.0,
    height=23.0
)


button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: fill_data(canvas,image_46,entries,window),
    relief="flat"
)
button_6.place(
    x=15.0,
    y=462.0,
    width=330.0,
    height=42.111114501953125
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    648.5,
    242.5,
    image=entry_image_14
)
entry_14 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#B0C3FF",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=387.0,
    y=230.0,
    width=523.0,
    height=23.0
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    648.5,
    299.5,
    image=entry_image_15
)
entry_15 = Entry(
    font=("Janna LT", 15 * -1),
    bd=0,
    bg="#B0C3FF",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=387.0,
    y=287.0,
    width=523.0,
    height=23.0
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    468.0,
    358.5,
    image=entry_image_16
)
entry_16 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#B0C3FF",
    fg="#000716",
    highlightthickness=0
)
entry_16.place(
    x=391.0,
    y=346.0,
    width=154.0,
    height=23.0
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    679.0,
    358.5,
    image=entry_image_17
)
entry_17 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#B0C3FF",
    fg="#000716",
    highlightthickness=0
)
entry_17.place(
    x=602.0,
    y=346.0,
    width=154.0,
    height=23.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_16),
    relief="flat"
)
button_24.place(
    x=678.0,
    y=171.0,
    width=36.0,
    height=30.0
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    546.5,
    432.5,
    image=entry_image_18
)
entry_18 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_18.place(
    x=484.0,
    y=420.0,
    width=125.0,
    height=23.0
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    581.5,
    475.5,
    image=entry_image_19
)
entry_19 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_19.place(
    x=485.0,
    y=463.0,
    width=193.0,
    height=23.0
)
entries = [entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, entry_7, entry_8, entry_9, entry_10, entry_11, entry_12, entry_13, entry_14, entry_15, entry_16, entry_17]
entries2 = [entry_18 ,entry_19]

image_image_44 = PhotoImage(
    file=relative_to_assets("image_44.png"))
image_44 = canvas.create_image(
    816.0,
    126.0,
    image=image_image_44
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copyentry(window,entry_20),
    relief="flat"
)
button_25.place(
    x=678.0,
    y=111.0,
    width=36.0,
    height=30.0
)

entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(
    834.5,
    130.5,
    image=entry_image_20
)
entry_20 = Entry(
    font=("Righteous", 15 * -1),
    bd=0,
    bg="#B0C3FF",
    fg="#000716",
    highlightthickness=0
)
entry_20.place(
    x=716.0,
    y=118.0,
    width=237.0,
    height=23.0
)


image_image_45 = PhotoImage(
    file=relative_to_assets("image_45.png"))
image_45 = canvas.create_image(
    727.0,
    97.0,
    image=image_image_45
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open('https://github.com/AyoubSghuri/CNIX-v2.0'),
    relief="flat"
)
button_26.place(
    x=822.0,
    y=18.0,
    width=147.0,
    height=51.0
)

image_image_46 = PhotoImage(
    file=relative_to_assets("image_46.png"))
image_46 = canvas.create_image(
    947.0,
    357.0,
    image=image_image_46,
    state='hidden'
)

button_image_27 = PhotoImage(
    file=relative_to_assets("button_27.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: fill_data_from_db(entries, entry_11.get()),
    relief="flat"
)
button_27.place(
    x=740.0,
    y=53.0,
    width=38.0,
    height=30.0
)
window.resizable(False, False)
window.mainloop()
