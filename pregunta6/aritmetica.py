import sys
from op_node import OpNode

def pre_order(tokens):
  operations = []
  operands = []

  first_node = None
  previous_node = None

  for token in tokens:
    if token in ['+', '-', '*', '/']:
      operations.append(token)
    else:

      # get operands
      try:
        op_value = int(token)
        operands.append(token)
      except:
        print(f"El token {token} es invalido")
        sys.exit()

      if len(operands) == 2:
        operator = operations.pop()
        op2 = operands.pop()
        op1 = operands.pop()

        if not previous_node:
          node = OpNode(operator, op1, op2)
        else:
          node = OpNode(operator, previous_node, op2)

        previous_node = node

        if not first_node:
          first_node = node

        result = eval(op1 + operator + op2)
        operands.append(str(result))
  
  return previous_node

def post_order(tokens):
  operands = []

  for token in tokens:
    if token in ['+', '-', '*', '/']:
      # evaluate when enough operands
      if len(operands) >= 2:
        op2_raw = operands.pop()
        op1_raw = operands.pop()
  
        result_node = OpNode(token, op1_raw, op2_raw)
        result = result_node.result()

        operands.append(result_node)
    else:

      # get operands
      try:
        op_value = int(token)
        operands.append(token)
      except:
        print(f"El token {token} es invalido")
        sys.exit()

  return operands[0]

def eval_expr(args):

  order = args[1]
  if not order in ['PRE', 'POST']:
    print('Por favor, indique un orden de evaluación válido. (PRE, POST)')
    return

  expression = ' '.join(args[2:])
  if not expression:
    print('Por favor, provea una expresión para que sea evaluada.')
    return

  tokens = expression.split(' ')

  if order == 'POST':
    node = post_order(tokens)
    print(node.result())
  else:
    node = pre_order(tokens)
    print(node.result())

  return node

def show_infix(option):

  node = eval_expr(option)

  if node:
    print(node)
  

def parse_options(option):
  """
  Checks if the user has entered a valid option
  It doesn't check the arguments, just the main command.
  """
  if option[0] == 'EVAL':
    eval_expr(option)
  elif option[0] == 'MOSTRAR':
    show_infix(option)
  elif option[0] == 'SALIR':
    sys.exit(1)
  else:
    print('Por favor, seleccione una opción válida.\n')

def main():
  while True:
    print('\nPor favor, indique la accion que desea:')
    print('EVAL <orden> <expr>')
    print('MOSTRAR <orden> <expr>')
    print('SALIR\n')
    input_u = input()
    parse_options(input_u.split(' '))

main()
