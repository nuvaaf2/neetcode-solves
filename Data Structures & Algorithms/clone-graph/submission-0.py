class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
       
        if not node:
            return None
            
    
        oldToNew = {}

        def dfs(curr_node):
          
            if curr_node in oldToNew:
                return oldToNew[curr_node]

       
            clone = Node(curr_node.val)
            
            oldToNew[curr_node] = clone

            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

      
            return clone

        
        return dfs(node)