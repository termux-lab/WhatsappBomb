import pyautogui, time, os
print("""
     ,'"".
     )  ,|
    /  /,'-.
   /  //  /.`.
 ,'  //  /  `.`.        _______
(    )--.`.   //|      /______/|
|`--'|   `.`.// |      |BOOM! ||
 `--'      `./  /______|______|/
   |WhaBomb  | /
   |_________|/
""")
message = input("Text=> ")
count = input("Count=> ")
star = input("Start=> ")
interv = input("Interval=>")
if interv == "":
    interv=0.2
input("Press Enter for starting")
times = int(star)
for i in range(int(star)):
    os.system("cls")
    print(times)
    time.sleep(int(1))
    times-=1
for i in range(int(count)):
    pyautogui.write(message)
    pyautogui.press("enter")
    time.sleep(int(interv))
pyautogui.alert('End :)')
