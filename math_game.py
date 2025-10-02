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


# ======================
# کلاس آیتم: Item
# ======================
class Item:
    def __init__(self, name, kind, value):
        self.name = name    # نام آیتم (مثلاً Potion)
        self.kind = kind    # نوع اثر: heal / ...
        self.value = value  # مقدار اثر (مثلاً چند HP)

    def __str__(self):
        if self.kind == "heal":
            return f"{self.name} (+{self.value} HP)"
        return f"{self.name} ({self.kind}: {self.value})"


# ======================
# کلاس سوال ریاضی: Question
# ======================
class Question:
    def __init__(self, a, b, op_symbol, answer):
        self.a = a
        self.b = b
        self.op_symbol = op_symbol
        self.answer = answer

    def text(self):
        return f"{self.a} {self.op_symbol} {self.b} = ?"

    def check_answer(self, user_answer):
        try:
            return int(user_answer) == self.answer
        except ValueError:
            return False


def generate_question(level):
    # سختی بر اساس سطح: اعداد بزرگ‌تر با سطح بالاتر
    max_n = 10 + level * 5
    a = random.randint(1, max_n)
    b = random.randint(1, max_n)
    op_symbol = random.choice(["+", "-", "*"])
    if op_symbol == "+":
        ans = a + b
    elif op_symbol == "-":
        ans = a - b
    else:
        ans = a * b
    return Question(a, b, op_symbol, ans)


# ======================
# توابع کمکی رابط کاربری
# ======================
def print_status(player, enemy):
    print("\n================ STATUS ================")
    print(player)
    print(enemy)
    print("=======================================\n")


def list_inventory(player):
    if not player.inventory:
        print("📭 کیف خالی است.")
        return
    print("🎒 آیتم‌ها:")
    for i, it in enumerate(player.inventory, 1):
        print(f"  {i}. {it}")


# ======================
# حلقه اصلی بازی
# ======================
def game():
    print("🎮 خوش آمدی به بازی: چالش ریاضی برای بقا")
    name = input("نام بازیکن را وارد کن: ").strip() or "Player"
    player = Player(name, health=100, level=1)
    # آیتم شروع
    player.add_item(Item("Potion", "heal", 20))

    # یک دشمن ساده
    enemy = Enemy("Goblin", health=60, level=1, damage=10)

    print_status(player, enemy)

    # حلقه مبارزه
    while player.is_alive() and enemy.is_alive():
        print("یک گزینه را انتخاب کن:")
        print("1) حمله (با حل سوال ریاضی)")
        print("2) استفاده از آیتم")
        print("3) نمایش آیتم‌ها")
        choice = input("> ").strip()

        if choice == "1":
            # حمله با سوال
            q = generate_question(player.level)
            print("❓ سوال:", q.text())
            ans = input("جواب: ").strip()
            if q.check_answer(ans):
                damage = 10 + player.level * 5
                print(f"✅ درست گفتی! {damage} آسیب به دشمن وارد شد.")
                enemy.take_damage(damage)
                player.gain_xp(15)
                # شانس جایزه
                if random.random() < 0.3:
                    reward = Item("Potion", "heal", 20)
                    player.add_item(reward)
                    print(f"🎁 جایزه گرفتی: {reward}")
            else:
                print("❌ اشتباه! نوبت دشمن است.")
                enemy.attack(player)

        elif choice == "2":
            list_inventory(player)
            item_name = input("اسم آیتم برای استفاده: ").strip()
            if item_name:
                player.use_item(item_name)

        elif choice == "3":
            list_inventory(player)

        else:
            print("⚠️ گزینه نامعتبر.")

        print_status(player, enemy)

    # پایان
    if player.is_alive() and not enemy.is_alive():
        print("🏆 تبریک! دشمن را شکست دادی.")
    elif not player.is_alive():
        print("☠️ باختی! بازی تمام شد.")
    else:
        print("🏁 بازی به پایان رسید.")


# اجرای بازی
if __name__ == "__main__":
    game()

# بگو «اوکی» تا از **اولین خط** شروع کنم و دقیقاً «کلمه‌به‌کلمه» توضیح بدم.
