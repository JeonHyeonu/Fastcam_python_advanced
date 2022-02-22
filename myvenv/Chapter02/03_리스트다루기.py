# 리스트 메서드

# 리스트 데이터 삭제
fruits = ["apple", "orange", "mango"]
fruits.remove("apple")
print(fruits)

# 리스트 정렬
nums = [5, 1, 2, 8, 3]
nums.sort()
print(nums)

# enumerate

titles = ["출석", "인증하기", "자유게시판"]

for index, title in enumerate(titles, 1): # 인덱스의 시작번호를 1번으로 지정
    print(f"{index}번째 메뉴입니다. 제목 : {title}")