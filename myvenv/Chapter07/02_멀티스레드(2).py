import threading
import time

# 주식 자동매매
# 매수, 매도

# 매수 스레드
def buyer():
    for i in range(5):
        print('[매수] 데이터 요청 중...')
        time.sleep(1)
        print('[매수] 데이터 요청 중...')
        time.sleep(1)
        print('[매수] 매수 타이밍!')
        time.sleep(1)
        print('[매수] 풀매수!!')
        time.sleep(1)

# 매도 스레드
def saler():
    for i in range(5):
        print('[매도] 데이터 요청 중...')
        time.sleep(1)
        print('[매도] 데이터 요청 중...')
        time.sleep(1)
        print('[매도] 매도 타이밍!')
        time.sleep(1)
        print('[매도] 풀매도!!')
        time.sleep(1)

print('[메인] start')
buyer = threading.Thread(target=buyer)
saler = threading.Thread(target=saler)
buyer.start()
saler.start()


buyer.join() # 매수 스레드가 종료될 때까지 메인 스레드가 기다림
saler.join() # 매도 스레드가 종료될 때까지 메인 스레드가 기다림
print('[메인] 장이 종료되었습니다.')