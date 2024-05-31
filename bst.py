class solution(object):
    def insertintobst(self,root,val):
        if rooot==none:
            return treenode(val)
        elif root.val>val:
            root.left=self.insertintobst(root.left,val)
        else:
            root.right=self.insertintobst(root.right,val)
        return root
