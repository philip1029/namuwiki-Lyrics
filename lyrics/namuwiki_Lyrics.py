import clipboard
import yaml

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




# YAML 파일 읽기
with open("lyrics/config.yaml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)

tablebgcolor = data['tablebgcolor'] # 최상단 테이블 색상 입력
color = data['color'] # or "#000"

album = data['album'] # 앨범 제목
file = data['file'] # 앨범 커버 파일 

song = data['song'] # 노래 제목    ex)Wish You Were Here(노래)
song_view = data['song_view'] # 출력되는 노래 제목    ex)Wish You Were Here

artist = data['artist'] # 아티스트 명    ex)핑크 플로이드
artist_view = data['artist_view'] # 출력되는 아티스트 명    ex)Pink Floyd

# composer = ["로저 워터스", "리처드 라이트(음악가)", "닉 메이슨", "데이비드 길모어"]
# composer_view = ["Roger Waters", "Richard Wright", "Nick Mason", "David Gilmour"]
composer = data['composer']
composer_view = data['composer_view']

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
lyrics = data['lyrics']
lyrics = lyrics[0:-1]
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


degree = data['degree'] # 'n'deg ex)135deg

background = []

#percent 함수 쓰기
for i in range(len(data['percent'])):
    percent(data['percent'][i][0], data['percent'][i][1])

background = ', '.join(background)

style = 'background-image: linear-gradient(%s, %s)"\n' %(degree, background)

Body = '{{{#!wiki style="margin: -5px -10px; padding: 7px 10px; %s}}} ||' %(style + lyrics_result)




result = Head + Body

clipboard.copy(result)
# print(result)
print("복사 되었습니다!")