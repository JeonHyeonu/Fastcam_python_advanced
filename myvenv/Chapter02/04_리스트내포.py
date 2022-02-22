# 리스트 내포
# for 사용
# 코드 진행 순서 for > if > 표현식 > 조건을 토대로 리스트화

nums = [i for i in range(5)]
print(nums)

nums2 = [100, 200, 300]
double_nums = [i * 2 for i in nums2]
print(double_nums)

# if 사용
nums3 = [i for i in range(10) if i % 2 == 0]
print(nums3)

nums4 = [100, 200, 300, 400, 500]
double_nums2 = [i * 2 for i in nums4 if i >= 300]

"""
해석하자면 nums4 리스트 안에 있는 것들을 순서대로 i에 집어 넣을건데,
if i 가 300보다 크거나 같다면 i를 곱하기 2 해준다
nums4에서 300보다 크거나 같은 값은 300, 400, 500 이기 때문에
결과값은 600, 800, 1000이 될 것
"""

print(double_nums2)