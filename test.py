def func(self):
    s_list = s.split()
    for i in range(len(s_list)):
        s_list[i] = s_list[i][::-1]
    s_word = ' '.join(s_list)
    return(s_word)

def test_answer(s_word):
    s_list = s_word.split()
    for i in range(len(s_list)):
        s_list[i] = s_list[i][::-1]
    print(' '.join(s_list))
    return s == ' '.join(s_list)

s="Let's take LeetCode contest"
print(func(s))
print(test_answer(func(s)))