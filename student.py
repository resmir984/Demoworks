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


django = Course()
django.add_course(course_name="django", status=True)
# print(django)
# ms=Course()
# ms.add_course(course_name="meanstack",status=True)
# bd=Course()
# bd.add_course(Course_name="bigdata",status=True)

djb1=Batch()
djb1.add_batch(course="django", batch_code="djmay2k22b1", start_date="12-6-2022")

print(djb1.course.get_name)