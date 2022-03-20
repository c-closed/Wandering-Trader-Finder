# -*- Encoding:UTF-8 -*- #
### 코드를 무단으로 복제,개조 및 배포하지 말 것 ###
### Copyright ⓒ 2021-2022 c-closed / 감는 c-closed@naver.com ###
import WTF_info
import webbrowser
import tkinter.messagebox
import tkinter

def check_lostark_install_path():
    tkinter.messagebox.showinfo("로아 설치 경로", WTF_info.LA_path)
    
def check_customizing_path():
    tkinter.messagebox.showinfo("커마 폴더 경로", WTF_info.Customizing_path)
    
def open_homepage():
    webbrowser.open(WTF_info.homepage_url)

def check_update_log():
    import WTF_update
    tkinter.messagebox.showinfo("업데이트 내용 확인", WTF_update.patchnote)

def check_current_version():
    tkinter.messagebox.showinfo("현재 버전", '[ '+WTF_info.current_version+' ]')

def change_area():
    import WTF_GUI
    current_continent = WTF_GUI.continent_name_combobox.get()
    if current_continent == "아르테미스":
        WTF_GUI.area_name_combobox.config(values=WTF_info.arthemis_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "유디아":
        WTF_GUI.area_name_combobox.config(values=WTF_info.eudia_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "루테란 서부":
        WTF_GUI.area_name_combobox.config(values=WTF_info.luterra_west_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "루테란 동부":
        WTF_GUI.area_name_combobox.config(values=WTF_info.luterra_east_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "토토이크":
        WTF_GUI.area_name_combobox.config(values=WTF_info.tortoyk_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "애니츠":
        WTF_GUI.area_name_combobox.config(values=WTF_info.anihc_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "아르데타인":
        WTF_GUI.area_name_combobox.config(values=WTF_info.arthetine_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "베른 북부":
        WTF_GUI.area_name_combobox.config(values=WTF_info.vern_north_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "슈샤이어":
        WTF_GUI.area_name_combobox.config(values=WTF_info.shushire_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "로헨델":
        WTF_GUI.area_name_combobox.config(values=WTF_info.rohendel_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "욘":
        WTF_GUI.area_name_combobox.config(values=WTF_info.yorn_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "페이튼":
        WTF_GUI.area_name_combobox.config(values=WTF_info.feiton_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "파푸니카":
        WTF_GUI.area_name_combobox.config(values=WTF_info.papunika_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "베른 남부":
        WTF_GUI.area_name_combobox.config(values=WTF_info.vern_south_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "로웬":
        WTF_GUI.area_name_combobox.config(values=WTF_info.lowen_area_list)
        tkinter.messagebox.showinfo("대륙 선택 완류",current_continent+"대륙이 적용되었습니다.")
        WTF_GUI.area_name_combobox.set("지역 선택")
    elif current_continent == "대륙 선택":
        tkinter.messagebox.showinfo("대륙 미선택","대륙을 선택 후 버튼을 눌러주세요.")
    else:
        tkinter.messagebox.showerror("오류 발생",'관리자에게 "콤보박스 오류"라고 전달해주세요.')

def open_map():
    import WTF_GUI
    current_continent = WTF_GUI.continent_name_combobox.get()
    current_area = WTF_GUI.area_name_combobox.get()
    path = WTF_info.exe_path+'/Map/'+current_continent+'/'+current_area+'.png'
    map_window = tkinter.Toplevel(WTF_GUI.main_window)
    map_window.title(current_area)
    map_window.iconbitmap(WTF_info.exe_path+'/MainFolder/icon.ico')
    map_window.wm_attributes("-topmost", 1)
    images = tkinter.PhotoImage(file=path,master=map_window)
    label = tkinter.Label(map_window, image=images)
    label.image = images
    label.pack()