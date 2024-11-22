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




# 정보
color = "#fff" # or #000

song = "Echoes" # 노래 제목    ex)Wish You Were Here(노래)
song_view = "Echoes" # 출력되는 노래 제목    ex)Wish You Were Here

artist = "핑크 플로이드" # 아티스트 명    ex)핑크 플로이드
artist_view = "Pink Floyd" # 출력되는 아티스트 명    ex)Pink Floyd

link = "53N99Nim6WE"

runningTime = "23:33"


# 하이라이트 가사
highlights = """
Strangers passing in the street
거리에서 스쳐가는 낯선 사람들
By chance two separate glances meet
우연히 두 시선이 교차하네
And I am you and what I see is me
그리고 나는 그대이며 내가 보는 것은 나
"""
highlights = indexing(highlights)
highlights = highlights.split('\n')

highlights_result = []


for i in range(len(highlights)):
    if is_english_char(highlights[i][0]) == True:
        highlights_result.append("'''%s'''" %highlights[i])
    else:
        highlights_result.append("{{{-3 %s}}}" %highlights[i])

highlights_result = '\n'.join(highlights_result)



# 디자인
degree = "160deg" # 'n'deg ex)135deg

background = []

percent("823A3B", "0%")
percent("703536", "32%")
percent("7B8493", "60%")
percent("264F57", "100%")

background = ', '.join(background)




result = """
[youtube(%s)]

{{{#!wiki style="width: 340px; background-image: linear-gradient(%s, %s); border-radius: 15px; padding: 1em 1em 1em 1em"
{{{#!wiki style="display: inline; font-family:-apple-system, BlinkMacSystemFont, SF Pro Display, HelveticaNeue, Arial, sans serif"
{{{#!wiki style="word-break: normal"
{{{%s
%s{{{#!wiki style="float: right; margin-right: .5em; margin-top: 1.2em; font-size: .6em"
{{{%s %s}}}}}}
{{{#!wiki style="margin: 10px 0 0 0"
[include(틀:색상 수평줄, 색상=#fff)]
}}}
{{{#!wiki style="margin: -30px 0 0 0"
{{{-2 '''[[%s|{{{%s %s}}}]]'''}}}
{{{-3 [[%s|{{{%s %s}}}]]}}}}}}
}}}}}}}}}}}}
""" %(link, degree, background, color, highlights_result, color, runningTime, song, color, song_view, artist, color, artist_view)

clipboard.copy(result)
# print(result)
print("복사 되었습니다!")