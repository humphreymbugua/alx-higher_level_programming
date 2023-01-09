#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len == 0:
        char_str = None
    else:
        char_str = sentence[0]
    tpl_val = (str_len, char_str)
    return (tpl_val)
