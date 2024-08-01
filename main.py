from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#0A7CFF")
        self.root.title("Resturent Billing System - CodeWithCurious.com")
        title=Label(self.root,text="Resturent Billing System",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)
        #===================================variables=======================================================================================
        self.nutella=IntVar()
        self.noodles=IntVar()
        self.lays=IntVar()
        self.oreo=IntVar()
        self.muffin=IntVar()
        self.silk=IntVar()
        self.namkeen=IntVar()
        self.atta=IntVar()
        self.pasta=IntVar()
        self.rice=IntVar()
        self.oil=IntVar()
        self.sugar=IntVar()
        self.dal=IntVar()
        self.tea=IntVar()
        self.soap=IntVar()
        self.shampoo=IntVar()
        self.lotion=IntVar()
        self.cream=IntVar()
        self.foam=IntVar()
        self.mask=IntVar()
        self.sanitizer=IntVar()
        self.total_sna=StringVar()
        self.total_gro=StringVar()
        self.total_hyg=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
               #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=0,padx=15)

        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)

        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=2,padx=10)

        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)

        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=4,padx=10)

        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #=======================================Resturant Menu=================================================================
        snacks=LabelFrame(self.root,text="Starter",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        snacks.place(x=5,y=180,height=380,width=325)

        item1=Label(snacks,text="Samosa",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.nutella).grid(row=0,column=1,padx=10)

        item2=Label(snacks,text="Paneer Tikka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.noodles).grid(row=1,column=1,padx=10)

        item3=Label(snacks,text="Chicken Tikka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.lays).grid(row=2,column=1,padx=10)

        item4=Label(snacks,text="Vegetable Pakora",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.oreo).grid(row=3,column=1,padx=10)

        item5=Label(snacks,text="Papdi Chaat",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.muffin).grid(row=4,column=1,padx=10)

        item6=Label(snacks,text="Tomato Soup",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.silk).grid(row=5,column=1,padx=10)

        item7=Label(snacks,text="Masala Papad",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.namkeen).grid(row=6,column=1,padx=10)
        #=================================== Main Course =====================================================================================
        grocery=LabelFrame(self.root,text="Main Course",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        grocery.place(x=340,y=180,height=380,width=325)

        item8=Label(grocery,text="Butter Chicken",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.atta).grid(row=0,column=1,padx=10)

        item9=Label(grocery,text="Pasta",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.pasta).grid(row=1,column=1,padx=10)

        item10=Label(grocery,text="Basmathi Rice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.rice).grid(row=2,column=1,padx=10)

        item11=Label(grocery,text="Paneer Masala",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.oil).grid(row=3,column=1,padx=10)
