def lca(root, v1, v2):       
    node = root
    while node:
        if max(v1, v2) < node.info:
            node = node.left
        elif min(v1, v2) > node.info:
            node = node.right
        else:
            break
    return node 
