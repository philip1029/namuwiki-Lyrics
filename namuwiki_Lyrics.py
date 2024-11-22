import clipboard

def indexing(a):
    return a[1:-1]

def is_english_char(char):
    return 'A' <= char <= 'Z' or 'a' <= char <= 'z'




# 정보란 부분

tablebgcolor = "#823A3B" # 최상단 테이블 색상 입력
color = "#FFF" # or "#000"

album = "Meddle" # 앨범 제목
file = "파일:meddle.jpg" # 앨범 커버 파일 

song = "One of These Days" # 노래 제목    ex)Wish You Were Here(노래)
song_view = "One of These Days" # 출력되는 노래 제목    ex)Wish You Were Here

artist = "핑크 플로이드" # 아티스트 명    ex)핑크 플로이드
artist_view = "Pink Floyd" # 출력되는 아티스트 명    ex)Pink Floyd

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
lyrics = """
One of these days, I’m going to cut you into little pieces
언젠가는, 너를 조각조각 잘라버릴 거야
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





# 여긴 알아서 바꿔라
style = """background-image: linear-gradient(160deg, rgba(130, 58, 59, 1) 0%, rgba(112, 53, 54, 1) 32%, rgba(123,132,147,1) 60%, rgba(38, 79, 87, 1) 100%)"
"""

Body = '{{{#!wiki style="margin: -5px -10px; padding: 7px 10px; ' + style + lyrics_result + '}}} ||'




result = Head + Body

clipboard.copy(result)
print(result)
print("\n복사 되었습니다!")