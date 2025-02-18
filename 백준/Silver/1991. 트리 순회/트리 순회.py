class Node:
  def __init__(self, data, left, right):
      self.data = data
      self.left = left
      self.right = right

def preorder(node):
  if node == '.':
      return
  print(node, end='')
  preorder(tree[node].left)
  preorder(tree[node].right)

def inorder(node):
  if node == '.':
      return
  inorder(tree[node].left)
  print(node, end='')
  inorder(tree[node].right)

def postorder(node):
  if node == '.':
      return
  postorder(tree[node].left)
  postorder(tree[node].right)
  print(node, end='')

N = int(input())
tree = {}

for _ in range(N):
  data, left, right = input().split()
  tree[data] = Node(data, left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')
