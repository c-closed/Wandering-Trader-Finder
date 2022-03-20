# -*- Encoding:UTF-8 -*- #
### 코드를 무단으로 복제,개조 및 배포하지 말 것 ###
### Copyright ⓒ 2021-2022 c-closed / 감는 c-closed@naver.com ###
from tkinter import *
import WTF_info
import WTF_func
from tkinter.ttk import *

main_window = Tk()
main_window.title("커스터마이징 적용기")
main_w = 300
main_h = 150
main_ws = main_window.winfo_screenwidth()
main_hs = main_window.winfo_screenheight()
main_x = (main_ws-main_w)/2
main_y = (main_hs-main_h)/2
main_window.geometry('%dx%d+%d+%d' % (main_w, main_h, main_x, main_y))
main_window.iconbitmap(WTF_info.exe_path+'/MainFolder/icon.ico')
main_window.wm_attributes("-topmost", 1)

menu = Menu(main_window)

menu_info = Menu(menu, tearoff=0, relief='groove')
menu_info.add_command(label="커마 폴더 경로 확인", command=WTF_func.check_customizing_path)
menu_info.add_command(label="로아 설치 경로 확인", command=WTF_func.check_lostark_install_path)
menu_info.add_command(label="현재 버전 확인", command=WTF_func.check_current_version)
menu_info.add_command(label="업데이트 로그", command=WTF_func.check_update_log)
menu_comm = Menu(menu, tearoff=0, relief='groove')
menu_comm.add_command(label="오류 및 건의사항", command=WTF_func.open_homepage)
menu.add_cascade(label="정보", menu=menu_info)
menu.add_cascade(label="소통", menu=menu_comm)
main_window.config(menu=menu)
    
continent_name_combobox = Combobox(main_window, values=WTF_info.continent_name_list)
continent_name_combobox.pack()
continent_name_combobox.set("대륙 선택")
continent_apply_btn = Button(main_window, text="적용하기", command=WTF_func.change_area)
continent_apply_btn.pack()
area_name_combobox = Combobox(main_window)
area_name_combobox.pack()
area_name_combobox.set("지역 선택")
map_open_btn = Button(main_window, text="지도 열기", command=WTF_func.open_map)
map_open_btn.pack()
main_window.mainloop()