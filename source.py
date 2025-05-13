def max_heapify(comparable_list, size=None, i_root=0):
  if size is None:
    size = len(comparable_list)

  i_largest = i_root
  left = (2*i_root)+1
  right = (2*i_root)+2

  if left < size and comparable_list[left] > comparable_list[i_largest]:
    i_largest = left

  if right < size and comparable_list[right] > comparable_list[i_largest]:
    i_largest = right

  if i_largest != i_root:
    comparable_list[i_root], comparable_list[i_largest] = comparable_list[i_largest], comparable_list[i_root]
    max_heapify(comparable_list, size, i_largest)

def heap_sort(comparable_list, inplace=False):
  output_list = comparable_list if inplace else comparable_list.copy()
  size = len(comparable_list)
  for i in range((size-1)//2, -1, -1):
    max_heapify(output_list, size, i)

  for i in range(size-1, 0, -1):
    output_list[0], output_list[i] = output_list[i], output_list[0]
    max_heapify(output_list, i, 0)
  return output_list

class max_heap:
  data = []

  def __init__(self, comparable_list):
    size = len(comparable_list)
    self.data = comparable_list.copy()
    for i in range((size-1)//2, -1, -1):
      max_heapify(self.data, size, i)

  def __getitem__(self, index):
    return self.data[index]
  
  def __repr__(self):
    return str(self.data)

  def parent(self, i):
    return self[(i-1)//2]
  
  def left(self, i):
    return self[(2*i)+1]
  
  def right(self, i):
    return self[(2*i)+2]
  
class priority_queue:
  data = []

  def __getitem__(self, index):
    return self.data[index]

  def __repr__(self):
    return str(self.data)

  def insert(self, x, priority):
    h = self.data
    h.append({'value': x, 'priority': priority})
    i = len(h) - 1
    while(i > 0):
      i_parent = (i-1)//2
      if (h[i_parent]['priority'] < h[i]['priority']):
        h[i_parent], h[i] = h[i], h[i_parent]
        i = i_parent
      else:
        break

  def extract_max(self):
    h = self.data
    size = len(h)
    if not size:
      return None
    
    output = h.pop(0)
    i = 0
    size-=1
    while True:
      left = (2*i)+1
      right = (2*i)+2
      largest = i

      if left < size and h[left]['priority'] > h[i]['priority']:
        largest = left

      if right < size and h[right]['priority'] > h[i]['priority']:
        largest = right

      if largest != i:
        h[i], h[largest] = h[largest], h[i]
        i = largest
      else:
        break

    return output
  
h = max_heap([15, 1, 2, 64, 9, 42, 5, 7, 77, 435, 342, 24, 55])

print(heap_sort([15, 1, 2, 64, 9, 42, 5, 7, 77, 435, 342, 24, 55]))

pq = priority_queue()

for x in range(len(h.data)):
  pq.insert(x, h[x])

print(pq)
pq.extract_max()
print(pq)
pq.extract_max()
print(pq)
pq.extract_max()
print(pq)
pq.extract_max()
print(pq)

class Node:
  value = None
  left = None
  right = None
  
  def __init__(self, comparable):
    self.value = comparable

  def insert(self, comparable):
    if comparable < self.value:
      if not self.left:
        self.left = Node(comparable)
        return self.left
      return self.left.insert(comparable)
    
    if comparable > self.value:
      if not self.right:
        self.right = Node(comparable)
        return self.left
      return self.right.insert(comparable)
      
  def search(self, target):
    if target == self.value:
      return self
    
    if target < self.value:
      return self.left.search(target)
    
    return self.right.search(target)
  
  def remove(self, target):
    if target < self.value:
      self.left = self.left.remove(target)
    elif target > self.value:
      self.right = self.right.remove(target)
    else:
      if self.left and self.right:
        sucessor = self.right
        while sucessor.left:
          sucessor = sucessor.left
        self.value = sucessor.value
        self.right = self.right.remove(sucessor.value)
      elif self.left:
        return self.left
      elif self.right:
        return self.right
      else:
        return None

    return self
  
  def pre(self):
    print(self.value)
    self.left.pre() if self.left else print(None)
    self.right.pre() if self.right else print(None)

  def post(self):
    self.left.post() if self.left else print(None)
    print(self.value)
    self.right.post() if self.right else print(None)

  def level(self):
    q = []
    q.append((self, 0))
    while(len(q)):
      (p, level) = q.pop(0)
      if (p):
        print(f'Level {level}: {p.value}')
        q.append((p.left, level+1))
        q.append((p.right, level+1))
      else:
        print(f'Level {level}: {None}')

class BST:
  root = None

  def insert(self, comparable):
    if not self.root:
      self.root = Node(comparable)
      return self.root
    else:
      return self.root.insert(comparable)
    
  def search(self, target):
    return self.root.search(target)
  
  def remove(self, target):
    if not self.root:
      return None
    self.root = self.root.remove(target)
    return self
  
  def pre(self):
    print(None) if not self.root else self.root.pre()
  
  def post(self):
    print(None) if not self.root else self.root.post()

  def level(self):
    print(None) if not self.root else self.root.level()

  def balance(self):
    if not self.root:
      return self
    
    def inorder(node, out):
      if not node:
        return
      inorder(node.left, out)
      out.append(node.value)
      inorder(node.right, out)

    sorted_vals = []
    inorder(self.root, sorted_vals)

    def build_balanced(arr, left, right):
      if left > right:
        return None
      mid = (left + right) // 2
      node = Node(arr[mid])
      node.left = build_balanced(arr, left, mid-1)
      node.right = build_balanced(arr, mid+1, right)
      return node
  
    self.root = build_balanced(sorted_vals, 0, len(sorted_vals)-1)
    return self

bst = BST()
for x in h.data:
  bst.insert(x)

bst.level()
bst.remove(15)
bst.level()

bst.remove(435)
bst.level()

bst.remove(342)
bst.level()

bst.remove(55)
bst.level()

bst.remove(1)
bst.level()

bst.post()
bst.level()
bst.balance()
bst.level()