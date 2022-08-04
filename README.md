# MusicParser Library

음원 사이트로부터 음반 정보를 읽어 parsing 하는 라이브러리입니다.

지원하는 사이트는 다음과 같습니다. 

* Bugs
* AllMusic
* ~~Naver Music~~ (VIBE로 변경되어 미지원)
* Melon

## 설치 방법

### `pip`으로 바로 설치

```
$ pip install git+https://github.com/rubysoho07/MusicParser.git
```

### `requirements.txt` 파일에 넣을 때

```
git+https://github.com/rubysoho07/MusicParser.git
```

### 특정 버전을 지정할 때 

URL 끝에 `@버전`을 넣습니다.

예) 0.0.4 버전인 경우

```
$ pip install git+https://github.com/rubysoho07/MusicParser.git@0.0.4
```

## 사용 방법

### 지원하는 모든 사이트에서 Parsing 하려는 경우

```python
from MusicParser.parser import MusicParser

parser = MusicParser()

# 결과를 JSON 문자열로 받고 싶은 경우
result_json = parser.to_json('Album 정보가 있는 URL')

# 결과를 Dict로 받고 싶은 경우
result_dict = parser.to_dict('Album 정보가 있는 URL')
```

### 특정 사이트를 지정해서 Parsing 하려는 경우

지원하는 사이트에 따른 Parser 종류는 다음과 같습니다.

* Bugs: `BugsParser`
* AllMusic: `AllMusicParser`
* Naver Music: `NaverMusicParser`
* Melon: `MelonParser`

다음과 같이 Parsing을 진행하면 됩니다. 아래 예제는 Bugs에서 앨범 정보를 Parsing 하는 경우입니다.

```python
from MusicParser.parser import BugsParser

bugs_parser = BugsParser()

# 결과를 JSON 문자열로 받고 싶은 경우
result_json = bugs_parser.to_json('Album 정보가 있는 URL')

# 결과를 Dict로 받고 싶은 경우
result_dict = bugs_parser.to_dict('Album 정보가 있는 URL')
```