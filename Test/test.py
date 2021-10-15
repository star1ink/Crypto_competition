import genFileTag
import fileread

filename = open("123.png", 'rb')
file_str = filename.read()
file_block_list = fileread.file_chunk(file_str)
file_tag = genFileTag.gen_file_tag(file_str, file_block_list, 10 ** (-3))
print(file_tag)

