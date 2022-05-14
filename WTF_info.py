# -*- Encoding:UTF-8 -*- #
### 코드를 무단으로 복제,개조 및 배포하지 말 것 ###
### Copyright ⓒ 2021-2022 c-closed / 감는 my______baby@naver.com ###
import os
from string import ascii_uppercase

current_version = 'v1.1.1'
homepage_url = 'http://github.com/c-closed/Wandering-Trader-Finder'
latest_release_url = 'http://github.com/c-closed/Wandering-Trader-Finder/releases/latest'
update_check_url = 'https://api.github.com/repos/c-closed/Wandering-Trader-Finder/releases/latest'

real_path = os.getcwd()
exe_path = real_path.replace('\\', '/')

continent_name_list = ['아르테미스','유디아','루테란 서부','루테란 동부','토토이크','애니츠','아르데타인','베른 북부','슈샤이어','로헨델','욘','페이튼','파푸니카','베른 남부','로웬','엘가시아','플레체','볼다이크']
arthemis_area_list = ['국경지대','로그힐','안게모스 산 기슭']
eudia_area_list = ['살란드 구릉지','오즈혼 구릉지']
luterra_west_area_list = ['격전의 평야','레이크바','메드리닉 수도원','빌브린 숲','자고라스 산']
luterra_east_area_list = ['디오리카 평원','라이아 단구','배꽃나무 자생지','보레아 영지','크로커니스 해변','해무리 언덕','흑장미 교회당']
tortoyk_area_list = ['달콤한 숲','바다향기 숲','성큼바위 숲','침묵하는 거인의 숲']
anihc_area_list = ['거울 계곡','델파이 현','등나무 언덕','소리의 숲','황혼의 연무']
arthetine_area_list = ['갈라진 땅','네벨호른','리제 폭포','메마른 통로','바람결 구릉지','토트리치']
vern_north_area_list = ['발란카르 산맥','베르닐 삼림','크로나 항구','파르나 숲','페스나르 고원']
shushire_area_list = ['머무른 시간의 호수','서리감옥 고원','얼어붙은 바다','얼음나비 절벽','칼날바람 언덕']
rohendel_area_list = ['바람향기 언덕','엘조윈의 그늘','유리연꽃 호수','은빛 물결 호수','파괴된 제나일']
yorn_area_list = ['검은모루 작업장','기약의 땅','무쇠망치 작업장','미완의 정원','시작의 땅']
feiton_area_list = ['칼라자 마을']
papunika_area_list = ['별모래 해변','비밀의 숲','얕은 바닷길','티카티카 군락지']
vern_south_area_list = ['벨리온 유적지','칸다리아 영지']
lowen_area_list = ['어금니의 강','웅크린 늑대의 땅']
elgacia_area_list = ['필레니소스 산','헤스테라 정원']
pletze_area_list = ['미구현']
voldaik_area_list = ['미구현']