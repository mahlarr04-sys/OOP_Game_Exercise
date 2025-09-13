# ======================
# بازی متنی: چالش ریاضی برای بقا
# مفاهیم: کلاس، وراثت، متد، مجیک‌متد، کپسوله‌سازی (Getter/Setter)، چندریختی
# ======================

import random

#  هم بازیکن- هم دشمن ویژگی مشترکشون تعریف میکنه/ کلاس پایه (Character)
class character:
    def __init__(self, name, health=100, level=1):#ویژگی ها مشتزک و وردوی ها بازی 
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
        return f"{self.__class__.__name__} {self.name}(lv.{self.level}) – hp: {self.health}/{self.max_health}"
    

# کلاس فرزند Player
class player(character):
    def __init__(self, name, health, level):#ویژگی ها و وردوی ها  رو میگیره  
        #برای ارث بری بایدد حتما انیت صدا بزنیم تا فعال بشه 
        super().__init__(name, health, level)
        self.inventory = []#ویژگی جدید/لیست ایتم ها
        self.xp =0#ویژگی جدید/امتیاز  تجربه
        #مقدار آستانه‌ی تجربه‌ی مورد نیاز برای ارتقا سطح
        while self.xp >= self._xp_threshold():
            self.xp -= self._xp_threshold()
            self._level_up()

    def _xp_threshold(self):#محاسبه آستانه‌ی تجربه (XP threshold) برای هر سطح
        return 50 * self.level
    
    def _level_up(delf):#تغییرات لول اپ
        self.level +=1
        self.max_health +=10
        self.set_health(self.max_health)
        print(f" لول‌آپ! سطح {self.level} | HP جدید: {self.health}/{self.max_health}")

    def add_item(self,item):#اظاقه کردن ایتم به لیست 
        self.inventory.append(item)

    def use_item(self ,item_name):#استفاده از ایتم موجود
        # جستجو بر اساس نام (غیرحساس به حروف بزرگ/کوچک)
        for i , it in enumerate(self.inventory):
            if it.name.lower()== item_name_lower():
                if it.kine =="heal":
                    set.self_health(set_health + it,value)
                    print(f" استفاده از {it.name} (+{it.value} HP)")
                self.inventory.pop(i)#حذف ایتم استفاده شده از لیست 
                return True
        print(" آیتمی با این نام پیدا نشد.")
        return False

    def set_health(self ,amount):#مقدار سلامتی در محدوده مجاز باشد
        if amount < 0:
            amount =0
        if amount >self.max_health:
            amount = self.max_health
        self.health =amount
        return self.health

    def __str__(self):#خروجی  هر جای مسیر 
         inv_count =len (self.inventory)
         return f"{self.name}(lv:{self.level} - hp:{self.health}/{self.max_health} – XP: {self.xp}/{self._xp_threshold()} – Items: {inv_count})"


    def answer_question(self, question, enemy):#پاسخ به soal
        print("❓ soal:", question.text())
        ans =input("jvab:").strip()
        if question.check_answer(ans):#بررسی که ایا جواب درست یا نه؟
            damage =10 +self.level*5#فمرول مقدار اسیب دیدیگی
            print(f"drst!{damage}asib b dshmn vard shod")
            enemy.teke_damage(damage)#فراخوانی/ضربه به دشمن و سلامتش  کم میکنه
            self.gain_xp(15)
            if random.random()<0.3:
                reward =Item("potion","heal",20)
                self.add_item(reward)
                print(f"jayze grfty:{reward}")
            return True
        else:
            print("ashtbah!!! nobt dshmn")
            enemy.attack(self)
            return False

    def get_health(self):#میزان زنده بودن
        return self.heslth
#کلاس دشمن 
class Enemy(Character):
    def __init__(self, name ,health, level , damage ):
        super().__init__(name, health,level)
        self.damage= damage

    def attack (self , player ):
        print(f"{self.name} hmle krd!  ({self.damage}asib)")
        player.take_damage(self.damage)


    def __str__(self):
        return f"👹 {self.name} (Lv.{self.level}) – HP: {self.health}/{self.max_health} – DMG: {self.damage}"



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

print



    
                
