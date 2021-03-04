def height(root):
    if root:
        return 1+ max(height(root.left), height(root.right))
    else:
        return -1
