# 스텍이랑 다르게 선입선출 형태(먼저 들어간 데이터가 먼저 나온다)

# (1) Enqueue : 큐 맨 뒤에 어떠한 요소를 추가, 마지막으로 온 손님에게 번호표 발부
# (2) Dequeue : 큐 맨 앞쪽의 요소를 삭제, 창구에서 서비스를 받은 손님의 번호표를 대기목록에서 삭
# (3) Peek : front에 위치한 데이터를 읽음, 다음 서비스를 받을 손님이 누구인지 확인
# (4) front : 큐의 맨 앞의 위치(인덱스), 다음 서비스를 받을 손님의 번호
# (5) rear : 큐의 맨 뒤의 위치(인덱스), 마지막에 온 손님의 번호

# 큐 예시
queue = []

def push(value):
    queue.append(value)
    print(f"Pushed {value} into the queue.")

def pop():
    if not queue:
        print("Queue is empty. Cannot pop.")
    else:
        value = queue.pop(0)
        print(f"Popped {value} from the queue.")

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter a value to push: "))
        push(value)
    elif choice == 2:
        pop()
    elif choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose again.")

# 배열 큐 << append 이상은 암것도 못함 << 맨 앞과 맨 뒤를 기억 못하기 때문
# 예를 들어 데이터를 빼낼 때, 그대로 있는 front까지 rear부터 계속 한 칸씩 당겨야함.
# 그럼 front를 옮기면 안됨? 되는데, 그럼 배열이 꽉 차면 데이터를 더 못 넣음.
# 그래서 나온 게 원형 큐
# rear는 다시는 0으로 못 돌아가면 원형 큐다.
class MyQueue:
    def __init__(self):
        self.front = self.rear = -1
        # rear이 -1부터 시작해서 뭐 더 못 넣음
        # 차이점 1
        self.queue = [0] * 5
    def enqueue(self,data):
        # 제일 뒤에 삽입
        if self.is_full():
            print('큐가 다 찼습니다.')
        else:
            self.rear += 1
        # 차이점 2 < rear 와 프론트가 같이 이동함
        # rear를 뒤로 한 칸 이동시키고, 그 자리에 data를 삽입
            self.queue[self.rear] = data

    def dequeue(self):
        # 현재 가장 앞에 있는 요소를 반환하고 (삭제)
        if self.is_empty():
            print('큐가 비었습니다.')
        else:
            self.front += 1
        # front를 뒤로 한 칸 이동시키고, 그 자리에 있던(맨 앞) 요소를 반환
            return self.queue[self.front]

    def is_full(self):
        if self.rear == len(self.queue)-1:
            return True
        else:
            return False

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5) # 가득 참
queue.enqueue(6) # 곽차서 못 들어감

print(queue.dequeue())
# 해결법은 맨 앞부분으로 계속 넘겨 연산하는 방법이 있으나 효율성 쓰레기
            
# 원형 큐 < 포화, 공백을 구분하기 위해 첫 란은 비워두고 그 다음부터 채움.
class CircleQueue:
    def __init__(self):
        self.front = self.rear = 0
        self.queue = [0] * 5
    def enqueue(self,data):
        # 제일 뒤에 삽입
        if self.is_full():
            print('큐가 다 찼습니다.')
        else:
            # self가 같이 이동하는 게 아니라 self.rear만 이동함
            self.rear  = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = data

    def dequeue(self):
        # 현재 가장 앞에 있는 요소를 반환하고 (삭제)
        if self.is_empty():
            print('큐가 비었습니다.')
        else:
            self.front = (self.front + 1) % len(self.queue)
            return self.queue[self.front]

    def is_full(self):
        if (self.rear + 1) % len(self.queue) == self.front:
            return True
        else:
            return False

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
