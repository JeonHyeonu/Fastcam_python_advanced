# None 에 해당되는 값은 모두 빈 문자열로 표시


cr_list = ["오메가3", None, "비타민C500", None, "홍삼절편"]

# 리스트 내포 사용 X
# result = []

# for i in cr_list:
#     if i != None:
#         result.append(i)
#     else:
#         result.append('')
# print(result)

result = [i if i != None else '' for i in cr_list]
print(result)