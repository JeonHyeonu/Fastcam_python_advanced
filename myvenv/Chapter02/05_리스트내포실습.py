# word_list 에 들어있는 문자열 첫글자가
# a 인 것만 뽑아 리스트로 만드시오

word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']

# 리스트 내포 사용 X
# a_list = []

# for i in word_list:
#     if i[0] == "a":
#         a_list.append(i)
# print(a_list)

# 리스트 내포 사용 O
a_list = [i for i in word_list if i[0] == "a"]

print(a_list)