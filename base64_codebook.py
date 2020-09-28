"""
base64_dictionary

base64 코드값 규칙이 들어있는 dictionary 이다.
배열이 아니라 dictionary 로 만든 이유는, 인코딩 과정은 배열로 해결되지만
디코딩 과정은 역방향 참조가 필요하기 때문이다.

예를 들어, 인코딩 과정에서 바이너리 표현을 6자리로 자른 후 decimal 로
변환했을 때 5가 나오면, 'F'를 기록하면 된다.

하지만 디코딩 과정은 숫자가 아니라 문자를 역으로 변환해야 한다.
디코딩 과정에서 문자 'F'가 등장하면 이를 5로 바꾸고,
5를 다시 바이너리 표현으로 변환하는 과정이 필요하다.
만약 ['A', 'B', 'C', ...] 형태의 배열만 존재한다면,
'F' 라는 문자가 등장할때까지 배열을 순회하면서 인덱스값을 모두 탐색해야한다.
배열 사이즈가 크지 않지만, 본질적으로 O(1)에 가능할 일을 O(n)으로 하게 된다.

이와 같은 이유로 코드북을 딕셔너리로 만들었다. Python 3 딕셔너리는 기본적으로
순서가 보장되기 때문에, 약간의 변형을 거치면 바로 배열처럼 쓸 수 있다.
인코딩 과정에서는 배열로 변환해서 쓰고, 디코딩 과정에는 사전처럼 사용하면 된다.
"""

base64_dictionary = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
    'a': 26,
    'b': 27,
    'c': 28,
    'd': 29,
    'e': 30,
    'f': 31,
    'g': 32,
    'h': 33,
    'i': 34,
    'j': 35,
    'k': 36,
    'l': 37,
    'm': 38,
    'n': 39,
    'o': 40,
    'p': 41,
    'q': 42,
    'r': 43,
    's': 44,
    't': 45,
    'u': 46,
    'v': 47,
    'w': 48,
    'x': 49,
    'y': 50,
    'z': 51,
    '0': 52,
    '1': 53,
    '2': 54,
    '3': 55,
    '4': 56,
    '5': 57,
    '6': 58,
    '7': 59,
    '8': 60,
    '9': 61,
    '+': 62,
    '/': 63,
}
