#include <stdio.h>
#include <stdlib.h> //malloc �޾ƾ��ؼ� ����

typedef char data;
typedef struct _Node {
	char key;
	struct _Node* left;
	struct _Node* right;
}Node;

Node * searchBST(Node * root, char x) {
	Node* p = root;
	while (p != NULL) {
		if (p->key == x)
			return p;
		else if (p->key < x)
			p = p->right;
		else
			p = p->left;
	}
	return(NULL);
}

Node* insertBST(Node* root, char x) {
	Node* p = root;
	Node* parent = NULL;
	while (p != NULL) {
		parent = p;
		if (p->key == x)
			return p;
		else if (p->key < x)
			p = p->right;
		else
			p = p->left;
	}

	//�� ��� �Ҵ�
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->key = x;
	newNode->left = newNode->right = NULL;

	// parent�� �ڽ����� �� ��� ���̱�
	if (parent != NULL) {
		if (parent->key < newNode->key)
			parent->right = newNode;
		else
			parent->left = newNode;
	}
	return newNode; 
}

Node* deleteBST(Node* root, char x) {
	Node* p = root;
	Node* parent = NULL;
	while ((p != NULL) && (p->key == x)) {
		parent = p;
		if (p->key == x)
			return p;
		else if (p->key < x)
			p = p->right;
		else
			p = p->left;
	}
	if (p == NULL) {
		printf("ã�� ��� X \n");
		return root;
	}

	if (p->left == NULL && p->right == NULL) { // ���� 0
		if (parent == NULL)
			root = NULL;
		else {
			if (parent->left == p)
				parent->left = NULL;
			else
				parent->right = NULL;
		} 
	}
	else if (p->left == NULL || p->right == NULL) { //���� 1
		Node* child = (p->left != NULL) ? p->left : p->right;
		if (parent == NULL)
			root = child;
		else
			if (parent->left == p)
				parent->left =  NULL;
			else
				parent->right = NULL;
	}

	else { //������ 2
		Node* succ_parent = p;
		Node* succ = p->right;
		while (succ->left != NULL) {
			succ_parent = succ;
			succ = succ->left;
		}
		p->key = succ->key;
		if (succ_parent->left == succ)
			succ_parent->left = succ->right;
		else
			succ_parent->right = succ->right;
		p = succ;
	}

	free(p);
	return root;
}

void Inorder(Node* root) {
	if (root == NULL)
		return;
	Inorder(root->left);
	printf("%c", root->key);
	Inorder(root->right);
}
int main() {
	Node* root = insertBST(NULL, 'D');
	insertBST(root, 'I');
	insertBST(root, 'F');
	insertBST(root, 'A');
	insertBST(root, 'G');
	insertBST(root, 'C');
	inorder(root); printf("\n");
	return 0;
}