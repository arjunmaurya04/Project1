import mysql.connector as db
from module import recruiter
import pandas as pd
import re
from datetime import datetime
con=db.connect(host="localhost", user="root",passwd='******',db="******")
cursor=con.cursor()

#---------------------Admin Table----------------------------------------------
try:
    Admin_table='create table if not exists admin(Email text,Password text)'
    cursor.execute(Admin_table)
    con.commit()
except:
    print("Table already exists")
#===============candidatedetail table====================================================================
try:
    candidatedetails='create table if not exists candidatedetails(email varchar(50),qualification varchar(50),workexp text,lastsalary float(10,2),source text,lastdesignation varchar(50),designationapply varchar(50),noticeperiod int,gender varchar(50),dob date,date_reg date);'
    cursor.execute(candidatedetails)
      
except:
    print("Table already exists")
#---------------Candidate Table------------------------------------------------
try:
    candidate_table='create table if not exists candidate1(Email varchar(50),Password text,Name text,Address text,Contact varchar(50))'
    cursor.execute(candidate_table)
    con.commit() 
except:
    print("Table already exists")   

def register(x):
    register_query='insert into candidate1(Email,Password,Name,Address,Contact) values(%s,%s,%s,%s,%s)'
    cursor.execute(register_query,x)
    con.commit()
#==========================Admin login=================================================================
def Admin_Login(Email,Password):
    select_query='Select * from admin where Email= %s and Password =%s'
    data=(Email,Password)
    cursor.execute(select_query,data)
    s=cursor.fetchone()

    try:
        
        if s[0]==Email:
            if s[1]==Password:
                return True
    except:
        print('-----Invalid email or Password--------')
#========================Candidate Login=============================================================================
def candidate_Login(Email,Password):
    select_query='Select * from candidate1 where Email= %s and Password =%s'
    data=(Email,Password)
    cursor.execute(select_query,data)
    s=cursor.fetchone()

    try:
        if s[0]==Email:
            if s[1]==Password:
                return True
    except:
        print('-----Invalid email or Password--------')
        
#================-candidate details===================================================
def details(y):
    detail_query='insert into candidatedetails(email,qualification,workexp,lastsalary,source,lastdesignation,designationapply,noticeperiod,gender,dob,date_reg) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(detail_query,y)
    con.commit()        
#-------------------display candidate details---------------------------------------------------
def display_candidated_names():
    # display='select * from candidate1 left join candidatedetails on candidate1.email=candidatedetails.email;'
  
    # cursor.execute(display)
    # result=cursor.fetchall()
    # print(result)

    display='select * from candidate1 left join candidatedetails on candidate1.email=candidatedetails.email;'
    
    cursor.execute(display)
    result=cursor.fetchall()
    rec=pd.DataFrame(result,columns=['Email','Password','Name','Address','Contact','final_status','qualification','workexp','lastsalary','source','lastdesignation','designationapply','noticeperiod','gender','dob','date_reg','email'])
    pd.set_option('display.colheader_justify','center')
    if rec.empty==True:
        print('\n no products found')
    else:
        print(rec)
#------------------------search candidate details------------------------------------------------------
def search_candidate(candname):
    display2='select * from candidate1 left join candidatedetails on candidate1.email=candidatedetails.email where candidate1.email= %s'
  
    cursor.execute(display2,(candname,))
    result=cursor.fetchall()
    rec=pd.DataFrame(result,columns=['Email','Password','Name','Address','Contact','final_status','qualification','workexp','lastsalary','source','lastdesignation','designationapply','noticeperiod','gender','dob','date_reg','email'])
    pd.set_option('display.colheader_justify','center')
    if rec.empty==True:
        print('\n no products found')
    else:
        print(rec)    
    # print(result)
#---------------------------------candidate feedback------------------------------------------------------------------
def candidate_feedback(f):
    feedback='update candidate1 set final_status=%s where email=%s;'
    cursor.execute(feedback,f)
    con.commit()

#----------------selected candidates----------------------------------------------------------------------------
def selected_candidate():
    display='select * from candidate1 where final_status="select";'
    
    cursor.execute(display)
    result=cursor.fetchall()
    rec=pd.DataFrame(result,columns=['Email','Password','Name','Address','Contact','final_status'])
    pd.set_option('display.colheader_justify','center')
    if rec.empty==True:
        print('\n no products found')
    else:
        print(rec)    
#===============Reject candidates==========================================================================
def rejected_candidate():
    display='select * from candidate1 where final_status="reject";'
    
    cursor.execute(display)
    result=cursor.fetchall()
    rec=pd.DataFrame(result,columns=['Email','Password','Name','Address','Contact','final_status'])
    pd.set_option('display.colheader_justify','center')
    if rec.empty==True:
        print('\n no products found')
    else:
        print(rec) 
#===============download data in excel format===================================================================
#query your date
def download_data():
    download1='select * from candidate1 left join candidatedetails on candidate1.email=candidatedetails.email;'
    cursor=con.cursor()
    cursor.execute(download1)
    data=cursor.fetchall()

    #get columns names
    columns=[i[0] for i in cursor.description]

    #create datafram
    df=pd.DataFrame(data,columns=columns)

    #generate unique filename with timestamp
    timestamp=datetime.now().strftime('%Y%m%d%H%M%S')
    file_path=f'output_{timestamp}.csv'

    #export the data to excel
    df.to_csv(file_path, index=False)
#=============delete candidate===========================================================
def delete_candidate(deleteid):
    delete_query='delete candidate1, candidatedetails from candidate1 join candidatedetails on candidate1.email=candidatedetails.email where candidate1.email=%s;'
    cursor.execute(delete_query,(deleteid,))
    con.commit()    
#====================candidate show data===============================================================
def show_data(Email):
    display2='select * from candidate1 left join candidatedetails on candidate1.email=candidatedetails.email where candidate1.email= %s'
  
    cursor.execute(display2,(Email,))
    result=cursor.fetchall()
    rec=pd.DataFrame(result,columns=['Email','Password','Name','Address','Contact','final_status','qualification','workexp','lastsalary','source','lastdesignation','designationapply','noticeperiod','gender','dob','date_reg','email'])
    pd.set_option('display.colheader_justify','center')
    if rec.empty==True:
        print('\n no products found')
    else:
        print(rec)
