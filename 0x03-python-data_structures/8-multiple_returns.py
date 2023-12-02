#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        sen_lenvrb = len(sentence)
    else:
        sen_lenvrb = 0
    return (sen_lenvrb, sentence if not sentence else sentence[:1])
