import sys
from memory_node import MemoryNode

def print_memory_state(node):
  """
  Recursion if has childs, print node if it's a leaf
  """

  if node.in_use and node.has_childs():
    print_memory_state(node.left_child)
    print_memory_state(node.right_child)
  else:
    print(node)

def show_memory(root_node):
  """
  Init in-order print of tree leafs
  """

  if not root_node.in_use and not root_node.has_childs():
    print('La memoria se encuentra vacía')
  else:
    print_memory_state(root_node)

def find_free_block(current_node, size):
  """
  Finds a free node if exists giving a root node
  """
  node = None

  if current_node.in_use:
    # check if already has childs
    if current_node.has_childs():
      node = check_childs(current_node, size)
  else:
    # check if node can be splitted
    if current_node.size // 2 >= size:
      split_node(current_node)
      node = check_childs(current_node, size)
    elif size <= current_node.size:
      current_node.in_use = True
      node = current_node

  return node

def check_childs(node, size):
  """
  Check for an available block on the childs of the tree
  """

  # check left child
  res_node = find_free_block(node.left_child, size)

  # if it didn't find space in the left child, check right child
  if not res_node:
    res_node = find_free_block(node.right_child, size)

  return res_node

def split_node(node):
  """
  Splits a node in 2 pieces adding childs
  """
  child_size = node.size // 2
  
  node.left_child = MemoryNode(child_size, node)
  node.right_child = MemoryNode(child_size, node)
  node.in_use = True

  return node

def use_block(options, root_node, ids):
  """
  Parses the input of RESERVAR command an assigns a free block when available
  """
  try:
    x, name, quantity = options
  except:
    print('Por favor, utilice el formato correcto')
    return

  # check if the id is already in use
  if not name in ids:
    node = find_free_block(root_node, int(quantity))
    
    # if result is None, there's no available block
    if not node:
      print(('No existe un espcio contiguo de memoria lo suficientemente grande '
             'para satisfacer la petifición'))
    else:
      # store information about the block/id
      ids[name] = node
      node.id = name
      print(f'Bloque reservado para el identificador {name}')

  else:
    print('Ya existe un bloque asigando para ese identificador')

def remove_node(node, ids):
  # remove basic information
  del ids[node.id]
  node.id = None
  node.in_use = False

  # empty root node
  if not node.parent_node:
    return
  
  parent = node.parent_node
  left = parent.left_child
  right = parent.right_child

  # merge nodes if sibling is empty too
  while not (left.in_use or right.in_use):
    parent.in_use = False
    parent.left_child = None
    parent.right_child = None

    if not parent.parent_node:
      break

    parent = parent.parent_node
    left = parent.left_child
    rgiht = parent.right_child
  
def free_block(root_node, options, ids):
  """
  frees the block used by the identifier provided if it has a block assigned
  """

  try:
    id = options[1]

    # check if identifier exists
    if not id in ids:
      print(f'No hay ningún bloque asignado para el identificador {id}')
      return

    remove_node(ids[id], ids)
    
  except:
    print('Por favor use el formato correcto')

def parse_options(option, root_node, ids):
  """
  Checks if the user has entered a valid option
  It doesn't check the arguments, just the main command.
  """
  if option[0] == 'RESERVAR':
    use_block(option, root_node, ids)
  elif option[0] == 'LIBERAR':
    free_block(root_node, option, ids)
  elif option[0] == 'MOSTRAR':
    show_memory(root_node)
  elif option[0] == 'SALIR':
    sys.exit(1)
  else:
    print('Por favor, seleccione una opción válida.\n')

def init_input(root_node, ids):
  """
  Starts infinite loop asking for commands
  """
  while True:
    print('\nPor favor, indique la operacion que desea con sus parametros:')
    input_u = input()
    parse_options(input_u.split(' '), root_node, ids)
    

def main():
  """
  Starts program execution with initial arguments.
  """

  ids = {}

  try:
  # initializes root node with the size of the memory
    memory = int(sys.argv[1])
    root = MemoryNode(memory, None)
    init_input(root, ids)
  except:
    print('Formato Incorrecto!')
    print('Invoque el programa como "python3 buddy_system.py <memory_size>"')

main()
