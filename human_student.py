#یک کلاس والد بنویسید که به عنوان انسان  ویژگی یک انسان را دارا باشد - اسم -قد و.. 
#سپس یک کلاس دانش اموز  که از لاس انسان ارث بری کند و ویژگی های  کلاس  چندم بودن و چه مدرسه ای بودن را به ان اظافه کنید

class Person:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    
    def __str__(self):
        return f"Person: {self.full_name()}, Age: {self.age}, Gender: {self.gender}"
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
p= Person("ali","mohammadi",20,"male")#وروردی اولیه
p.first_name="seyed"#ویژگی های انسان را تغییر دهد
print(p)