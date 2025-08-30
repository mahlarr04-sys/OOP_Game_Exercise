# کلاس پایه (Character)
class character:
    def __init__(self, name, health, level):#ویژگی ها و وردوی ها بازی 
        pass
    def take_damage(self, amount):#میزان اسیب
        pass
    def is_alive(self):#وضعیت زنده بودنش
        pass
    def __str__(self):#نشان دادن نام
        pass
# کلاس فرزند Player
class player(character):
    def __init__(self, name, health, level):#ویژگی ها و وردوی ها  رو میگیره  
        #برای ارث بری بایدد انیت صدا بزنیم تا فعال بشه 
        super().__init__(name, health, level)
        pass
    def answer_question(self, question):#پاسخ به سوال
        pass
    def gain_xp(self, amount):# اضافه کردن و بررسی لول اپxpتجربه 
        pass
    def add_item(self, item):#اضافه کردن آیتم
        pass
    def use_item(self, item_name):#استفاده و حذف ان آیتم
        pass    
    def get_health(self):#میزان زنده بودن
        pass
class Enemy(Character):
    def __init__(self, name ,health, level , damage ):
        super().__init__(name, health,level)
        pass
    




    
                