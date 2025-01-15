import pyautogui as pg
import time
from pynput import keyboard
import requests
from bs4 import BeautifulSoup
import pyperclip
# Tọa độ
tb_x = 280
tb_y = 351
fx = 534
fy = 353
start_x, start_y, end_x, end_y = 408, 522, 697, 539
npx = 1306
npy = 103
newtxtx, newtxty = 1719, 33
# Chuỗi để nhập
c = '058304000000'
# Biến toàn cục kiểm tra thoát
exit_program = False
# Hàm sẽ được gọi khi nhấn phím
def on_press(key):
    global exit_program
    try:
        if key == keyboard.Key.esc:
            print("Phím Esc đã được nhấn, chương trình sẽ thoát.")
            exit_program = True
            return False  # Dừng listener
    except AttributeError:
        pass
# Lắng nghe bàn phím trong một luồng riêng
listener = keyboard.Listener(on_press=on_press)
listener.start()
x = 0
# Chạy vòng lặp tự động 
for i in range(774, 999999): #32029
    if x <= 3000:
        if exit_program:
            break  # Nếu phím Esc được nhấn, thoát khỏi vòng lặp
        # Thực hiện các thao tác tự động
        pg.leftClick(tb_x, tb_y)
        time.sleep(0.1)
        pg.hotkey('ctrl', 'a')
        time.sleep(0.1)

        pg.typewrite(c[:len(c)-len(str(i))]+str(i))
        time.sleep(0.1)

        pg.leftClick(fx, fy)
        time.sleep(0.1)

        pg.moveTo(start_x, start_y)

        time.sleep(0.1)
        pg.mouseDown()

        time.sleep(0.1)
        pg.moveTo(end_x, end_y)

        time.sleep(0.1)
        pg.mouseUp()

        time.sleep(0.1)
        pg.hotkey('ctrl', 'c')

        time.sleep(0.1)
        pg.leftClick(npx, npy)
        time.sleep(0.1)
        pg.typewrite('\n'+str(i) + ": ")
        pg.hotkey('ctrl', 'v')
        x+=1
        print(x)
    else:
        x=0
        pg.leftClick(newtxtx, newtxty)
#     # time.sleep(1)  # Thêm độ trễ giữa các lần thao tác nếu cần


listener.stop()  # Dừng listener khi kết thúc