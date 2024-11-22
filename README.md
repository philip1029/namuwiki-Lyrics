# Namuwiki Lyrics Formatter

이 프로젝트는 나무위키에서 사용할 수 있도록 노래 가사와 관련 정보를 예쁘게 편집할 수 있게 돕는 프로그램입니다. 사용자가 입력한 정보(앨범, 노래 제목, 아티스트 등)와 가사를 바탕으로, 나무위키 문서에서 잘 보이도록 포맷팅된 텍스트를 생성하여 클립보드에 복사해 줍니다.

또한, 이 프로그램은 노래의 하이라이트 가사를 포함한 노래를 간략하게 소개할 수 있는 텍스트를 생성하는 프로그램도 함께 있습니다.

# 사용법
파이썬3 설치는 했다고 가정합니다.

우선 `setting.py`를 실행하여 `namuwiki_Lyrics.py`와 `namuwiki_Song-Introduction.py`를 실행할 떄 필요한 모듈을 설치해 주어야합니다.

```
python3 setting.py
```

## namuwiki_Lyrics
먼저 `lyrics/config.yaml` 파일에 필요한 정보를 입력합니다. 이 파일에서 앨범 제목, 노래 제목, 아티스트, 가사 등을 설정할 수 있습니다. 쌍따옴표 안에 각 주석이 설명하는 값들을 넣어주세요!

모두 입력하였다면 `lyrics/namuwiki_Lyrics.py` 파일을 실행해줍니다.
```
python3 lyrics/namuwiki_Lyrics.py
```
프로그램을 실행하면, 입력한 데이터를 바탕으로 나무위키에서 사용할 수 있는 포맷팅된 텍스트가 클립보드에 복사됩니다.

## namuwiki_Song-Introduction
마찬가지로 `Song-Introduction/config.yaml` 파일에 필요한 정보를 입력합니다. 쌍따옴표 안에 각 주석이 설명하는 값들을 넣어주세요!!

모두 입력하였다면 `Song-Introduction/namuwiki_Song-Introduction.py` 파일을 실행해줍니다.
```
python3 Song-Introduction/namuwiki_Song-Introduction.py
```
프로그램을 실행하면, 입력한 데이터를 바탕으로 나무위키에서 사용할 수 있는 포맷팅된 텍스트가 클립보드에 복사됩니다.

# 기여
이 프로젝트는 누구나 기여할 수 있습니다. 기능 추가나 버그 수정 등의 기여를 원하시면 PR을 보내 주세요!