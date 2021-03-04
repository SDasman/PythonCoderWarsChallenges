def pathmaker(root,val,samp_list):
    if root:
        if val > root.info:
            samp_list.append(root)
            return pathmaker(root.right, val, samp_list)
        elif val < root.info:
            samp_list.append(root)
            return pathmaker(root.left, val, samp_list)
        elif val == root.info:
            samp_list.append(root)
            return samp_list
    else:
        return samp_list

def lca(root, v1, v2):
    v1_path = []
    v2_path = []
    v1_path = pathmaker(root, v1, v1_path)
    v2_path = pathmaker(root, v2, v2_path)
    low = 25
    for num1 in v1_path:
        for num2 in v2_path:
            if num1 == num2:
                if num1.info< low:
                    low = num1
    return low

  
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
