from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
      def __init__(self,root):
            self.root=root
            self.root.geometry("1350x700+0+0")
            self.root.title("Billing Software")
            bg_color="#074463"
            title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",20,"bold"),pady=2).pack(fill=X)
#=============variables==========================
#=============Cosmetic===========================
            self.soap=IntVar()
            self.face_cream=IntVar()
            self.face_wash=IntVar()
            self.sampoo=IntVar()
            self.body_lotion=IntVar()
            self.hair_gel=IntVar()
#=============grocery=============================
            self.rice=IntVar()
            self.food_oil=IntVar()
            self.wheat=IntVar()
            self.dal=IntVar()
            self.sugar=IntVar()
            self.tea=IntVar()
#==============cold drinks=======================
            self.mazza=IntVar()
            self.thums_up=IntVar()
            self.frooti=IntVar()
            self.thums_up_char=IntVar()
            self.limca=IntVar()
            self.sprite=IntVar()
#=============Total Product Price===============
            self.cosmetic_price=StringVar()
            self.grocery_price=StringVar()
            self.cold_drink_price=StringVar()

            self.cosmetic_tax=StringVar()
            self.grocery_tax=StringVar()
            self.cold_drink_tax=StringVar()

#================Customer=======================
            self.c_name=StringVar()
            self.c_phone=StringVar()
            
            self.bill_no=StringVar()
            x=random.randint(1000,9999)          
            self.bill_no.set(str(x))
            
            self.search_bill=StringVar()

