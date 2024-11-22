import clipboard
import yaml

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
with open("Song-Introduction/config.yaml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)


# 정보
color = data['color'] # or #000

song = data['song'] # 노래 제목    ex)Wish You Were Here(노래)
song_view = data['song_view'] # 출력되는 노래 제목    ex)Wish You Were Here

artist = data['artist'] # 아티스트 명    ex)핑크 플로이드
artist_view = data['artist_view'] # 출력되는 아티스트 명    ex)Pink Floyd

link = data['link']

runningTime = data['runningTime']


# 하이라이트 가사
highlights = data['highlights']
highlights = highlights[0:-1]
highlights = highlights.split('\n')

highlights_result = []


for i in range(len(highlights)):
    if is_english_char(highlights[i][0]) == True:
        highlights_result.append("'''%s'''" %highlights[i])
    else:
        highlights_result.append("{{{-3 %s}}}" %highlights[i])

highlights_result = '\n'.join(highlights_result)



# 디자인
degree = data['degree'] # 'n'deg ex)135deg

background = []

#percent 함수 쓰기
for i in range(len(data['percent'])):
    percent(data['percent'][i][0], data['percent'][i][1])

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