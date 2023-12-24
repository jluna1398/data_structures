# box example
# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item);
#         elif item.is_a_key():
#             print("found inside")

def countdown(i):
    if i <= 0:
        print("Lets count down")
    else:
        print(i)
        countdown(i-1)

countdown(10)