#=============costomer detail frame==============
            F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Costomer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
            F1.place(x=0,y=80,relwidth=1)
            
            cname_lbl=Label(F1,text="Costomer name",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
            cname_txt=Entry(F1,width=20,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

            cphn_lbl=Label(F1,text="Phone No",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
            cphn_txt=Entry(F1,width=20,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

            c_bill_lbl=Label(F1,text="Bill Number",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
            c_bill_txt=Entry(F1,width=20,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

            
            # bill_btn=Button(F1,text="search",command=self.find_bill,width=8,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=5,pady=10)
            total_btn=Button(F1,text="search",command=self.total,width=8,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=5,pady=10)
#===========Cosmetic Frame========================
            
            F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
            F2.place(x=5,y=180,width=340,height=380)

            bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
            bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

            fcr_lbl=Label(F2,text="Face Cream",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
            fcr_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

            fwh_lbl=Label(F2,text="Face Wash",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
            fwh_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

            smp_lbl=Label(F2,text="Sampoo",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
            smp_txt=Entry(F2,width=10,textvariable=self.sampoo,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

            bls_lbl=Label(F2,text="Body Loshan",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
            bls_txt=Entry(F2,width=10,textvariable=self.body_lotion,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

            hgl_lbl=Label(F2,text="Hair Gel",font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
            hgl_txt=Entry(F2,width=10,textvariable=self.hair_gel,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)


#============Grocery Frame========================
            
            F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
            F3.place(x=340,y=180,width=340,height=380)

            rice_lbl=Label(F3,text="Rice",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
            rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

            foil_lbl=Label(F3,text="Food Oil",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
            foil_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

            wht_lbl=Label(F3,text="wheat",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
            wht_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

            dal_lbl=Label(F3,text="Dal",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
            dal_txt=Entry(F3,width=10,textvariable=self.dal,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

            sgr_lbl=Label(F3,text="Sugar",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
            sgr_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

            tea_lbl=Label(F3,text="Tea",font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
            tea_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

#===========Cosmetic Frame========================                                                                         
            F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
            F4.place(x=680,y=180,width=340,height=380)

            maza_lbl=Label(F4,text="Mazza",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
            maza_txt=Entry(F4,width=10,textvariable=self.mazza,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

            thb_lbl=Label(F4,text="Thums Up",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
            thb_txt=Entry(F4,width=10,textvariable=self.thums_up,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

            frt_lbl=Label(F4,text="Frooti",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
            frt_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

            thbc_lbl=Label(F4,text="Thums Up Char.",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
            thbc_txt=Entry(F4,width=10,textvariable=self.thums_up_char,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

            lmc_lbl=Label(F4,text="Limca",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
            lmc_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

            sprt_lbl=Label(F4,text="sprite",font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
            sprt_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

#===========Bill area==============================
            F5=Frame(self.root,bd=10,relief=GROOVE)
            F5.place(x=1020,y=180,width=340,height=380)
            bil_title=Label(F5,text="Bill Area",bd=8,relief=GROOVE,fg="black",font=("times new roman",15,"bold"),pady=2).pack(fill=X)
            scrol_y=Scrollbar(F5,orient=VERTICAL)
            self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
            scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=self.txtarea.yview)
            self.txtarea.pack(fill=BOTH,expand=1)
#============Button Frame=================================
            
            F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
            F6.place(x=0,y=560,relwidth=1,height=140)

            m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
            m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

            m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
            m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

            m3_lbl=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
            m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

            m4_lbl=Label(F6,text="Cosmetic Tex",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
            m4_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

            m5_lbl=Label(F6,text="Grocery Tex",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
            m5_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

            m6_lbl=Label(F6,text="Cold Drinks tex",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
            m6_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

            btn_f=Frame(F6,bd=7,relief=GROOVE)
            btn_f.place(x=750,width=580,height=105)

            tolal_btn=Button(btn_f,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,width=9,font="arial 15 bold",bd=5).grid(row=0,column=0,padx=5,pady=5)

            Gbil_btn=Button(btn_f,text="Genrate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,width=9,font="arial 15 bold",bd=5).grid(row=0,column=1,padx=5,pady=5)

            Clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=15,width=9,font="arial 15 bold",bd=5).grid(row=0,column=2,padx=5,pady=5)

            Exit_btn=Button(btn_f,text="Exit",command=self.exit_app,bg="cadetblue",fg="white",pady=15,width=9,font="arial 15 bold",bd=5).grid(row=0,column=3,padx=5,pady=5)
            
            self.welcome_bill()

            
      def total(self):
#======================cosmetic===============================      
            self.c_s_p=self.soap.get()*20
            self.c_fc_p=self.face_cream.get()*80
            self.c_fw_p=self.face_wash.get()*120
            self.c_smp_p=self.sampoo.get()*120
            self.c_bl_p=self.body_lotion.get()*60
            self.c_hg_p=self.hair_gel.get()*80

            self.total_cosmetic_price=float(
                                                                            self.c_s_p+
                                                                            self.c_fc_p+
                                                                            self.c_fw_p+
                                                                            self.c_smp_p+
                                                                            self.c_bl_p+
                                                                            self.c_hg_p
                                                                          )
            self.cosmetic_price.set("Rs.   "+str(self.total_cosmetic_price))
            self.c_tax=round((self.total_cosmetic_price*0.05),2)
            self.cosmetic_tax.set("Rs.   "+str(self.c_tax))

#=======================grocery======================================

            self.g_rc_p=self.rice.get()*80
            self.g_fo_p=self.food_oil.get()*200
            self.g_wht_p=self.wheat.get()*60
            self.g_dl_p=self.dal.get()*100
            self.g_sgr_p=self.sugar.get()*60
            self.g_tea_p=self.tea.get()*110


            self.total_grocery_price=float(
                                                                            self.g_rc_p+
                                                                            self.g_fo_p+
                                                                            self.g_wht_p+
                                                                            self.g_dl_p+
                                                                            self.g_sgr_p+
                                                                            self.g_tea_p
                                                                   )
            self.grocery_price.set("Rs.   "+str(self.total_grocery_price))
            self.g_tax=round((self.total_grocery_price*0.1),2)
            self.grocery_tax.set("Rs.   "+str(self.g_tax))


#======================cold drinks===========================================

            self.cd_mz_p=self.mazza.get()*90
            self.cd_thu_p=self.thums_up.get()*90
            self.cd_frt_p=self.frooti.get()*120
            self.cd_thuc_p=self.thums_up_char.get()*90
            self.cd_lmc_p=self.limca.get()*80
            self.cd_spt_p=self.sprite.get()*90  


            self.total_cold_drinks_price=float(
                                                                            self.cd_mz_p+
                                                                            self.cd_thu_p+
                                                                            self.cd_frt_p+
                                                                            self.cd_thuc_p+
                                                                            self.cd_lmc_p+
                                                                            self.cd_spt_p
                                                                              )
            self.cold_drink_price.set("Rs.   "+str(self.total_cold_drinks_price))
            self.cd_tax=round((self.total_cold_drinks_price*0.05),2)
            self.cold_drink_tax.set("Rs.   "+str(self.cd_tax))
            
#---------------TOTAL BILL-------------------------------------

            self.Total_bill=float(self.total_cosmetic_price+
                                  self.total_grocery_price+
                                  self.total_cold_drinks_price+
                                  self.c_tax+
                                  self.g_tax+
                                  self.cd_tax
                                  )

#======================================welcome bill===================================            


      def welcome_bill(self):
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\tWelcome pbhut shop\n")
            self.txtarea.insert(END,f"\n  Bill Number   :  {self.bill_no.get()}")
            self.txtarea.insert(END,f"\n  Costomer Name   :  {self.c_name.get()}")
            self.txtarea.insert(END,f"\n  Phone Number    :  {self.c_phone.get()}")
            self.txtarea.insert(END,f"\n=====================================")
            self.txtarea.insert(END,f"\nProducts\t\tQTY\t\tPrice")
            self.txtarea.insert(END,f"\n=====================================")
#==========================bill area=========================================================
      def bill_area(self):
        self.welcome_bill()
        
        total_cosmetics = self.total_cosmetic_price
        total_groceries = self.total_grocery_price
        total_cold_drinks = self.total_cold_drinks_price
    
        cosmetics_tax = total_cosmetics * 0.05
        groceries_tax = total_groceries * 0.05
        cold_drinks_tax = total_cold_drinks * 0.05
        
        if self.soap.get() != 0:
            self.txtarea.insert(END,f"\nBath Soap         {self.soap.get()}           {self.soap.get() * 20}")
        if self.face_cream.get() != 0:
            self.txtarea.insert(END,f"\nFace Cream        {self.face_cream.get()}           {self.face_cream.get() * 80}")
        if self.face_wash.get() != 0:
            self.txtarea.insert(END,f"\nFace Wash         {self.face_wash.get()}           {self.face_wash.get() * 120}")
        if self.sampoo.get() != 0:
            self.txtarea.insert(END,f"\nSampoo        {self.sampoo.get()}           {self.sampoo.get() * 120}")
        if self.hair_gel.get() != 0:
            self.txtarea.insert(END,f"\nHair Gel        {self.hair_gel.get()}           {self.hair_gel.get() * 60}")
        if self.body_lotion.get() != 0 :
            self.txtarea.insert(END,f"\nBody Lotion       {self.body_lotion.get()}           {self.body_lotion.get() * 60}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END,f"\nWheat             {self.wheat.get()}           {self.wheat.get() * 60}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END,f"\nFood Oil          {self.food_oil.get()}           {self.food_oil.get() * 200}")
        if self.dal.get() != 0:
            self.txtarea.insert(END,f"\nDal              {self.dal.get()}           {self.dal.get() * 100}")
        if self.rice.get() != 0:
            self.txtarea.insert(END,f"\nRice              {self.rice.get()}           {self.rice.get() * 80}")
        if self.sugar.get() != 0:
            self.txtarea.insert(END,f"\nSugar             {self.sugar.get()}           {self.sugar.get() * 60}")
        if self.tea.get() != 0:
            self.txtarea.insert(END,f"\nTea             {self.tea.get()}           {self.tea.get() * 110}")
        if self.mazza.get() != 0:
            self.txtarea.insert(END,f"\nMazza              {self.mazza.get()}           {self.mazza.get() * 90}")
        if self.frooti.get() != 0:
            self.txtarea.insert(END,f"\nFrooti            {self.frooti.get()}           {self.frooti.get() * 120}")
        if self.thums_up.get() != 0:
            self.txtarea.insert(END,f"\nThums up              {self.thums_up.get()}           {self.thums_up.get() * 90}")
        if self.thums_up_char.get() != 0:
            self.txtarea.insert(END,f"\nThums up charged     {self.thums_up_char.get()}           {self.thums_up_char.get() * 90}")
        if self.sprite.get() != 0:
            self.txtarea.insert(END,f"\nSprite          {self.sprite.get()}           {self.sprite.get() * 90}")
        if self.limca.get() != 0:
            self.txtarea.insert(END,f"\nLimca          {self.limca.get()}           {self.limca.get() * 80}")
        self.txtarea.insert(END,"\n===================================")
        
        self.txtarea.insert(END,"\n===================================")
        self.txtarea.insert(END,f"\nSubtotal - Cosmetics: {total_cosmetics}")
        self.txtarea.insert(END,f"\nSubtotal - Groceries: {total_groceries}")
        self.txtarea.insert(END,f"\nSubtotal - Cold Drinks: {total_cold_drinks}")
        
        self.txtarea.insert(END,"\n===================================")
        
        self.txtarea.insert(END,f"\nTaxes - Cosmetics: {cosmetics_tax}")
        self.txtarea.insert(END,f"\nTaxes - Groceries: {groceries_tax}")
        self.txtarea.insert(END,f"\nTaxes - Cold Drinks: {cold_drinks_tax}")
        
        self.txtarea.insert(END,"\n===================================")
        
        self.txtarea.insert(END,f"\n                      Total : {self.total_cosmetic_price+self.total_grocery_price+self.total_cold_drinks_price+self.total_cosmetic_price * 0.05+self.total_grocery_price * 0.05+self.total_cold_drinks_price * 0.05}")
        self.save_bill_to_file()

      def clear_data(self):
        self.txtarea.delete('1.0',END)

      def save_bill_to_file(self):
            # Open a file in write the bill details
            bill_content = self.txtarea.get("1.0", "end-1c")
            with open(f'D:/python/bills/{self.bill_no.get()}.txt', 'w+') as file:
                  file.write(bill_content)
                  print('file saved sucssesfully')
                  file.close()

      def exit_app(self):
            op=messagebox.askyesno("exit","Do You Want To Exit?")
            if op>0:
                  self.root.destroy()
root=Tk()
obj = Bill_App(root)
root.mainloop()
