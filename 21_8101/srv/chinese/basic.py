temp_sentence = input()
none = 'init'


def sentence_pattern (sentence):
    if  '?' in sentence:
        if '誰' in sentence:
            if '是' in sentence:
                start=str(sentence.find('是'))
                end=str(sentence.find('?'))
                return(sentence[int(start)+1:int(end)])
    else:
        return '敘事句或是表態句'

print(sentence_pattern(temp_sentence))