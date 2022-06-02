class BST:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def array2BST(array):
        '''
        array:sorted array
        '''
        n = len(array)
        if n == 0: return None
        m = n//2
        left,root,right = array[:m],array[m],array[m+1:]
        return BST(root,BST.array2BST(left),BST.array2BST(right))
    
    @staticmethod
    def BST2array(node):
        '''
        node:BST node
        '''
        if not node: return []
        return BST.BST2array(node.left)+[node.val]+BST.BST2array(node.right)