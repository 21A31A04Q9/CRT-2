class Solution(object):
    def preorderhelper(self,root,result):
        if root == None:
            return
        result.append(root.val)
        self.preorderhelper(root.left,result)
        self.preorderhelper(root.right)
    def preordertraversal(self,root):
        result = []
        self.preorderhelper(root,result)
        return result
    
