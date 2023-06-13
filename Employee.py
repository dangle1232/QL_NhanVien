from tkinter import*
from tkinter import messagebox, ttk
import pymysql #pip install pymysql
import time
import tempfile
import os
class EmployeeSystem:
    def __init__(self,root):
        self.root =root
        self.root.title("Quản Lý Tiền Lương Nhân Viên")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title= Label(self.root, text="Quản Lý Tiền Lương Nhân Viên", font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w").place(x=0,y=0,relwidth=1)
        btn_show_emp=Button (self.root,text="All Employees",command=self.employee_frame, font=("times new roman",13),bg="gray",fg="white").place(x=1100,y=10,height=30,width=120)
        #===== Frame1==================
        #========Variables=========
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_exp=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_cccd=StringVar()
        self.var_contact=StringVar()
        self.var_status=StringVar()
        self.var_supp=StringVar()
        
        Frame1=Frame(self.root,bd=3,relief=RIDGE)
        Frame1.place(x=10,y=70,width=750,height=620)
        
        title2= Label(Frame1, text="Chi Tiết Nhân Viên", font=("times new roman",20,"bold"),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1) 
        lbl_code=Label(Frame1, text="Mã Nhân Viên", font=("times new roman",20),fg="black",anchor="w").place(x=10,y=70)
        self.txt_code= Entry(Frame1, textvariable=self.var_emp_code,font=("times new roman",15),bg="lightyellow",fg="black")
        self.txt_code.place(x=220,y=74,width=200)
        btn_search=Button (Frame1,command=self.Search,text="Search", font=("times new roman",15),bg="green",fg="black").place(x=440,y=72,height=30)
        #=========Row 1=============
        lbl_designation=Label(Frame1, text="Chuyên Môn", font=("times new roman",18),fg="black").place(x=10,y=120)
        txt_designation= Entry(Frame1,  textvariable=self.var_designation,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=125,width=200)
        lbl_dob=Label(Frame1, text="Ngày Sinh", font=("times new roman",18),fg="black").place(x=390,y=120)
        txt_dob= Entry(Frame1, textvariable=self.var_dob,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=125)
 
         #=========Row 2============
        lbl_Name=Label(Frame1, text="Họ Tên", font=("times new roman",18),fg="black").place(x=10,y=170)
        txt_Name= Entry(Frame1, textvariable=self.var_name, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=175,width=200)
        lbl_doj=Label(Frame1, text="Ngày Làm", font=("times new roman",18),fg="black").place(x=390,y=170)
        txt_doj= Entry(Frame1, textvariable=self.var_doj,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=175)
        
         #=========Row 3=============
        lbl_age=Label(Frame1,text="Tuổi", font=("times new roman",18),fg="black").place(x=10,y=220)
        txt_age= Entry(Frame1,textvariable=self.var_age, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=225,width=200)
        lbl_experience=Label(Frame1, text="Kinh Nghiệm", font=("times new roman",18),fg="black").place(x=390,y=220)
        txt_experience= Entry(Frame1,textvariable=self.var_exp,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=225)
        
          #=========Row4=============
        lbl_gender=Label(Frame1, text="Giới Tính", font=("times new roman",18),fg="black").place(x=10,y=270)
        txt_gender= Entry(Frame1, textvariable=self.var_gender,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=275,width=200)
        lbl_CCCD=Label(Frame1, text="Mã CCCD", font=("times new roman",18),fg="black").place(x=390,y=270)
        txt_CCCD= Entry(Frame1,textvariable=self.var_cccd,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=275)
        
          #=========Row 5=============
        lbl_email=Label(Frame1, text="Email", font=("times new roman",18),fg="black").place(x=10,y=320)
        txt_email= Entry(Frame1,textvariable=self.var_email, font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=325,width=200)
        lbl_contact=Label(Frame1, text="Liên Hệ", font=("times new roman",18),fg="black").place(x=390,y=320)
        txt_contact= Entry(Frame1,textvariable=self.var_contact,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=325)
          #=========Row 6=============
        lbl_hired=Label(Frame1, text="Nơi Làm Việc", font=("times new roman",18),fg="black").place(x=10,y=370)
        txt_hired= Entry(Frame1, textvariable=self.var_hr_location,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=375,width=200)
        lbl_status=Label(Frame1, text="Vị Trí", font=("times new roman",18),fg="black").place(x=390,y=370)
        txt_status= Entry(Frame1,textvariable=self.var_status,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=375)
        
                  #=========Row 7=============
        lbl_address=Label(Frame1, text="Địa Chỉ", font=("times new roman",18),fg="black").place(x=10,y=422)
        self.txt_address= Text(Frame1,font=("times new roman",15),bg="lightyellow",fg="black")
        self.txt_address.place(x=170,y=425,width=550,height=150)
        
          #===== Frame2==================
          #========Variables=========
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_t_days=StringVar()
        self.var_absent=StringVar()
        self.var_supp=StringVar()
        self.var_net_salary=StringVar()
        
        Frame2=Frame(self.root,bd=3,relief=RIDGE)
        Frame2.place(x=770,y=70,width=580,height=350)
        
        title2= Label(Frame2, text="Bảng Lương Nhân Viên", font=("times new roman",20,"bold"),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1) 
        lbl_month=Label(Frame2, text="Tháng", font=("times new roman",18),fg="black").place(x=10,y=60)
        txt_month= Entry(Frame2,textvariable=self.var_month, font=("times new roman",15),bg="lightyellow",fg="black").place(x=100,y=62,width=100)
        
        
        lbl_year=Label(Frame2, text="Năm", font=("times new roman",18),fg="black").place(x=210,y=60)
        txt_year= Entry(Frame2, textvariable=self.var_year,font=("times new roman",15),bg="lightyellow",fg="black").place(x=270,y=62,width=100)
        
        lbl_salary=Label(Frame2, text="Lương", font=("times new roman",18),fg="black").place(x=380,y=60)
        txt_salary= Entry(Frame2, textvariable=self.var_salary,font=("times new roman",15),bg="lightyellow",fg="black").place(x=460,y=62,width=100)
        
        #=========Row 1=============
        lbl_days=Label(Frame2, text="Tổng Ngày", font=("times new roman",18),fg="black").place(x=10,y=120)
        txt_days= Entry(Frame2, textvariable=self.var_t_days,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=125,width=120)
        lbl_absent= Label(Frame2,text="Ngày Nghỉ",font=("times new roman",18),fg="black").place(x=300,y=120)
        txt_absent= Entry(Frame2, textvariable=self.var_absent,font=("times new roman",15),bg="lightyellow",fg="black").place(x=420,y=125,width=120 )  
        #=========Row 3=============
        lbl_supp=Label(Frame2, text="Phụ Cấp", font=("times new roman",18),fg="black").place(x=10,y=180)
        txt_supp= Entry(Frame2,  textvariable=self.var_supp,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=185,width=120)
        lbl_netsalary= Label(Frame2,text="Tổng Lương",font=("times new roman",18),fg="black").place(x=300,y=180)
        txt_netsalary= Entry(Frame2,  textvariable=self.var_net_salary, font=("times new roman",15),bg="lightyellow",fg="black").place(x=420,y=185,width=120 )
        
        btn_calculate=Button (Frame2,command=self.calculate,text="Calculate", font=("times new roman",15),bg="green",fg="black").place(x=150,y=225,height=30,width=120)
        self.btn_save=Button (Frame2,command=self.add,text="Save", font=("times new roman",15),bg="orange",fg="black")
        self.btn_save.place(x=285,y=225,height=30,width=120)
        btn_clear=Button (Frame2,command=self.clear,text="Clear", font=("times new roman",15),bg="red",fg="black").place(x=420,y=225,height=30,width=120) 
        
        
        self.btn_update=Button (Frame2,command=self.update,state=DISABLED,text="Update", font=("times new roman",15),bg="gray",fg="black")
        self.btn_update.place(x=150,y=260,height=30,width=180)
        self.btn_delete=Button (Frame2,command=self.Delete,text="Delete", state=DISABLED,font=("times new roman",15),bg="yellow",fg="black")
        self.btn_delete.place(x=340,y=260,height=30,width=200)
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
        def clear_all():
          self.var_txt.set('')
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
        btn_dot=Button(Cal_Frame,text="C",command=clear_all,font=("times new roman",15,"bold")).place(x=61,y=222,width=60,height=60)
        btn_sum=Button(Cal_Frame,text="+",command=lambda:btn_click('+'),font=("times new roman",15,"bold")).place(x=122,y=222,width=60,height=60)
        btn_equal=Button(Cal_Frame,text="=",command=result,font=("times new roman",15,"bold")).place(x=183,y=222,width=60,height=60)
        
        #=============Salary=========
        sal_Frame= Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_Frame.place(x=250,y=2,width=320,height=300)
        title_sal= Label(sal_Frame, text="Biên Lai Lương", font=("times new roman",18,"bold"),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1) 
        sal_Frame2= Frame(sal_Frame,bg="white",bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=230)
        self.sample=f'''\tCompany Name, XYZ\n\tAddress:Xyz, Floor 4
-----------------------------------------
Employee ID\t\t:
Salary Of\t\t: Mon-YYYY
Generated On\t\t:DD-MM-YYYY
-----------------------------------------
Total Days\t\t:DD
Total Present\t\t:DD
Total Absent\t\t:DD
Convence\t\t :
Medical\t\t: 
PF\t\t:
Gross Payment\t\t: 
Net Salary\t\t:
-----------------------------------------
This is computer generated slip, not
required any signature
'''
        scroll_y= Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)
        
        self.txt_salary_receipt=Text(sal_Frame2,font=("times new roman",13),bg="lightyellow",yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END,self.sample)
        self.btn_print=Button (sal_Frame,command=self.print,state=DISABLED,text="Print", font=("times new roman",20),bg="lightblue",fg="black")
        self.btn_print.place(x=180,y=262,height=30,width=120)
        
        self.check_connection( )
        
    #===================== All functions start here===========   
    def Search(self):
       try:
            con = pymysql.connect(host='localhost', user='root', password='', db='ems')
            cur = con.cursor()
            cur.execute("SELECT * FROM emp_salary WHERE e_id=%s", (self.var_emp_code.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Mã nhân viên không tồn tại, hãy thử lại",
                                     parent=self.root)
            else:
                
                self.var_emp_code.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hr_location.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_exp.set(row[9])
                self.var_cccd.set(row[10])
                self.var_contact.set(row[11])
                self.var_status.set(row[12])
                self.txt_address.delete('1.0', END)
                self.txt_address.insert( END,row[13])
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_salary.set(row[16])
                self.var_t_days.set(row[17])
                self.var_absent.set(row[18])
                self.var_supp.set(row[19])
                self.var_net_salary.set(row[20])
                file_ = open('Salary_reciept/'+str(row[21]),'r')
                self.txt_salary_receipt.delete('1.0',END)
                for i in file_:
                  self.txt_salary_receipt.insert(END,i)
                file_.close()  
                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_code.config(state="readonly")
                self.btn_print.config(state=NORMAL)
                
       except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}")
            
    def clear(self):
                self.btn_save.config(state=NORMAL)
                self.btn_update.config(state=DISABLED)
                self.btn_delete.config(state=DISABLED)
                self.txt_code.config(state=NORMAL)
                self.btn_print.config(state=DISABLED )
                self.var_emp_code.set("")
                self.var_designation.set("")
                self.var_name.set("")
                self.var_age.set("")
                self.var_gender.set("")
                self.var_email.set("")
                self.var_hr_location.set("")
                self.var_doj.set("")
                self.var_dob.set("")
                self.var_exp.set("")
                self.var_cccd.set("")
                self.var_contact.set("")
                self.var_status.set("")
                self.txt_address.delete('1.0', END)
                self.var_month.set("")
                self.var_year.set("")
                self.var_salary.set("")
                self.var_t_days.set("")
                self.var_absent.set("") 
                self.var_supp.set("")
                self.var_net_salary.set("")
                self.txt_salary_receipt.delete('1.0',END)
                self.txt_salary_receipt.insert(END,self.sample)
    def Delete(self):
      if self.var_emp_code.get()=='':
        messagebox.showerror("Error","Mã nhân viên không được trống")
      else:
        
        try:
              con = pymysql.connect(host='localhost', user='root', password='', db='ems')
              cur = con.cursor()
              cur.execute("Select * FROM emp_salary WHERE e_id=%s", (self.var_emp_code.get()))
              row = cur.fetchone()
              if row == None:
                  messagebox.showerror("Error", "Mã nhân viên không hợp lệ, hãy thử lại",
                                      parent=self.root)
              else:
                op=messagebox.askyesno("Confirm","Bạn có muốn xoá ?")
                if op==True:
                  cur.execute("delete from emp_salary where e_id=%s",(self.var_emp_code.get()))
                  con.commit()
                  con.close()
                  messagebox.showinfo("Delete", "Xoá thành công",
                                      parent=self.root)
                  self.clear()
        except Exception as ex:
              messagebox.showerror("Error", f"Error occurred: {str(ex)}")       
                  
    def add(self):
     if self.var_emp_code.get() == '' or self.var_net_salary.get() == '' or self.var_name.get() == '':
        messagebox.showerror("Error", "Chi tiết nhân viên không được trống")
     else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='ems')
            cur = con.cursor()
            cur.execute("SELECT * FROM emp_salary WHERE e_id=%s", (self.var_emp_code.get()))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Mã nhân viên đã tồn, hãy thử lại",
                                     parent=self.root)
            else:
                cur.execute("INSERT INTO emp_salary VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                    self.var_emp_code.get(),
                    self.var_designation.get(),
                    self.var_name.get(),
                    self.var_age.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_hr_location.get(),
                    self.var_doj.get(),
                    self.var_dob.get(),
                    self.var_exp.get(),
                    self.var_cccd.get(),
                    self.var_contact.get(),
                    self.var_status.get(),
                    self.txt_address.get('1.0', END),
                    self.var_month.get(),
                    self.var_year.get(),
                    self.var_salary.get(),
                    self.var_t_days.get(),
                    self.var_absent.get(),
                    self.var_supp.get(),
                    self.var_net_salary.get(),
                    self.var_emp_code.get()+".txt"
                   
                    )
                    )

                con.commit()
                con.close()
                file_ = open('Salary_reciept/'+str(self.var_emp_code.get())+".txt",'w')
                file_.write (self.txt_salary_receipt.get('1.0',END))
                file_.close()
                messagebox.showinfo("Success", "Thêm thành công")
                self.btn_print.config(state=NORMAL)
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}")

    
    def calculate(self):
      if self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='' or self.var_t_days.get()=='' or self.var_absent.get()=='' or self.var_supp.get()=='' :
        messagebox.showerror("Error","vui lòng nhập đủ thông tin") 
      else:
        per_day=int(self.var_salary.get())/int(self.var_t_days.get()) 
        work_day=int(self.var_t_days.get())-int(self.var_absent.get())
        sal=per_day *work_day
        addition=int(self.var_supp.get())
        net_sal=sal+addition
        self.var_net_salary.set(str(round(net_sal,2)))  
        #========================Update the reciept   
        sample=f'''\tCompany Name, XYZ\n\tAddress:Xyz, Floor 4
-----------------------------------------
Mã Nhân viên\t\t: {self.var_emp_code.get()}
Lương tháng\t\t: {self.var_month.get()}-{self.var_year.get()}
Được tạo\t\t: {str(time.strftime("%d-%M-%Y"))}
-----------------------------------------
Tổng Ngày\t\t:{self.var_t_days.get()}
Ngày Thực\t\t:{str(int(self.var_t_days.get())-int(self.var_absent.get()))}
Ngày Nghỉ\t\t: {self.var_absent.get()}
Phụ Cấp\t\t :Rs.{self.var_supp.get()}
Lương Cứng\t\t: Rs.{self.var_salary.get()}
Tổng Lương\t\t:Rs.{self.var_net_salary.get()}
-----------------------------------------
 Good Job
'''
      self.txt_salary_receipt.delete('1.0',END)
      self.txt_salary_receipt.insert(END,sample)
        
    def check_connection(self):
      try:
        con= pymysql.connect(host='localhost',user='root',password='',db='ems')
        cur=con.cursor()
        cur.execute("Select * from emp_salary")
        rows= cur.fetchall()
        #print(rows)
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to:{str(ex)}")
    
    def show(self):
      try:
        con= pymysql.connect(host='localhost',user='root',password='',db='ems')
        cur=con.cursor()
        cur.execute("Select * from emp_salary")
        rows= cur.fetchall()
        #print(rows)
        self.employee_tree.delete(*self.employee_tree.get_children())
        for row in rows:
          self.employee_tree.insert('',END,values=row)
        con.close()
      except Exception as ex:
        messagebox.showerror("Error",f"Error due to:{str(ex)}")
        
    def update(self):
     if self.var_emp_code.get() == '' or self.var_net_salary.get() == '' or self.var_name.get() == '':
        messagebox.showerror("Error", "Vui lòng nhập đủ thông tin")
     else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='ems')
            cur = con.cursor()
            cur.execute("SELECT * FROM emp_salary WHERE e_id=%s", (self.var_emp_code.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Mã nhân viên không hợp lệ, hãy thử lại",
                                     parent=self.root)
            else:
                cur.execute("UPDATE `emp_salary` SET `desigation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hr_location`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`cccd`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`t_days`=%s,`absent_days`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s,`salary_receipt`=%s WHERE  `e_id`=%s",
                    (
                    
                    self.var_designation.get(),
                    self.var_name.get(),
                    self.var_age.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_hr_location.get(),
                    self.var_doj.get(),
                    self.var_dob.get(),
                    self.var_exp.get(),
                    self.var_cccd.get(),
                    self.var_contact.get(),
                    self.var_status.get(),
                    self.txt_address.get('1.0', END),
                    self.var_month.get(),
                    self.var_year.get(),
                    self.var_salary.get(),
                    self.var_t_days.get(),
                    self.var_absent.get(),
                    self.var_supp.get(),
                    self.var_net_salary.get(),
                    self.var_emp_code.get()+".txt",
                    self.var_emp_code.get()
                   
                    )
                    )

                con.commit()
                con.close()
                file_ = open('Salary_reciept/'+str(self.var_emp_code.get())+".txt",'w')
                file_.write (self.txt_salary_receipt.get('1.0',END))
                file_.close()
                messagebox.showinfo("Success", "Cập nhật thành công")
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}")
      
    def employee_frame(self):
        self.root2 =Toplevel(self.root)
        self.root2.title("Danh Sách Nhân viên")
        self.root2.geometry("1000x500+120+100")
        self.root.config(bg="white")
        title= Label(self.root, text="Tất cả nhân viên", font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w").pack(side=TOP,fill=X)
        self.root2.focus_force()
        
        scrolly= Scrollbar(self.root2,orient=VERTICAL)
        scrollx = Scrollbar(self.root2,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'desigation', 'name', 'age', 'gender', 'email', 'hr_location', 'doj', 'dob', 'experience', 'cccd', 'contact', 'status', 'address', 'month', 'year', 'basic_salary', 't_days', 'absent_days',  'supp', 'net_salary', 'salary_receipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id',text="ID")
        self.employee_tree.heading('desigation',text="Chuyên Môn")
        self.employee_tree.heading('name',text="Tên")
        self.employee_tree.heading('age',text="Tuổi")
        self.employee_tree.heading('gender',text="Giới Tính")
        self.employee_tree.heading('email',text="Email")
        self.employee_tree.heading('hr_location',text="Nơi làm việc")
        self.employee_tree.heading('doj',text="Ngày làm")
        self.employee_tree.heading('dob',text="Ngày sinh")
        self.employee_tree.heading('experience',text="Kinh nghiệm")
        self.employee_tree.heading('cccd',text="CCCD")
        self.employee_tree.heading('contact',text="Liên hệ")
        self.employee_tree.heading('status',text="Vị trí")
        self.employee_tree.heading('address',text="Địa chỉ")
        self.employee_tree.heading('month',text="Tháng")
        self.employee_tree.heading('year',text="Năm")
        self.employee_tree.heading('basic_salary',text="Lương cứng")
        self.employee_tree.heading('t_days',text="Tổng ngày")
        self.employee_tree.heading('absent_days',text="Ngày nghỉ")
        self.employee_tree.heading('supp',text="Phụ cấp")
        self.employee_tree.heading('net_salary',text="Tổng lương")
        self.employee_tree.heading('salary_receipt',text="Biên lai")
        self.employee_tree['show']='headings'
        
        self.employee_tree.column('e_id',width=100)
        self.employee_tree.column('desigation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_location',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('cccd',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=500)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('t_days',width=100)
        self.employee_tree.column('absent_days',width=100)
        self.employee_tree.column('supp',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_receipt',width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1) 
        self.show()
        self.root2.mainloop()
        
    def print(self):
      
      file_=tempfile.mkstemp(".txt")
      open(file_,'w').write(self.txt_salary_receipt.get('1.0',END))
      os.startfile(file_,'print')
        
root=Tk()
obj=EmployeeSystem(root)
root.mainloop()
