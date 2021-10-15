def file_chunk(Str, size=20):
    '''

    :param Str: String
    the binary file string
    :param size: int
    sliding window size
    :return: list
    a list of chunked binary file strings
    '''
    chunking = []
    max_value = Str[0]
    max_index = 0
    last_index = -1
    for i in range(len(Str)):
        if Str[i] > max_value:
            max_index = i
            max_value = Str[i]
        else:
            if (i - max_index) == size:
                chunking.append(Str[last_index + 1:i])
                last_index = i
                max_index = i + 1
                max_value = Str[max_index]
            elif i == len(Str) - 1:
                chunking.append(Str[last_index + 1:i])
    return chunking


if __name__ == '__main__':
    filename = open("123.png", 'rb')
    file_str = filename.read()
    print(file_chunk(file_str)[0])
    print(help(file_chunk))
