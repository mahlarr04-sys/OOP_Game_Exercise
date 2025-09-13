#یک تابع بنویسید که بینهایت  ارگومان وروردی بگیرد و همه با هم جمع کنه 
def smart_sum(*args):
    total = 0
    for item in args:
        if isinstance(item, (int, float)):
            total += item
        elif isinstance(item, (list, tuple)):
            total += smart_sum(*item)
        elif isinstance(item, str) and item.isdigit():
            total += int(item)
    return total

# مثال ساده برای تست:
result = smart_sum(5, "10", [2, "3a"], "hello", (1, "7"), "003", 4.5)
#10+2+3+1+7+3+4.5
print(result)  # خروجی: 32.5

             


