# def say_hollo(name):
#     print(f"hello {name}")
# default value   = ""ودى تحطها م الاخر للاول عشان الكود ميعطلش
# packing and un packing **

# say_hollo("islam")

def full_name(first, middle, last="unknown"):
    print(
        f"hello {first.capitalize().strip()} {middle.upper():.1s} {last.capitalize().strip()}")


full_name("islam", "ibrahim")
print("-"*60)


def say_hello(*people):  # مهم فشخ لو مش عارف هيبقى عندك كام اسم
    for name in people:
        print(f"hello {name}")


say_hello("ahmed", "ali", "ramy")
