class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index2=len(numbers)-1
        index1=0
        while(numbers[index1]+numbers[index2]!=target):
            if(numbers[index1]+numbers[index2]<target):
                
                    index1+=1
               
            elif(numbers[index1]+numbers[index2]>target):
                index2-=1
        return[index1+1,index2+1]
