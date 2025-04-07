class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        for x in range(len(triangle)-2,-1,-1):
            for i in range(0, x+1):
    
                triangle[x][i]+=min(triangle[x+1][i],triangle[x+1][i+1])
        return triangle[0][0]

            
        
    
        



        
