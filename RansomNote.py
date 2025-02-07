class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for item in ransomNote:
            if item in magazine:
                magazine=magazine.replace(item, ".", 1)
            else:
                return False
        return True
        
