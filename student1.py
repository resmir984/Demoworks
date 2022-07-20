class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")

    @property
    def get_name(self):
        print(self.course_name)
        return self.course_name

    def __str__(self):
        return self.course_name


class Batch():
    def add_batch(self, **kwargs):
        self.course = kwargs.get("course")
        self.batch_code = kwargs.get("batch_code")
        self.start_date = kwargs.get("start_date")
    def __str__(self):
        return self.batch_code

class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.email=kwargs.get("email")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.student_name

django=Course()
django.add_course(course_name="django",status=True)

djb1=Batch()
djb1.add_batch(course=django,batch_code="djmay2k22b1",start_date="12-6-2022")

rahul=Student()
rahul.add_student(student_name="rahul",email="rahul@gmail.com",batch=djb1)
akhil=Student()
akhil.add_student(student_name="akhil",email="akhil@gmail.com",batch=djb1)
vishnu=Student()
vishnu.add_student(student_name="vishnu",email="vishnu@gmail.com",batch=djb1)
print(vishnu)

meanstack=Course()
meanstack.add_course(course_name="meanstack",status=True)
msb1=Batch()
msb1.add_batch(batch_code="msmayb1",start_date="12-7-1022",course=meanstack)

ravi=Student()
ravi.add_student(student_name="ravi",email="ravi@gmail.com",batch=msb1)

vinay=Student()
vinay.add_student(student_name="vinay",email="vinay@gmail.com",batch=msb1)

students=[]
students.append(ravi)
students.append(rahul)
students.append(vinay)
students.append(vishnu)

#print students in meanstack

for stud in students:
    if stud.batch.course.course_name=="meanstack":
        print(stud)

ms_stud=[stud.student_name for stud in students if stud.batch.course.course_name=="meanstack"]
print(ms_stud)

#master_string= "abbcddeghgg"
#chk_word="egg"
