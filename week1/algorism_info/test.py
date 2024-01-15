class MyQueue:
    def __init__(self):
        self.front = self.rear = -1
        # rear이 -1부터 시작해서 뭐 더 못 넣음
        self.queue = [0] * 5
    def enqueue(self,data):
        # 제일 뒤에 삽입
        if self.is_full():
            print('큐가 다 찼습니다.')
        else:
            self.rear += 1
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
queue.enqueue(7)
queue.enqueue(8)

print(queue.dequeue())