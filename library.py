from tkinter import *
from tkinter import ttk
#import mysql.connector

class LibraryManagementSystem:


    def __init__(self,window):
        self.window = window
        self.window.title("Library Management System")
        self.window.geometry("1550x800+0+0")


       # db= mysql.connector.connect(host="localhost", user="root", password="Software@259",database="library_management_system")




        self.member_var = StringVar()
        self.prn_no_var = StringVar()
        self.ID_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.mobile_var = StringVar()
        self.email_id_var = StringVar()
        self.book_id_var = StringVar()
        self.book_title_var = StringVar()
        self.author_name_var = StringVar()
        self.date_borrowed_var = StringVar()
        self.date_due_var = StringVar()
        self.days_on_book_var = StringVar()
        self.late_rtn_fine_var = StringVar()
        self.date_over_due_var = StringVar()
        self.actual_price_var = StringVar()






        lbltitle=Label(self.window,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="brown",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        dataFrame=Frame(self.window,bd=10,relief=RIDGE,bg="powder blue",padx=20)
        dataFrame.place(x=0,y=130,width=1530,height=400)

        # ============================================= Dataframe left =================================

        dataframeleft=LabelFrame( dataFrame, text="Library Membership Information ",bd=10,bg="powder blue",relief=RIDGE,font=("times new roman",12,"bold"),padx=20)
        dataframeleft.place(x=0,y=5,width=860,height=370)

        lbl_member = Label(dataframeleft,text="Member Type",bg="powder blue",font=("times new roman",14,"bold"),padx=2,pady=6)
        lbl_member.grid(row=0,column=0,sticky="w")

        combo_member=ttk.Combobox(dataframeleft,textvariable=self.member_var,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_member["value"]=("Admin","Student","Lecturer")
        combo_member.grid(row=0,column=1)

        lbl_prnno = Label(dataframeleft,text="PRN NO.",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_prnno.grid(row=1,column=0,sticky="w")

        prnno_entry = Entry(dataframeleft,textvariable=self.prn_no_var,font=("times new roman",12,"bold"),width=32)
        prnno_entry.grid(row=1,column=1)

        lbl_Idno = Label(dataframeleft,text="ID NO.",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_Idno.grid(row=2,column=0,sticky="w")

        IDNO_entry = Entry(dataframeleft,textvariable=self.ID_var,font=("times new roman",12,"bold"),width=32)
        IDNO_entry.grid(row=2,column=1)

        lbl_FirstName = Label(dataframeleft,text="First Name",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_FirstName.grid(row=3,column=0,sticky="w")

        FirstName_entry = Entry(dataframeleft,textvariable=self.firstname_var,font=("times new roman",12,"bold"),width=32)
        FirstName_entry.grid(row=3,column=1)

        lbl_LastName = Label(dataframeleft,text="Last Name",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_LastName.grid(row=4,column=0,sticky="w")

        LastName_entry = Entry(dataframeleft,textvariable=self.lastname_var,font=("times new roman",12,"bold"),width=32)
        LastName_entry.grid(row=4,column=1)

        lbl_Address1 = Label(dataframeleft,text="Address 1",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_Address1.grid(row=5,column=0,sticky="w")

        Address1_entry = Entry(dataframeleft,textvariable=self.address1_var,font=("times new roman",12,"bold"),width=32)
        Address1_entry.grid(row=5,column=1)

        lbl_Address2 = Label(dataframeleft,text="Address 2",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_Address2.grid(row=6,column=0,sticky="w")

        Address2_entry = Entry(dataframeleft,textvariable=self.address2_var,font=("times new roman",12,"bold"),width=32)
        Address2_entry.grid(row=6,column=1)

        lbl_Mobile = Label(dataframeleft,text="Mobile",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_Mobile.grid(row=7,column=0,sticky=W)

        Mobile_entry = Entry(dataframeleft,textvariable=self.mobile_var,font=("times new roman",12,"bold"),width=32)
        Mobile_entry.grid(row=7,column=1)

        lbl_EmailId = Label(dataframeleft,text="Email ID:",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_EmailId.grid(row=8,column=0,sticky=W)

        EmailId_entry = Entry(dataframeleft,textvariable=self.email_id_var,font=("times new roman",12,"bold"),width=32)
        EmailId_entry.grid(row=8,column=1)

        lbl_Bookid = Label(dataframeleft,text="Book Id:",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_Bookid.grid(row=0,column=2,sticky=W)

        Bookid_entry = Entry(dataframeleft,textvariable=self.book_id_var,font=("times new roman",12,"bold"),width=35)
        Bookid_entry.grid(row=0,column=3)

        lbl_BookTitle = Label(dataframeleft,text="Book Title: ",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_BookTitle.grid(row=1,column=2,sticky=W)

        BookTitle_entry = Entry(dataframeleft,textvariable=self.book_title_var,font=("times new roman",12,"bold"),width=35)
        BookTitle_entry.grid(row=1,column=3)

        lbl_AuthorName = Label(dataframeleft,text="Author Name:",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_AuthorName.grid(row=2,column=2,sticky=W)

        AuthorName_entry = Entry(dataframeleft,textvariable=self.author_name_var,font=("times new roman",12,"bold"),width=35)
        AuthorName_entry.grid(row=2,column=3)

        lbl_DateBorrowed = Label(dataframeleft,text="Date Borrowed:",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_DateBorrowed.grid(row=3,column=2,sticky=W)

        DateBorrowed_entry = Entry(dataframeleft,textvariable=self.date_borrowed_var,font=("times new roman",12,"bold"),width=35)
        DateBorrowed_entry.grid(row=3,column=3)

        lbl_DateDue = Label(dataframeleft,text="Date Due:",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_DateDue.grid(row=4, column=2, sticky=W)

        DateDue_entry = Entry(dataframeleft,textvariable=self.date_due_var,font=("times new roman",12,"bold"),width=35)
        DateDue_entry.grid(row=4,column=3)

        lbl_DaysOnBook = Label(dataframeleft,text="Date On Book:",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_DaysOnBook.grid(row=5,column=2,sticky=W)

        DaysOnBook_entry = Entry(dataframeleft,textvariable=self.days_on_book_var,font=("times new roman",12,"bold"),width=35)
        DaysOnBook_entry.grid(row=5,column=3)

        lbl_LateReturnFine = Label(dataframeleft,text="Late Return Fine:",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_LateReturnFine.grid(row=6,column=2,sticky=W)

        LateRetFine_entry = Entry(dataframeleft,textvariable=self.late_rtn_fine_var,font=("times new roman",12,"bold"),width=35)
        LateRetFine_entry.grid(row=6,column=3)


        lbl_DateOvrDue = Label(dataframeleft,text="Date Over Due:",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_DateOvrDue.grid(row=7,column=2,sticky=W)

        DateOvrDue_entry = Entry(dataframeleft,textvariable=self.date_over_due_var,font=("times new roman",12,"bold"),width=35)
        DateOvrDue_entry.grid(row=7,column=3)

        lbl_ActualPrice = Label(dataframeleft,text="Actual Price:",font=("times new roman",14,"bold"),bg="powder blue",padx=2,pady=6)
        lbl_ActualPrice.grid(row=8,column=2,sticky=W)

        ActualPrice_entry = Entry(dataframeleft,textvariable=self.actual_price_var,font=("times new roman",12,"bold"),width=35)
        ActualPrice_entry.grid(row=8,column=3)


        # ========================================== Dataframe Right ====================================

        dataframeright=LabelFrame(dataFrame,text="Book Details",bd=10,bg="powder blue",relief=RIDGE,font=("times new roman",12,"bold"))
        dataframeright.place(x=900,y=0,width=550,height=350)

        self.txtbox = Text(dataframeright,font=("times new roman",12,"bold"),width=30,height=14,padx=2,pady=6)
        self.txtbox.grid(row=0,column=2)

        listScrollbarc = Scrollbar(dataframeright)
        listScrollbarc.grid(row=0,column=1,sticky="ns")

        listBooks = ["Learning Python", " The C Programming Language", " Introduction to Algorithms", " Javascript-The Good Parts"," Writing Solid Code "," Hacker's Delight"," Masala Lab "," Flavours In The Air "," Tiffin"," Yes Please "," Me Talk Pretty One Day(Paperback)"," Meditation and Its Methods ","Lectures on Bhagvad Gita"," Head First Book"," Learn Python The Hard Way"," Machine Python"," Advance Python"," Ishq Python"]

        listbox = Listbox(dataframeright,font=("times new roman",12,"bold"),width=32,height=14,yscrollcommand = listScrollbarc.set)
        listbox.grid(row=0,column=1,padx=6)
        listScrollbarc.config( command = listbox.yview() )

        for item in listBooks:
            listbox.insert(END,item)
    #

        FrameButton=Frame(self.window,bd=10,relief=RIDGE,bg="powder blue")
        FrameButton.place(x=0,y=530,width=1530,height=60)

        Save_Btn = Button(FrameButton,text="Add Data",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        Save_Btn.grid(row=0,column=0,padx=8,pady=6)

        Update_btn = Button(FrameButton,text="Update",font=("times new roman",12, " bold "),width=23,bg="blue",fg="white")
        Update_btn.grid(row=0,column=1,padx=8,pady=6)

        Show_btn = Button(FrameButton,text="Show Data",font=("times new roman",12,"bold"),bg="blue",width=23,fg="white")
        Show_btn.grid(row=0,column=2,padx=8,pady=6)

        Delete_btn = Button(FrameButton,text="Delete",font=("times new roman",12 ,"bold"),bg="blue",width=23,fg="white")
        Delete_btn.grid(row=0,column=3,padx=8,pady=6)

        Reset_btn = Button(FrameButton,text="Reset",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        Reset_btn.grid(row=0,column=4,padx=8,pady=6)

        Exit_btn = Button(FrameButton,text="Exit",font=("times new roman",12,"bold"),width=23,bg="blue",fg="white")
        Exit_btn.grid(row=0,column=5,padx=8,pady=6)

        # ============================================== Show Data Frame ====================================


        FrameData=Frame(self.window,relief=RIDGE,bd=10,bg="powder blue",)
        FrameData.place(x=0,y=590,width=1530,height=190)

        Table_frame = Frame(FrameData,relief=RIDGE,bd=5,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1490,height=175)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)


        self.library_table = ttk.Treeview(Table_frame,columns=("membertype","prnno","title","1stname","lstname","adress1","adress2","mobile","emailid","bookid","booktitle","author","dateborrowed","datedue","days","latertnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set , yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno", text="PRN NO")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("1stname", text="First Name")
        self.library_table.heading("lstname", text="Last Name")
        self.library_table.heading("adress1", text="Address1")
        self.library_table.heading("adress2", text="Address2")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("emailid", text="Email Id")
        self.library_table.heading("bookid", text="Book Id")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days")
        self.library_table.heading("latertnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("1stname", width=100)
        self.library_table.column("lstname", width=100)
        self.library_table.column("adress1", width=100)
        self.library_table.column("adress2", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("emailid", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latertnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

    def add_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Software@259",database="library_management_system")
        my_cursor=conn.cursor
        my_cursor.execute("insert into library value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.prn_no_var.get(),
            self.ID_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.mobile_var.get(),
            self.email_id_var.get(),
            self.book_id_var.get(),
            self.book_title_var.get(),
            self.author_name_var.get(),
            self.date_borrowed_var.get(),
            self.date_due_var.get(),
            self.late_rtn_fine_var.get(),
            self.date_over_due_var.get(),
            self.actual_price_var.get()


        ))
        conn.commit()
        conn.close()













if __name__ == "__main__":
    window=Tk()
    obj=LibraryManagementSystem(window)
    window.mainloop()