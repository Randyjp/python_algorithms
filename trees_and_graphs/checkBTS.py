# 4.5) Check if tree is a search binary tree

def checkBST(root):
    nums = []
    traverse(root, nums)
    return nums == list(sorted(set(nums)))


def traverse(node, num_list=[]):
    if node is None:
        return
    traverse(node.left, num_list)
    num_list.append(node.data)
    traverse(node.right, num_list)
    return num_list


