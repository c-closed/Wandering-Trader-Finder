# -*- Encoding:UTF-8 -*- #
### 코드를 무단으로 복제,개조 및 배포하지 말 것 ###
### Copyright ⓒ 2021-2022 c-closed / 감는 c-closed@naver.com ###
import WTF_info
import webbrowser
import tkinter.messagebox
import tkinter
import WTF_update
    
def open_homepage():
    webbrowser.open(WTF_info.homepage_url)

def check_update_log():
    import WTF_update
    tkinter.messagebox.showinfo("업데이트 내용 확인", WTF_update.patchnote)

def check_current_version():
    tkinter.messagebox.showinfo("현재 버전", '[ '+WTF_info.current_version+' ]')

def open_map():
    import WTF_GUI
    if WTF_GUI.continent_name_combobox.get() == "대륙 선택":
        tkinter.messagebox.showinfo("대륙 미선택","대륙을 선택 후 버튼을 눌러주세요.")
    elif WTF_GUI.area_name_combobox.get() == "지역 선택":
        tkinter.messagebox.showinfo("지역 미선택","지역을 선택 후 버튼을 눌러주세요.")
    else:
        path = WTF_info.exe_path+'/Map/'+WTF_GUI.continent_name_combobox.get()+'/'+WTF_GUI.area_name_combobox.get()+'.png'
        map_window = tkinter.Toplevel(WTF_GUI.main_window)
        map_window.title(WTF_GUI.area_name_combobox.get())
        map_window.iconbitmap(WTF_info.exe_path+'/MainFolder/WTF_icon.ico')
        map_window.wm_attributes("-topmost", 1)
        images = tkinter.PhotoImage(file=path,master=map_window)
        label = tkinter.Label(map_window, image=images)
        label.image = images
        label.pack()
    
def do_not_see_again():
    with open(WTF_info.exe_path+'/MainFolder/다시보지않기.txt','w',encoding="UTF-8") as file:
        file.write("다시보지않기")
        
def chk_do_not_see_again():
    with open(WTF_info.exe_path+'/MainFolder/다시보지않기.txt','r',encoding="UTF-8") as file:
        check_do_not_see_again = file.read()
    if check_do_not_see_again == "다시보지않기":
        pass
    elif check_do_not_see_again == "":
        import WTF_GUI
        do_not_see_again_window = tkinter.Toplevel(WTF_GUI.main_window)
        do_not_see_again_window.title("다시보지않기")
        patchnote_label = tkinter.Label(do_not_see_again_window, text=WTF_update.patchnote)
        patchnote_label.pack(padx=5, pady=5)
        do_not_see_again_btn = tkinter.Button(do_not_see_again_window, text="다시보지않기", command=do_not_see_again)
        do_not_see_again_btn.pack(pady=5)
        
def change_area(event):
    import WTF_GUI
    current_continent = WTF_GUI.continent_name_combobox.get()
    if current_continent == "아르테미스":
        WTF_GUI.area_name_combobox.config(values=WTF_info.arthemis_area_list)
    elif current_continent == "유디아":
        WTF_GUI.area_name_combobox.config(values=WTF_info.eudia_area_list)
    elif current_continent == "루테란 서부":
        WTF_GUI.area_name_combobox.config(values=WTF_info.luterra_west_area_list)
    elif current_continent == "루테란 동부":
        WTF_GUI.area_name_combobox.config(values=WTF_info.luterra_east_area_list)
    elif current_continent == "토토이크":
        WTF_GUI.area_name_combobox.config(values=WTF_info.tortoyk_area_list)
    elif current_continent == "애니츠":
        WTF_GUI.area_name_combobox.config(values=WTF_info.anihc_area_list)
    elif current_continent == "아르데타인":
        WTF_GUI.area_name_combobox.config(values=WTF_info.arthetine_area_list)
    elif current_continent == "베른 북부":
        WTF_GUI.area_name_combobox.config(values=WTF_info.vern_north_area_list)
    elif current_continent == "슈샤이어":
        WTF_GUI.area_name_combobox.config(values=WTF_info.shushire_area_list)
    elif current_continent == "로헨델":
        WTF_GUI.area_name_combobox.config(values=WTF_info.rohendel_area_list)
    elif current_continent == "욘":
        WTF_GUI.area_name_combobox.config(values=WTF_info.yorn_area_list)
    elif current_continent == "페이튼":
        WTF_GUI.area_name_combobox.config(values=WTF_info.feiton_area_list)
    elif current_continent == "파푸니카":
        WTF_GUI.area_name_combobox.config(values=WTF_info.papunika_area_list)
    elif current_continent == "베른 남부":
        WTF_GUI.area_name_combobox.config(values=WTF_info.vern_south_area_list)
    elif current_continent == "로웬":
        WTF_GUI.area_name_combobox.config(values=WTF_info.lowen_area_list)
    elif current_continent == "엘가시아":
        WTF_GUI.area_name_combobox.config(values=WTF_info.elgacia_area_list)
    elif current_continent == "플레체" or "볼다이크":
        tkinter.messagebox.showinfo("대륙 미구현","현재 '플레체'와 '볼다이크'는 미구현 대륙입니다.")
    elif current_continent == "대륙 선택":
        tkinter.messagebox.showinfo("대륙 미선택","대륙을 선택 후 버튼을 눌러주세요.")
    else:
        tkinter.messagebox.showerror("오류 발생",'관리자에게 "콤보박스 오류"라고 전달해주세요.')
    WTF_GUI.area_name_combobox.set("지역 선택")