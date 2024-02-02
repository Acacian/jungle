#include <stdio.h>
#include <stdlib.h>

#pragma warning (disable : 4996)

typedef struct node
{
	int value; //값을 저장하는 변수
	struct node* next; // 다음 노드의 주소를 저장
}node; //struct node = node로 만들어 줌 

node* head = NULL; //첫 노드의 주소를 저장하는 변수(포인터 변수: 8바이트, Null : 포인터가 가르키는 대상이 없는 경우)
void insertFrontNode(int data);
void insertTailNode(int data);
void displayNode();
int getNodeCount();
void removeNodeFront();
void memoryFree();
void removeNodeValue(int target);

int main()
{
	int choice;
	int data;
	int count;
	while (1)
	{
		system("cls");
		printf("\n\n  *** 단일 연결 리스트(Singly Linked List) ***\n\n");
		printf("=====================================\n");
		printf(" 1. 맨 앞 삽입\n");
		printf(" 2. 맨 뒤 삽입\n");
		printf(" 3. 앞에서부터 N번째 삽입\n");
		printf(" 4. 오름차순 정렬 삽입\n");
		printf("=====================================\n");
		printf(" 5. 맨 앞 삭제\n");
		printf(" 6. 맨 뒤 삭제\n");
		printf(" 7. 전체 노드 삭제\n");
		printf(" 8. 특정 값 삭제\n");
		printf(" 9. 앞에서부터 N번째 삭제\n");
		printf("=====================================\n");
		printf("10. 단일 연결 리스트 출력(노드 순회)\n");
		printf("11. 노드의 개수 구하기\n");
		printf("12. 노드 검색\n");
		printf(" 0. 프로그램 종료\n");
		printf("=====================================\n");
		printf("\n메뉴 선택 : ");
		scanf("%d", &choice);
		while (getchar() != '\n');

		switch (choice)
		{
		case 1:
			printf("\n\n정수 입력 : ");
			scanf("%d", &data);
			insertFrontNode(data);
			break;
		case 2:
			printf("\n\n정수 입력 : ");
			scanf("%d", &data);
			insertTailNode(data);
			break;
		case 3:
			break;
		case 4:
			break;
		case 5:
			removeNodeFront();
			break;
		case 6:
			break;
		case 7:
			memoryFree();
			break;
		case 8:
			printf("\n\n삭제할 값 입력 :");
			scanf("%d", &data);
			removeNodeValue(data);
			break;
		case 9:
			break;
		case 10:
			displayNode();
			break;
		case 11:
			count = getNodeCount(); //노드의 개수를 구해서 리턴
			printf("\n\n\t\t생성된 노드의 개수는 %d개입니다.\n", count);
			break;
		case 12:
			break;
		case 0:
			memoryFree();
			exit(0); //프로그램 강제 종료
		}//end switch

		//switch문을 빠져 나오면 일시 대기 시킨다.
		printf("\n\n\t\t");
		system("pause"); //일시 대기

	}//end while
	return 0;
}

void insertFrontNode(int data)
{
	node* newNode; // 생성된 노드의 주소를 저장하는 변수
	newNode = (node*)malloc(sizeof(node));  //노드 생성
	newNode->value = data;
	newNode->next = NULL;

	if (head == NULL) //생성된 노드가 없는 경우(첫 노드인 경우)
	{
		head = newNode;
		printf("case1. 노드 맨 앞 삽입(첫 노드로 연결)\n");
		return; //호출한 곳으로 돌아간다.(함수 종료)
	}

	newNode->next = head; // head가 Null이 아니라면 head의 값을 줘
	head = newNode;
	printf("case2. 노드 맨 앞 삽입(일반적인 경우)\n");
}

void displayNode()
{
	node* curNode; //방문한 노드의 주소를 저장하는 변수
	if (head == NULL) // 생성된 노드가 없는 경우
		return;
	system("cls"); //화면지우기, mac은 clear
	printf("\n\nSimply Linkedlist : ");

	curNode = head;
	while (curNode->next != NULL) // 이렇게 하면 마지막 노드는 절대 포함되지않음
	{
		printf("%d => ", curNode->value); //방문 노드의 값을 출력
		curNode = curNode->next; //방문 노드를 다음 노드로 이동
	}
	printf("%d\n", curNode->value); //마지막 노드 출력
}

int getNodeCount()
{
	int count = 0;
	node* curNode; //방문 노드의 주소를 저장하는 포인터
	if(head == NULL)
		return 0;

	curNode = head; //방문 노드를 첫 번째 노드로 설정
	while (curNode != NULL)
	{
		++count; //노드의 개수를 1개씩 증가
		curNode = curNode->next;
	}

	return count;
}

void removeNodeFront()
{
	node* delNode;
	//맨 앞 노드 삭제
	if (head == NULL)
		return;
	// 첫 번째 노드를 삭제할 노드로 설정
	// head를 다음 노드로 이동
	// 첫 번째 노드를 제거
	delNode = head;
	head = head->next;
	free(delNode);
	printf("\n\n\t\t모든 노드를 제거했습니다.\n"); 
}

void memoryFree()
{
	node* delNode;
	//맨 앞 노드 삭제
	if (head == NULL)
		return;

	//모든 노드 제거 : 첫 번째 노드를 제거하는것으 반복
	while (head != NULL)
	{
		delNode = head;
		head = head->next;
		free(delNode); // 대부분 앞과 동일
	}
}

void removeNodeValue(int target)
{
	node* delNode;
	node* prevNode;
	// 연결리스트가 구성되지 않은 경우
	if (head == NULL)
	{
		printf("\n\n\t\t연결리스트가 구성되지 않은 경우 삭제\n");
		return;
	}

	// 삭제할 노드가 첫 번째 노드일 경우, head가 변경되어야 함.
	if (head->value == target)
	{
		delNode = head;
		head = head->next; //head를 다음으로 이동
		free(delNode);
		printf("\n\n\t\t삭제할 노드가 첫 노드일 경우 삭제 성공\n");
		return;
	}

	//일반적인 경우(중간 삭제)
	//순회하면서 삭제할 노드 검색
	prevNode = head;
	delNode = head;
	while (prevNode->next != NULL)
	{
		delNode = prevNode->next;
		if (delNode->value == target) //삭제할 노드야?
		{
			prevNode->next = delNode->next; //연결
			free(delNode);//제거
			printf("\n\n\t\t중간 노드 삭제 성공\n");
		}
		prevNode = delNode;
	}
	 
}

void insertTailNode(int data)
{
	 node* curNode;
	 node* newNode; // 생성된 노드의 주소를 저장하는 변수
	 newNode = (node*)malloc(sizeof(node));  //노드 생성
	 newNode->value = data;
	 newNode->next = NULL;

	if (head == NULL) //연결리스트가 구성 되기 전
	{
		head = newNode;
		return; //호출한 곳으로 돌아간다.(함수 종료)
	}

	//연결리스트 순회 -> 마지막노드에 위치
	curNode = head;
	while (curNode->next != NULL)
		curNode = curNode->next;

	curNode->next = newNode;//마지막노드와 새노드를 연결

}

