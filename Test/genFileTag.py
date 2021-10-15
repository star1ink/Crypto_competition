import counting_bloom_filter


def gen_file_tag(ft_len, tag_list, p_f):
    '''

    :param ft_len:
    :param tag_list:
    :param p_f:
    :return:
    '''
    b_num = len(tag_list)
    print(b_num)
    paras = counting_bloom_filter.gen_para(ft_len, b_num, p_f)
    file_tag = counting_bloom_filter.init_bf(paras[0])
    for i in tag_list:
        counting_bloom_filter.add_to_bf(str(i), file_tag, paras)
    return file_tag

