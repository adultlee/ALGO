import sys
sys.setrecursionlimit(10**8)

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

def postorder_traversal(tree):
    
    if not tree:
        return
    
    root = tree[0]
    pre = []
    post = []


    for i in range(1, len(tree)):
        if root > tree[i]:
            pre.append(tree[i])
        else :
            post.append(tree[i])

    

    postorder_traversal(pre)
    postorder_traversal(post)
    print(root)
    

    
    

# 입력 받기

postorder_traversal(tree)