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

song = "A Pillow of Winds" # 노래 제목    ex)Wish You Were Here(노래)
song_view = "A Pillow of Winds" # 출력되는 노래 제목    ex)Wish You Were Here

artist = "핑크 플로이드" # 아티스트 명    ex)핑크 플로이드
artist_view = "Pink Floyd" # 출력되는 아티스트 명    ex)Pink Floyd

# composer = ["로저 워터스", "리처드 라이트(음악가)", "닉 메이슨", "데이비드 길모어"]
# composer_view = ["Roger Waters", "Richard Wright", "Nick Mason", "David Gilmour"]
composer = ["로저 워터스", "데이비드 길모어"]
composer_view = ["Roger Waters", "David Gilmour"]

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
lyrics = """
A cloud of eiderdown
구름 같은 깃털 이불이
Draws around me
나를 감싸고 있어
Softening the sound
소리를 죽이면서

Sleepy time, when I lie
잠이 올 때, 내가 누우면
With my love by my side
내 사랑을 옆에 두고서
And she’s breathing low
그리고 그녀는 조용히 숨쉬지

And the candle dies
그리고 촛불은 꺼져가


When night comes down, you lock the door
밤이 오면, 너는 문을 잠가
The book falls to the floor
책이 바닥으로 떨어지지

As darkness falls and waves roll by
어둠이 지고 파도가 치면
The seasons change, the wind is warm
계절이 바뀌고, 바람은 따스해지지

Now wakes the owl, now sleeps the swan
올빼미는 깨어나고, 백조는 잠에 들어 
Behold a dream, the dream is gone
꿈을 꾸자니, 꿈은 사라졌지

Green fields, a cold rain is falling
푸른 들판에 차가운 비가 내려
In a golden dawn
금빛의 새벽녘에


And deep beneath the ground
그리고 땅속 깊은 곳에서
The early morning sounds
이른 아침의 소리가 들려오지
And I go down
그리고 나는 잠겨가

Sleepy time, when I lie
잠이 올 때, 내가 누우면
With my love by my side
내 사랑을 옆에 두고서
And she’s breathing low
그리고 그녀는 조용히 숨쉬지

And I rise, like a bird
그리고 나는 떠올라, 새처럼
In the haze, when the first rays
안개 속에서, 첫 햇살이
Touch the sky
하늘에 닿을 때

And the night winds die
그리고 밤의 바람은 사라져
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