import clipboard

def indexing(a):
    return a[1:-1]

def hex_to_rgb(hex_str):
    # '#' 제거
    hex_str = hex_str.lstrip('#')

    # 16진수 문자열을 정수로 변환
    rgb = tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4)) + (1,)

    return "rgba" + str(rgb)
# hex_to_rgb("#FF00FF") => rgba(255, 0, 255, 1)

def percent(hex, percentage):
    background.append(hex_to_rgb(hex) + ' ' + percentage)

def is_english_char(char):
    return 'A' <= char <= 'Z' or 'a' <= char <= 'z'




# 정보란 부분

tablebgcolor = "#823A3B" # 최상단 테이블 색상 입력
color = "#FFF" # or "#000"

album = "Meddle" # 앨범 제목
file = "파일:meddle.jpg" # 앨범 커버 파일 

song = "Echoes" # 노래 제목    ex)Wish You Were Here(노래)
song_view = "Echoes" # 출력되는 노래 제목    ex)Wish You Were Here

artist = "핑크 플로이드" # 아티스트 명    ex)핑크 플로이드
artist_view = "Pink Floyd" # 출력되는 아티스트 명    ex)Pink Floyd

# composer = ["로저 워터스", "리처드 라이트(음악가)", "닉 메이슨", "데이비드 길모어"]
# composer_view = ["Roger Waters", "Richard Wright", "Nick Mason", "David Gilmour"]
composer = ["로저 워터스", "리처드 라이트(음악가)", "닉 메이슨", "데이비드 길모어"]
composer_view = ["Roger Waters", "Richard Wright", "Nick Mason", "David Gilmour"]

Head = """
||<tablebgcolor=%s><tablealign=center><tablewidth=600><color=%s>
----
{{{#!wiki style="display: inline; font-family:-apple-system, BlinkMacSystemFont, SF Pro Display, HelveticaNeue, Arial, sans serif"
{{{#!wiki style="margin: -5px -10px; display: inline-table"
||<tablebordercolor=%s><tablebgcolor=%s> {{{#!wiki style="margin: -5px 0;"
[[%s|[[%s|height=45px]]]]}}}||<color=%s>{{{#!wiki style="margin: -5px 0;"
'''{{{+1 [[%s|{{{%s %s}}}]]}}}'''[br][[%s|{{{%s %s}}}]]}}} ||}}}}}}
----

""" % (tablebgcolor, color, tablebgcolor, tablebgcolor, album, file, color, song, color, song_view, artist, color, artist_view)

Head = indexing(Head)




# 가사 부분
# 일반 줄 구분은 엔터 한 번, 간주는 엔터 두 번

# 왼쪽 텍스트를 만들기 위해서는 아래 텍스트를 추가해야 함.
# {{{#!wiki style="text-align:right"
# (가사)
# (가사))}}}
lyrics = """
Overhead the albatross
머리 위의 알바트로스 
Hangs motionless upon the air
공중에 가만히 매달려 있네
And deep beneath the rolling waves
그리고 굽이치는 파도 아래 깊은 곳
In labyrinths of coral caves
산호 동굴의 미궁 안에서
The echo of a distant time
머나먼 시간의 메아리가
Comes willowing across the sand
모래를 가로질러 나부끼듯 건너오고
And everything is green and submarine
모든 것은 푸르게 물들어 바다 아래 잠겼네

And no one showed us to the land
누구도 우리를 육지로 안내하지 않았고
And no one knows the where's or why's
누구도 어디인지 왜인지 모른 채
Something stirs and something tries
무언가는 꿈틀대며, 무언가는 노력하여
Starts to climb toward the light
빛을 향해 기어오르기 시작하네 


Strangers passing in the street
거리에서 스쳐가는 낯선 사람들
By chance two separate glances meet
우연히 두 시선이 교차하네
And I am you and what I see is me
나는 그대이며 내가 보는 것은 나
And do I take you by the hand
그리고 나는 그대의 손을 맞잡아
And lead you through the land
뭍을 가로질러 그대를 이끌어
And help me understand
이해할 수 있게 도와주네
The best I can
내가 할 수 있는 한

And no one calls us to move on
누구도 우리에게 움직이라 하지 않고
And no one forces down our eyes
누구도 우리의 눈을 가리려 하지 않고
No one speaks and no one tries
누구도 입을 열지 않고, 누구도 시도하지 않으며
No one flies around the sun
누구도 태양의 주변을 날아다니지 않네


Cloudless everyday
구름 한 점 없는 나날 속
You fall upon my waking eyes
그대는 나의 뜬 눈 위로 떨어지며
Inviting and inciting me
유혹하고 선동하여[* [[비틀즈]]의 노래 [[Across the Universe]]의 가사에서 따온 구절이다.]
To rise
날 일깨우네
And through the window in the wall
그리고 벽의 창문 너머로
Come streaming in on sunlight wings
아침을 알리는 수백만의 찬란한
A million bright ambassadors of morning
햇살의 날개들이 흘러들어오네

And no one sings me lullabies
누구도 내게 자장가를 불러 주지 않고
And no one makes me close my eyes
누구도 내 눈을 감겨 주지 않네
So I throw the windows wide
그렇기에 나는 창문을 크게 열어젖히며
And call to you across the sky
하늘을 가로질러 그대를 부르네
"""
lyrics = indexing(lyrics)
lyrics = lyrics.split('\n')

# print(lyrics)
lyrics_result = []

for i in range(len(lyrics)):
    if lyrics[i] == "":
        if lyrics[i+1] == "":
            lyrics_result.append("")
            lyrics_result.append("● ● ●")
        else:
            lyrics_result.append("")
    elif is_english_char(lyrics[i][0]) == True:
        if "[" in lyrics[i]:
            start_index = lyrics[i].find("[")
            before_bracket = lyrics[i][:start_index]  # '[' 이전 부분
            after_bracket = lyrics[i][start_index:]  # '[' 포함 이후 부분
            formatted = f"{{{{+1 '''{before_bracket.strip()}'''}}}}{after_bracket}"  # 원하는 형식으로 결합
            lyrics_result.append(formatted)
        else:
            lyrics_result.append("{{{+1 '''%s'''}}}" %lyrics[i])
    else:
        lyrics_result.append(lyrics[i])

author = ""
for i in range(len(composer)):
    author = '[[%s|{{{%s %s}}}]], ' %(composer[i], color, composer_view[i]) + author
author = author[0:-2]

lyrics_result = '\n'.join(lyrics_result)
lyrics_result = """
{{{#!wiki style="display: inline; font-family:-apple-system, BlinkMacSystemFont, SF Pro Display, HelveticaNeue, Arial, sans serif"
{{{#!wiki style="word-break: normal"
%s

'''Written By:''' %s
}}}}}}
""" %(lyrics_result, author)
lyrics_result = indexing(lyrics_result)

# print(lyrics_result)
# clipboard.copy(lyrics_result)


degree = "160deg" # 'n'deg ex)135deg

background = []

#percent 함수 쓰기
percent("823A3B", "0%")
percent("703536", "32%")
percent("7B8493", "60%")
percent("264F57", "100%")

background = ', '.join(background)

style = 'background-image: linear-gradient(%s, %s)"\n' %(degree, background)

Body = '{{{#!wiki style="margin: -5px -10px; padding: 7px 10px; %s}}} ||' %(style + lyrics_result)




result = Head + Body

clipboard.copy(result)
# print(result)
print("복사 되었습니다!")