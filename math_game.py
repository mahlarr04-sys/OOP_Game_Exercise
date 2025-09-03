# ======================
# بازی متنی: چالش ریاضی برای بقا
# مفاهیم: کلاس، وراثت، متد، مجیک‌متد، کپسوله‌سازی (Getter/Setter)، چندریختی
# ======================

import random

#  هم بازیکن- هم دشمن ویژگی مشترکشون تعریف میکنه/ کلاس پایه (Character)
class character:
    def __init__(self, name, health, level):#ویژگی ها مشتزک و وردوی ها بازی 
        self.name =name
        self.health= health
        self.level=level
        self.max_health= health
    def take_damage (self, amount):#میزان اسیب دیدگی
        if amount<0:
            amount=0
        self.health -= amount
        if self.health <0:
             self.health =0
        return self.health

    def is_alive(self):#وضعیت زنده بودنش
        return self.health >0
    
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
#کلاس دشمن 
class Enemy(Character):
    def __init__(self, name ,health, level , damage ):
        super().__init__(name, health,level)
        pass
    def attack (self , player ):
        pass
    def __str__(self):
        pass
#کلاس ایتم
class Item:
    def __init__(self , name ,effect):
        pass
    def __str__(self):
        pass
#حلقه اصلی بازی
def game():
    pass
#اجرا بازی - فراخوانی
if __name__  =="__main__":
    game()





    
                


    

                
