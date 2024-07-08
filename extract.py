import cv2
import pytesseract
import numpy as np
import time
import re
import json
import sqlite3
from tkinter import messagebox
from concurrent.futures import ThreadPoolExecutor

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
face_cascade = cv2.CascadeClassifier("xml/haarcascade_frontalface_alt2.xml")

class PersonCID:
    def __init__(self, nom=None, nomAr=None, prenom=None, prenomAr=None, sexe=None, etatCivil=None, adresse=None, adresseAr=None, dateNaiss=None, dateExpCID=None, cin=None, numPhone=None, fatherName=None, motherName=None, adresseBack=None):
        self.nom = nom
        self.nomAr = nomAr
        self.prenom = prenom
        self.prenomAr = prenomAr
        self.sexe = sexe
        self.dateNaiss = dateNaiss
        self.dateExpCID = dateExpCID
        self.etatCivil = etatCivil
        self.adresseFront = adresse
        self.adresseAr = adresseAr
        self.cin = cin
        self.numPhone = numPhone
        self.fatherName = fatherName
        self.motherName = motherName
        self.adresseBack = adresseBack

    @staticmethod
    def checkFrontOrBack(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        return True if len(faces) else False

    @staticmethod
    def dataText(img,threshN):
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh_fr = cv2.threshold(img_gray, threshN, 255, cv2.THRESH_BINARY_INV)[1]
        txt_fr = pytesseract.image_to_string(thresh_fr, lang='fra', config='--psm 11')
        thresh_ar = cv2.threshold(img_gray, threshN, 255, cv2.THRESH_BINARY_INV)[1]
        txt_ar = pytesseract.image_to_string(thresh_ar, lang='ara', config='--psm 11')
        # cv2.imshow('image window', thresh_fr)
        # cv2.imshow('image window', thresh_fr)        
        # cv2.imshow('image window ar', thresh_ar)

        # cv2.waitKey(0)
        return txt_fr.split('\n'), txt_ar.split('\n')
    
    @staticmethod
    def dataTextEng(img_array):
        # img_gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        # thresh_img = cv2.threshold(img_gray, 160, 255, cv2.THRESH_BINARY_INV)[1]
        # cv2.imshow('image window', img_array)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        custom_config = r'--oem 3 --psm 11 -c tessedit_char_whitelist=0123456789'
        txt_Num = pytesseract.image_to_string(img_array, config=custom_config)
        return txt_Num.split('\n')

    def reset(self):
        self.nom = self.nomAr = self.prenom = self.prenomAr = self.sexe = self.dateNaiss = self.dateExpCID = self.etatCivil = self.adresseFront = self.adresseAr = self.cin = self.numPhone = None

    @staticmethod
    def fullNameAr(img):
        (h, w) = img.shape[:2]
        (cX, cY) = (w // 2, h // 2)
        topRight = img[0:cY, cX:w]
        thresh_ar = cv2.threshold(topRight, 129, 255, cv2.THRESH_BINARY_INV)[1]
        txt_ar = pytesseract.image_to_string(thresh_ar, lang='ara', config='--psm 11')
        return txt_ar.split("\n")

    def filterData(self, imgPath):
        start_time = time.time()
        img = cv2.imread(imgPath)
        is_front = self.checkFrontOrBack(img)
        print(is_front)
        
        if is_front:
            regex_patterns = {
                "fullname": re.compile("^[A-Z]{3,}$"),
                "cin": re.compile("^[A-Z]+[0-9]+$"),
                "address_front": re.compile("^à\s([A-Z]+\s*){2,}$"),
                "date": re.compile("^[0-9]{2}\.[0-9]{2}\.[0-9]{4}$"),
                "full_ar": re.compile("^(عبد)*\s*[ء-ي]+$")
            }
            
            lst_ar = self.fullNameAr(img)
            threshN = 136
            lst, lst_ar_text = self.dataText(img,threshN)
            
            for i in lst_ar:
                if regex_patterns["full_ar"].match(i):
                    if self.prenomAr is None:
                        self.prenomAr = i
                    else:
                        self.nomAr = i
            
            for i in lst:
                if regex_patterns["fullname"].match(i):
                    if self.prenom is None:
                        self.prenom = i
                    else:
                        self.nom = i
            
            for i in lst:
                if regex_patterns["cin"].match(i):
                    self.cin = i
                    break

            for i in lst:
                if regex_patterns["address_front"].match(i):
                    self.adresseFront = i
                    break

            for i in lst:
                if regex_patterns["date"].match(i):
                    if self.dateNaiss is None:
                        self.dateNaiss = i
                    else:
                        self.dateExpCID = i
        else:
            regex_patterns = {
                "adresse_ar": re.compile("العنوان\s([ء-ي]+\s*){2,}[0-9]+\s+([ء-ي]+\s*)*"),
                "sexe": re.compile("^(F|M)$"),
                "etat_civil": re.compile("^[0-9]+\/+[0-9]+$"),
                "ben": re.compile("[A-ZÇ]+ ben [A-ZÇ]+"),
                "bent": re.compile("[a-z]*\s*[A-Z]+\sbent\s[A-Z]+"),
                "adresse_back": re.compile("Adresse(\s*[a-zA-Z]+\s+)+[0-9]+(\s*[a-zA-Z]+\s*)*")
            }
            threshN = 130
            lst, lst_ar_text = self.dataText(img,threshN)

            for i in lst:
                if regex_patterns["sexe"].match(i):
                    self.sexe = "Homme" if i == "M" else "Femme"
                    break

            for i in lst_ar_text:
                if regex_patterns["adresse_ar"].match(i):
                    self.adresseAr = i
                    break

            for i in lst:
                if regex_patterns["adresse_back"].match(i):
                    prefix = "Adresse "
                    if i.startswith(prefix):
                        i = i[len(prefix):]
                    self.adresseBack = i
                    break

            for i in lst:
                if regex_patterns["etat_civil"].match(i):
                    self.etatCivil = i
                    break

            for i in lst:
                if regex_patterns["ben"].match(i):
                    self.fatherName = i
                    break

            for i in lst:
                if regex_patterns["bent"].match(i):
                    prefix = "etde "
                    if i.startswith(prefix):
                        i = i[len(prefix):]
                    self.motherName = i
                    break
        tiimesum= []
        tiimesum.append(time.time() - start_time)
        
        print(time.time() - start_time)
        
    def save_as_json(self,entries, filename):
        data = {
            'nom': entries[0].get(),
            'nomAr': entries[1].get(),
            'prenom': entries[2].get(),
            'prenomAr': entries[3].get(),
            'sexe': entries[16].get(),
            'etatCivil': entries[15].get(),
            'adresse': entries[4].get(),
            'adresseAr': entries[14].get(),
            'dateNaiss': entries[8].get(),
            'dateExpCID': entries[7].get(),
            'cin': entries[6].get(),
            'numPhone': entries[10].get(),
            'fatherName': entries[9].get(),
            'motherName': entries[11].get(),
            'adresseBack': entries[13].get()
        }
        if self.cin:    
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        else:
            tkinter.messagebox.ERROR = 'error'
        print(f"Data saved as JSON to {filename}")

    @classmethod
    def load_from_json(cls,filename):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            instance = cls()
        for key, value in data.items():
            setattr(instance, key, value)
            print(key , value)
        print(instance)
        return instance
        # return PersonCID(**data)
        
    def save_to_sqlite(self,entries, db_filename):
        if not self.cin:
            messagebox.showerror("Error", "CIN cannot be empty.")
            return

        conn = sqlite3.connect(db_filename)
        c = conn.cursor()
        
        # Create table if not exists
        c.execute('''CREATE TABLE IF NOT EXISTS persons
                     (nom TEXT, nomAr TEXT, prenom TEXT, prenomAr TEXT,
                      sexe TEXT, etatCivil TEXT, adresse TEXT, adresseAr TEXT,
                      dateNaiss TEXT, dateExpCID TEXT, cin TEXT NOT NULL UNIQUE, numPhone TEXT,
                      fatherName TEXT, motherName TEXT, adresseBack TEXT)''')

        # Check if data already exists based on unique identifier (cin in this case)
        c.execute('SELECT * FROM persons WHERE cin=?', (entries[6].get(),))
        existing_data = c.fetchone()

        if existing_data:
            messagebox.showwarning("Data Exists", f"Data with CIN {entries[6].get()} already exists. Not inserting.")
        else:
            # Insert data into table
            data_tuple = (
                entries[0].get(),  # nom
                entries[1].get(),  # nomAr
                entries[2].get(),  # prenom
                entries[3].get(),  # prenomAr
                entries[16].get(),  # sexe
                entries[15].get(),  # etatCivil
                entries[4].get(),  # adresse
                entries[14].get(),  # adresseAr
                entries[8].get(),  # dateNaiss
                entries[7].get(),  # dateExpCID
                entries[6].get(),  # cin
                entries[10].get(),  # numPhone
                entries[9].get(),  # fatherName
                entries[11].get(),  # motherName
                entries[13].get(),  # adresseBack
            )
            
            c.execute('INSERT INTO persons VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', data_tuple)
            conn.commit()
            messagebox.showinfo("Data Saved", f"Data saved to SQLite database: {db_filename}")

        conn.close()
# # Example usage
# img_path = 'path_to_your_image.jpg'
# person_cid = PersonCID()
# person_cid.filterData(img_path)
