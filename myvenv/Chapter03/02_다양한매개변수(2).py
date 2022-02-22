# 1. 위치 가변 매개변수
def print_fruits(*args):
    for arg in args:
        print(arg)

print_fruits("apple", "orange", "mango", "banana")

# 2. 키워드 가변 매개변수
def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

comment_info(name="유재석", content="이번주는 유퀴즈")

# 매개변수 작성 순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변

def post_info(title, content, *tags):
    print(f"제목 :  {title}")
    print(f"내용 :  {content}")
    print(f"태그 :  {tags}")

post_info("파이썬 함수 정리", "다양한 매개변수", "#파이썬", "#함수")