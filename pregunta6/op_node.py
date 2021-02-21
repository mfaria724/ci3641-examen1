precedence = {
  '+': 0,
  '-': 0,
  '*': 1,
  '/': 1
}

class OpNode:
  operator = None
  left = None
  right = None

  def result(self):
    return str(eval(str(self.left) + self.operator + str(self.right)))

  def __init__(self, operator, op1, op2):
    self.operator = operator
    self.left = op1
    self.right = op2

  def __str__(self):

    if isinstance(self.left, OpNode):
      if precedence[self.operator] > precedence[self.left.operator]:
        left = f"({str(self.left)})"
      else:
        left = f"{str(self.left)}"
    else:
      left = str(self.left)

    if isinstance(self.right, OpNode):
      if precedence[self.operator] > precedence[self.right.operator]:
        right = f"({str(self.right)})"
      else:
        right = f"{str(self.right)}"
    else:
      right = str(self.right)

    return f"{left} {self.operator} {right}"
