import numpy as np

MIN_VALUE = 0.75


def sim_Text(f_tag_1, f_tag_2):
    if len(f_tag_1) != len(f_tag_2):
        return MIN_VALUE
    else:
        return np.dot(f_tag_1, f_tag_2) / (np.linalg.norm(f_tag_1) * (np.linalg.norm(f_tag_2)))

