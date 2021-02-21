from op_node import OpNode

precedence = {
  '+': 0,
  '-': 0,
  '*': 1,
  '/': 1
}

child = OpNode('+', '1', '2')
father = OpNode('*', '1', child)

print(child)
print(father)
print(type(father.left))
print(type(father.right))
