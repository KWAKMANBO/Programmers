class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = root
        self.current_node = None

    def insert(self, value):
        # 현재 노드를 루트로 초기화
        self.current_node = self.root
        while True:
            # 삽입하려는 값이 현재 노드의 값보다 작다면
            if value < self.current_node.value:
                if self.current_node.left is not None:
                    # 현재 노드의 왼쪽 자식이 존재한다면
                    # 노드를 하나 아래로 이동 시키기
                    self.current_node = self.current_node.left
                else:
                    # 현재 노드의 왼쪽 자식이 존재하지 않는다면
                    self.current_node.left = Node(value)
                    break
            else:  # 삽입하려는 갑싱 현재 노드의 값보다 크다면
                # 삽입하려는 값이 현재 노드의 값보다 크다면 오른쪽 노드로 위치 시키기
                if self.current_node.right is not None:
                    # 현재 노드의 오른쪽 자식이 존재한다면 다음 노드로 이동
                    self.current_node = self.current_node.right
                else:
                    # 존재하지 않는다면 현재 노드의 오른쪽자식으로 위치시키기
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        # node부터 탐색
        self.current_node = self.root
        # current_node를 계속 변경하므로 curreunt_node가 Null이 아니면 계속 탐색
        while self.current_node:
            # value가 존재하므로 True를 반환
            if self.current_node.value == value:
                return True
            # 작다면 현재 노드의 왼쪽쪽 자식노드로 이동
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                # 크다면 현재 노드의 오른쪽 자식 노드로 이동
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        current_node = self.root
        parent = None

        # 삭제할 노드가 존재하는 지 탐색
        while current_node:
            if current_node.value == value:
                break
            parent = current_node
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        if current_node is None:
            # 존재하지 않는다면 False를 반환
            return False

        # current_ndoe :  삭제할 노드
        # parent : 삭제할 노드의 부모 노드
        # 부모노드와의 연결을 끊어줘야하므로 parent라는 변수를 사용
        if current_node.left is None and current_node.right is None:
            # 자식 노드를 가지고 있지 않은 경우
            if parent is None:
                # root노드가 자식을 가지고 있찌 않다-> 트리를 비어버리면됨
                self.root = None
            elif parent.left == current_node:
                parent.left = None
            else:
                parent.right = None
        elif current_node.left and current_node.right is None:
            # 왼쪽 자식 하나만 가지고 있는 경우
            if parent is None:
                self.root = current_node.left
            elif parent.left == current_node:
                parent.left = current_node.left
            else:
                parent.right = current_node.left
        elif current_node.left is None and current_node.right:
            # 오른쪽 자식 하나만 가지고 있는 경우
            if parent is None:
                self.root = current_node.right
            elif parent.left == current_node:
                parent.left = current_node.right
            else:
                parent.right = current_node.right
        else:
            # 양쪽의 자식을 가지고 있는 경우

            # 삭제할 노드의 자리를 대체할 자식 노드를 찾기
            # successor(후계자)라는 변수를 사용
            successor_parent = current_node
            # 후계자는 삭제할 노드보다 큰값중 가장 작은 값을 찾아야함
            # right인 이유는 current_node의 오른족 자식이 큰값이기 때문에
            successor = current_node.right

            # 후계자 찾기
            while successor.left:
                successor_parent = successor
                successor = successor.left

            # 후계자 제거하기
            if successor_parent != current_node:
                # 후계자와 후계자 부모와의 연결 끊기
                successor_parent.left = successor.right
                successor.right = current_node.right
            successor.left = current_node.left

            if parent is None:
                self.root = successor
            elif parent.left == current_node:
                parent.left = successor
            else:
                parent.right = successor


def print_inorder(node):
    """중위 순회로 트리 상태를 출력해서 확인"""
    if node is not None:
        print_inorder(node.left)
        print(node.value, end=' ')
        print_inorder(node.right)


# 1. 루트 노드 생성
root = Node(10)
bst = BST(root)
print_inorder(bst.root)

# 2. 여러 값 insert
for val in [5, 15, 3, 7, 13, 17, 1, 4, 6, 8]:
    bst.insert(val)

print("중위 순회 출력 (insert 후):")
print_inorder(bst.root)  # 정렬된 순서로 출력돼야 함
print("\n")

# 3. search 테스트
print("Search 7:", bst.search(7))  # True
print("Search 20:", bst.search(20))  # False

# 4. delete 테스트
print("\nDelete leaf node (4):")
bst.delete(4)
print_inorder(bst.root)
print("\n")

print("Delete node with one child (15):")
bst.delete(15)
print_inorder(bst.root)
print("\n")

print("Delete node with two children (5):")
bst.delete(5)
print_inorder(bst.root)
print("\n")
