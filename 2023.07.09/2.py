def tree_leaves(tree: list) -> int:

    """Считает количество всех элементов списка, в который входят другие списки"""
    
    result = 0
    
    for elem in tree:
        if type(elem) == type([]):
            result += tree_leaves(elem)
        else:
            result += 1
    
    return result
    
    
# >>> tree = []
# >>> print(tree_leaves(tree))
# 0  
# >>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf']]
# >>> tree_leaves(tree)
# 33
# >>>
# >>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
# >>> tree_leaves(tree)
# 38
# >>> tree = [[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf']
# >>> tree_leaves(tree)
# 9