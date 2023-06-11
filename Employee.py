from tkinter import*

class EmployeeSystem:
    def __init__(self,root):
        self.root =root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title= Label(self.root, text="Employee Paroll Management system", font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w").place(x=0,y=0,relwidth=1)
        #===== Frame1==================
        Frame1=Frame(self.root,bd=3,relief=RIDGE)
        Frame1.place(x=10,y=70,width=750,height=620)
        
        title2= Label(Frame1, text="Employee Details", font=("times new roman",20,"bold"),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1) 
        lbl_code=Label(Frame1, text="Employee Code", font=("times new roman",20),fg="black",anchor="w").place(x=10,y=70)
        txt_code= Entry(Frame1, font=("times new roman",15),bg="lightyellow",fg="black").place(x=220,y=74,width=200)
        btn_search=Button (Frame1,text="Search", font=("times new roman",15),bg="green",fg="black").place(x=440,y=72,height=30)
        #=========Row 1=============
        lbl_designation=Label(Frame1, text="Designation", font=("times new roman",20),fg="black").place(x=10,y=120)
        txt_designation= Entry(Frame1, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=125,width=200)
        lbl_dob=Label(Frame1, text="D.O.B", font=("times new roman",20),fg="black").place(x=390,y=120)
        txt_dob= Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=125)
 
         #=========Row 2============
        lbl_Name=Label(Frame1, text="Name", font=("times new roman",20),fg="black").place(x=10,y=170)
        txt_Name= Entry(Frame1, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=175,width=200)
        lbl_doj=Label(Frame1, text="D.O.J", font=("times new roman",20),fg="black").place(x=390,y=170)
        txt_doj= Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=175)
        
         #=========Row 3=============
        lbl_age=Label(Frame1, text="Age", font=("times new roman",20),fg="black").place(x=10,y=220)
        txt_age= Entry(Frame1, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=225,width=200)
        lbl_experience=Label(Frame1, text="Experience", font=("times new roman",20),fg="black").place(x=390,y=220)
        txt_experience= Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=225)
        
          #=========Row4=============
        lbl_gender=Label(Frame1, text="Gender", font=("times new roman",20),fg="black").place(x=10,y=270)
        txt_gender= Entry(Frame1, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=275,width=200)
        lbl_CCCD=Label(Frame1, text="CCCD", font=("times new roman",20),fg="black").place(x=390,y=270)
        txt_CCCD= Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=275)
        
          #=========Row 5=============
        lbl_email=Label(Frame1, text="Email", font=("times new roman",20),fg="black").place(x=10,y=320)
        txt_email= Entry(Frame1, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=325,width=200)
        lbl_contact=Label(Frame1, text="Contact", font=("times new roman",20),fg="black").place(x=390,y=320)
        txt_contact= Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=325)
        
          #=========Row 6=============
        lbl_age=Label(Frame1, text="Age", font=("times new roman",20),fg="black").place(x=10,y=220)
        txt_age= Entry(Frame1, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=225,width=200)
        lbl_experience=Label(Frame1, text="Experience", font=("times new roman",20),fg="black").place(x=390,y=220)
        txt_experience= Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=225)
        
          #=========Row 6=============
        lbl_hired=Label(Frame1, text="Hired Location", font=("times new roman",18),fg="black").place(x=10,y=370)
        txt_hired= Entry(Frame1, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=375,width=200)
        lbl_status=Label(Frame1, text="Status", font=("times new roman",20),fg="black").place(x=390,y=370)
        txt_status= Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=375)
        
                  #=========Row 7=============
        lbl_address=Label(Frame1, text="Address", font=("times new roman",18),fg="black").place(x=10,y=422)
        txt_address= Text(Frame1, font=("times new roman",15),bg="lightyellow",fg="black")
        txt_address.place(x=170,y=425,width=550,height=150)
        
          #===== Frame2==================
        Frame2=Frame(self.root,bd=3,relief=RIDGE)
        Frame2.place(x=770,y=70,width=580,height=350)
        
        title2= Label(Frame2, text="Employee Salary Details", font=("times new roman",20,"bold"),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1) 
        lbl_month=Label(Frame2, text="Month", font=("times new roman",18),fg="black").place(x=10,y=60)
        txt_month= Entry(Frame2, font=("times new roman",15),bg="lightyellow",fg="black").place(x=100,y=62,width=100)
        
        
        lbl_year=Label(Frame2, text="Year", font=("times new roman",18),fg="black").place(x=210,y=60)
        txt_year= Entry(Frame2, font=("times new roman",15),bg="lightyellow",fg="black").place(x=270,y=62,width=100)
        
        lbl_salary=Label(Frame2, text="Salary", font=("times new roman",18),fg="black").place(x=380,y=60)
        txt_salary= Entry(Frame2, font=("times new roman",15),bg="lightyellow",fg="black").place(x=460,y=62,width=100)
        
        #=========Row 1=============
        lbl_days=Label(Frame2, text="Total Days", font=("times new roman",18),fg="black").place(x=10,y=120)
        txt_days= Entry(Frame2, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=125,width=120)
        lbl_absent= Label(Frame2,text="Absents",font=("times new roman",18),fg="black").place(x=300,y=120)
        txt_absent= Entry(Frame2, font=("times new roman",15),bg="lightyellow",fg="black").place(x=420,y=125,width=120 )
        
         
        #=========Row 2=============
        lbl_medical=Label(Frame2, text="Medical", font=("times new roman",18),fg="black").place(x=10,y=150)
        txt_medical= Entry(Frame2, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=155,width=120)
        lbl_pf= Label(Frame2,text="PF",font=("times new roman",18),fg="black").place(x=300,y=150)
        txt_pf= Entry(Frame2, font=("times new roman",15),bg="lightyellow",fg="black").place(x=420,y=155,width=120 )
        
        #=========Row 3=============
        lbl_convence=Label(Frame2, text="Conveyance", font=("times new roman",18),fg="black").place(x=10,y=180)
        txt_convence= Entry(Frame2, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=185,width=120)
        lbl_netsalary= Label(Frame2,text="Net Salary",font=("times new roman",18),fg="black").place(x=300,y=180)
        txt_netsalary= Entry(Frame2, font=("times new roman",15),bg="lightyellow",fg="black").place(x=420,y=185,width=120 )
        
        btn_calculate=Button (Frame2,text="Calculate", font=("times new roman",15),bg="green",fg="black").place(x=150,y=240,height=30,width=120)
        btn_save=Button (Frame2,text="Save", font=("times new roman",15),bg="orange",fg="black").place(x=285,y=240,height=30,width=120)
        btn_clear=Button (Frame2,text="Clear", font=("times new roman",15),bg="red",fg="black").place(x=420,y=240,height=30,width=120)
        
        #=====Frame 3===================
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380,width=580,height=310)
        #=========Calculate Frame===============
        self.var_txt =StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
        
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
               
            
        Cal_Frame=Frame(Frame3,bg="white",bd=3,relief=RIDGE)
        Cal_Frame.place(x=2,y=2,width=247,height=300)
        txt_Result= Entry(Cal_Frame,textvariable=self.var_txt,bg="lightyellow", font=("times new roman",20)).place(x=0,y=0,relwidth=1,height=40)
        #=============Row1============
        btn_7=Button(Cal_Frame,text="7",command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=0,y=42,width=60,height=60)
        btn_8=Button(Cal_Frame,text="8",command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=61,y=42,width=60,height=60)
        btn_9=Button(Cal_Frame,text="9",command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=122,y=42,width=60,height=60)
        btn_div=Button(Cal_Frame,text="/",command=lambda:btn_click('/'),font=("times new roman",15,"bold")).place(x=183,y=42,width=60,height=60)
        
        #=============Row 2============
        btn_4=Button(Cal_Frame,text="4",command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=0,y=102,width=60,height=60)
        btn_5=Button(Cal_Frame,text="5",command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=61,y=102,width=60,height=60)
        btn_6=Button(Cal_Frame,text="6",command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=122,y=102,width=60,height=60)
        btn_mul=Button(Cal_Frame,text="*",command=lambda:btn_click('*'),font=("times new roman",15,"bold")).place(x=183,y=102,width=60,height=60)                                              
       
        #=============Row 3===============
        btn_1=Button(Cal_Frame,text="1",command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=0,y=162,width=60,height=60)
        btn_2=Button(Cal_Frame,text="2",command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=61,y=162,width=60,height=60)
        btn_3=Button(Cal_Frame,text="3",command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=122,y=162,width=60,height=60)
        btn_min=Button(Cal_Frame,text="-",command=lambda:btn_click('-'),font=("times new roman",15,"bold")).place(x=183,y=162,width=60,height=60)
        
        #=============Row4==============
        btn_0=Button(Cal_Frame,text="0",command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=0,y=222,width=60,height=60)
        btn_dot=Button(Cal_Frame,text=".",command=lambda:btn_click('.'),font=("times new roman",15,"bold")).place(x=61,y=222,width=60,height=60)
        btn_sum=Button(Cal_Frame,text="+",command=lambda:btn_click('+'),font=("times new roman",15,"bold")).place(x=122,y=222,width=60,height=60)
        btn_equal=Button(Cal_Frame,text="=",command=result,font=("times new roman",15,"bold")).place(x=183,y=222,width=60,height=60)
        
root=Tk()
obj=EmployeeSystem(root)
root.mainloop()
