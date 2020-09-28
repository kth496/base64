### 개요
주어진 텍스트 파일을 [Base64](https://ko.wikipedia.org/wiki/%EB%B2%A0%EC%9D%B4%EC%8A%A464) 인코딩으로 변환하는 Python 프로그램

### 구조
```
┌―― base64_codebook.py
├―― main.py
├―― README.md
└―― /data  
```

- `base64_codebook` Base64 인코딩 규칙이 담긴 딕셔너리 파일
- `main.py` Base64 인코딩 및 디코딩 시뮬레이션 전 과정이 담긴 Python 프로그램
- `/data` 시뮬레이션에 필요한 `input.txt` `output.txt` `decoded.txt` 가 담긴 폴더


### 실행 방법
1. 인코딩 하고 싶은 내용을 `input.txt`에 작성한다.

2. 터미널에서 `python main.py` 를 실행하면 `output.txt`에 결과가 기록된다.

### 개발 및 테스트 환경
Interpreter : Python 3.7

### 만든 사람
김태홍 (32131417@dankook.ac.kr)
