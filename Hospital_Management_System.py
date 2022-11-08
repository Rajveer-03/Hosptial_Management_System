from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        lbtitle = Label(self.root, bd = 20, relief= RIDGE, text = "Hospital Management System", fg = "red", bg = "White",font=("times new roman",50,"bold")) 
        lbtitle.pack(side = TOP, fill=X)

        # ----------------making the data frame----------------

        Dataframe = Frame(self.root, bd = 20, relief = RIDGE)
        Dataframe.place(x=0,y= 130, width = 1530, height = 400)

        DataFrameLeft = LabelFrame(Dataframe, bd = 10, padx = 20, relief = RIDGE, font=("arial",12,"bold"),text = "Patient Information")
        DataFrameLeft.place(x = 0, y = 5, width = 980, height = 350)

        DataFrameRight = LabelFrame(Dataframe, bd = 10, padx = 20, relief = RIDGE, font=("arial",12,"bold"),text = "Prescription")
        DataFrameRight.place(x = 990, y = 5, width = 460, height = 350)

        # ----------------making the Buttons frame----------------
        Buttonframe = Frame(self.root, bd = 20, relief = RIDGE)
        Buttonframe.place(x=0, y= 530, width = 1530, height = 70)

        # ----------------making the Details frame----------------
        Detailsframe = Frame(self.root, bd = 20, relief = RIDGE)
        Detailsframe.place(x=0, y= 600, width = 1530, height = 190)

        lblNameTablet = Label(DataFrameLeft, text = "Name of tablet", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblNameTablet.grid(row = 0, column = 0)

        comNametablet = ttk.Combobox(DataFrameLeft, font = ("times new roman", 12, "bold"), width = 33)

        comNametablet["values"] = ("Paracetamol", "Crocine", "Norflox", "Adderall", "Activian", "Amlodipine", "Combiflame", "Dollo")
        comNametablet.grid(row = 0, column = 1)

        lblref = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Reference No: ", padx = 2)
        lblref.grid(row = 1, column = 0, sticky = W)
        txtref = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtref.grid(row = 1, column = 1)

        lbldose = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Dose: ", padx = 2, pady = 6)
        lbldose.grid(row = 2, column = 0, sticky = W)
        txtdose = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtdose.grid(row = 2, column = 1)

        lblNoOftablets = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "No. of Tablets: ", padx = 2, pady = 6)
        lblNoOftablets.grid(row = 3, column = 0, sticky = W)
        txtNoOftablets = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtNoOftablets.grid(row = 3, column = 1)

        lbllot = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Lot: ", padx = 2, pady = 6)
        lbllot.grid(row = 4, column = 0, sticky = W)
        txtlot = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtlot.grid(row = 4, column = 1)

        lblissue = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Issue Date: ", padx = 2, pady = 6)
        lblissue.grid(row = 5, column = 0, sticky = W)
        txtissue = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtissue.grid(row = 5, column = 1)

        lblExp = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Exp Date: ", padx = 2, pady = 6)
        lblExp.grid(row = 6, column = 0, sticky = W)
        txtExp = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtExp.grid(row = 6, column = 1)

        lbldaily = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Daily dose: ", padx = 2, pady = 6)
        lbldaily.grid(row = 7, column = 0, sticky = W)
        txtdaily = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtdaily.grid(row = 7, column = 1)

        lblside = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Side effect: ", padx = 2, pady = 6)
        lblside.grid(row = 8, column = 0, sticky = W)
        txtside = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtside.grid(row = 8, column = 1)

        lblinfo = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Further Information: ", padx = 2, pady = 6)
        lblinfo.grid(row = 0, column = 2, sticky = E)
        txtinfo = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtinfo.grid(row = 0, column = 3)

        lblpressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Blood Pressure: ", padx = 2, pady = 6)
        lblpressure.grid(row = 1, column = 2, sticky = E)
        txtpressure = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtpressure.grid(row = 1, column = 3)

        lblpressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Storage Advice: ", padx = 2, pady = 6)
        lblpressure.grid(row = 2, column = 2, sticky = E)
        txtpressure = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtpressure.grid(row = 2, column = 3)

        lblpressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Medication: ", padx = 2, pady = 6)
        lblpressure.grid(row = 3, column = 2, sticky = E)
        txtpressure = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtpressure.grid(row = 3, column = 3)

        lblpressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Patient ID: ", padx = 2, pady = 6)
        lblpressure.grid(row = 4, column = 2, sticky = E)
        txtpressure = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtpressure.grid(row = 4, column = 3)

        lblpressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "NHS number: ", padx = 2, pady = 4)
        lblpressure.grid(row = 5, column = 2, sticky = E)
        txtpressure = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtpressure.grid(row = 5, column = 3)

        lblpressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Patient Name: ", padx = 2, pady = 4)
        lblpressure.grid(row = 6, column = 2, sticky = E)
        txtpressure = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtpressure.grid(row = 6, column = 3)

        lblpressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Date of Birth: ", padx = 2, pady = 4)
        lblpressure.grid(row = 7, column = 2, sticky = E)
        txtpressure = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtpressure.grid(row = 7, column = 3)

        lblpressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Patient Address: ", padx = 2, pady = 6)
        lblpressure.grid(row = 8, column = 2, sticky = E)
        txtpressure = Entry(DataFrameLeft, font = ("arial", 13, "bold"), width = 35)
        txtpressure.grid(row = 8, column = 3)
        

root = Tk()
ob = Hospital(root)
root.mainloop()



    
