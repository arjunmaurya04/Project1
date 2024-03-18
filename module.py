class recruiter:
    def __init__(self,rid=0,name=None,salary=None):
        self.rid=rid
        self.name=name
        self.salary=salary

    def __repr__(self):
        return f'Recruiter[{self.rid}.{self.name},{self.salary}]'
#------------------------------------------------------------------------------------------------------------
class candidate_info:
    def __init__(self,Name,Address,Contact,Email,Password):
        self.Name=Name
        self.Address=Address
        self.Contact=Contact
        self.Email=Email
        self.Password=Password
    def __repr__(self):
        return f'candidate_info[{self.name} {self.Address} {self.Contact} {self.Email} {self.Password}'
#-------------------------------------------------------------------------------------------------
class admin:
    def __init__(self,Email,Password):
        self.Email=Email
        self.Password=Password
    
    def __repr__(self):
        return f'admin[{self.Email} {self.Password}]'
#=====================================================================================================
class candidatedetails:
    def __init__(self,email,qualification,workexp,lastsalary,source,lastdesignation,designationapply,noticeperiod,gender,dob,date):
        self.email=email
        self.qualification=qualification
        self.workexp=workexp
        self.lastsalary=lastsalary
        self.source=source
        self.lastdesignation=lastdesignation
        self.designationapply=designationapply
        self.noticeperiod=noticeperiod
        self.gender=gender
        self.dob=dob
        self.date=date
    def __repr__(self):
        return f'candidatedetails[{self.email}{self.qualification} {self.workexp} {self.lastsalary} {self.source} {self.lastdesignation} {self.designationapply} {self.noticeperiod} {self.gender} {self.dob} {self.date}'