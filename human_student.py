#یک کلاس والد بنویسید که به عنوان انسان  ویژگی یک انسان را دارا باشد - اسم -قد و.. 
#سپس یک کلاس دانش اموز  که از لاس انسان ارث بری کند و ویژگی های  کلاس  چندم بودن و چه مدرسه ای بودن را به ان اظافه کنید

class Person:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def ful_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return f"{self.ful_name()}, Age: {self.age}, Gender: {self.gender}, "
    

class Student(Person):
    def __init__(self, first_name, last_name, age, gender, school, grade):
        super().__init__(first_name, last_name, age, gender)  # ✅ الان پدر __init__ داره
        self.grade = grade
        self.school = school

    def __str__(self):
        return super().__str__() + f"School: {self.school}, Grade: {self.grade}"

    def get_grade(self):
        return self.grade
    
    def get_school(self):
        return self.school


s = Student("ali", "karami", 22, "male", "ABC school", "11")
print(s)    
print(s.ful_name())
print(s.get_grade())
print(s.get_school())
