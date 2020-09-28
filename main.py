def txt_to_string_arr(file_path):
    """
    txt_to_string_arr

    :param file_path: 파일 주소 string 임
    :return: (1D-array) string 배열
    """
    f = open(file_path, 'r')
    ret = []
    while True:
        line = f.readline()
        if not line:
            break
        ret.append(line)
    f.close()
    return ret


def str_arr_to_ascii_binary_arr(string_array):
    """
    str_arr_to_ascii_binary_arr
    주어진 string 배열을 문자 단위로 접근해서 바이너리로 변환한다.

    내장함수 ord 는 주어진 문자의 아스키코드 값을 리턴한다.
    내장함수 bin 은 주어진 값의 바이너리 표현을 리턴한다.
    이때 접두사로 '0b'가 붙으며, 표현 자릿수가 고정되지 않는다.
    따라서 왼쪽에 0을 필요한만큼 추가해서 8비트 표현으로 만든다.

    :param string_array: string 배열
    :return: (1D-array) string 배열
    """
    ret = []
    for line in string_array:
        binary_line = ""
        for char in line:
            char_to_binary = bin(ord(char))[2:].zfill(8)
            binary_line += char_to_binary
        ret.append(binary_line)
    return ret


def concat_binary_arr_with_zero_fill(binary_array):
    """
    concat_binary_arr_with_zero_fill
    주어진 바이너리 배열을 하나의 string 으로 합친다.
    이때, 길이가 3의 배수가 아니라면, 필요한 만큼 0을 붙인다.

    :param binary_array: string 배열
    :return: (string) string
    """
    ret = ""
    for line in binary_array:
        ret += line
    while len(ret) % 3 != 0:
        ret += '0'
    return ret


def convert_raw_to_base64(raw_data):
    """
    convert_raw_to_base64
    주어진 바이너리 string 을 base64 string 으로 변환한다.

    인자로 전달받는 string 의 길이가 3의 배수임이 보장된다.
    따라서 6개 문자씩 앞에서부터 잘라내고, 그 값을 정수로
    변환한다음, base64 문자 표에서 찾으면 된다.

    :param raw_data: 바이너리로 표현 문자열
    :return: (string) string
    """

    # 코드북에 대한 내용은 base64_codebook 파일 참고
    from base64_codebook import base64_dictionary
    base64_table = list(base64_dictionary)

    ret = ""
    while len(raw_data) > 0:
        snip = raw_data[:6]
        raw_data = raw_data[6:]
        idx = int(snip, 2)
        ret += base64_table[idx]

    return ret


def save_string_to_txt(string, path):
    """
    save_string_to_txt

    :param string: 저장하려는 string
    :param path: 저장할 경로
    :return: None
    """
    f = open(path, 'w')
    f.write(string)
    f.close()
    return


def decode_base64(string):
    """
    decode_base64
    base64 표현 문자열을 디코딩한다.

    주어진 string 을 문자단위로 접근해서 6자리 바이너리 표현으로 바꾼다.
    이런식으로 모든 내용을 변환해서 binary_exp 를 만든다.
    이때 주의할 점은, 해당 문자를 곧장 아스키 바이너리 표현으로 바꾸면 안된다.
    가령 base64 string 에 등장하는 'A'는 0b000000 으로 표현되어야한다.

    변환 과정에서 약간의 디테일만 다를뿐, 인코딩과 디코딩을 사실상 동일하다.

    :param string: 디코딩 할 string
    :return: (string) 디코딩 된 string
    """

    # 코드북에 대한 내용은 base64_codebook 파일 참고
    from base64_codebook import base64_dictionary

    binary_exp = ""
    for char in string:
        val = base64_dictionary[char]
        binary_exp += bin(val)[2:].zfill(6)

    ret = ""
    while len(binary_exp) >= 8:
        snip = binary_exp[:8]
        binary_exp = binary_exp[8:]
        ret += chr(int(snip, 2))
    return ret


def main():
    """
    Main

    메인 함수는 Base64 인코딩의 모든 과정을 실행하는 역할을 한다.
    C 언어의 구조처럼 만들기 위해 도입했음.
    :return: None
    """

    # input.txt 파일을 읽어서 string 배열로 자장함
    str_array = txt_to_string_arr('data/input.txt')

    # string 배열을 binary 표현 배열로 변환함
    binary_array = str_arr_to_ascii_binary_arr(str_array)

    # binary 배열을 하나의 string 로 합침.
    # 길이가 3의 배수가 되게 뒤에 0을 추가함
    raw_binary_data = concat_binary_arr_with_zero_fill(binary_array)

    # binary string 을 base64 인코딩함
    base64_result = convert_raw_to_base64(raw_binary_data)

    # 결과 출력
    print(base64_result)

    # 결과 저장
    save_string_to_txt(base64_result, 'data/output.txt')

    # base64를 디코딩하기
    decoded_string = decode_base64(base64_result)

    # 디코딩 결과 출력 및 저장
    print(decoded_string)
    save_string_to_txt(decoded_string, 'data/decoded.txt')


if __name__ == '__main__':
    main()
