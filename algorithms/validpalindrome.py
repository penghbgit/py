class Solution:
    def palindrome(self, str):
        str = str.lower()
        left = 0
        right = len(str) - 1
        while(left < right):
            leftStr = str[left]
            rightStr = str[right]
            while(not self.__isvalid(leftStr)):
                left += 1
                leftStr = str[left]
                if(left >= right):
                    return True
            while(not self.__isvalid(rightStr)):
                right -= 1
                rightStr = str[right]
                if(right <= left):
                    return True
            if(leftStr != rightStr):
                return False
            left += 1
            right -= 1


    def __isvalid(self, str):
        if(str.isalnum()):
            return True
        return False

if __name__=="__main__":
    str = "A man, a plan, a canal: Panama"
    solution = Solution()
    print solution.palindrome(str)