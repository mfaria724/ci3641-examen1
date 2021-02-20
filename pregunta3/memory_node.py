class MemoryNode:
  size = 0
  in_use = False
  parent_node = None
  left_child = None
  right_child = None
  id = None

  def has_childs(self):
    return self.left_child and self.right_child

  def __init__(self, size, parent):
    self.size = size
    self.parent_node = parent

  def __str__(self):
    # result = "{:<8} {:<15} {:<10} {:<10}".format(k, lang, perc, change)
    result = "{:<20} {:<10}\n".format("Tamaño:", self.size) + \
             "{:<20} {:<10}\n".format("Asignado a:", str(self.id))
    
    return result

