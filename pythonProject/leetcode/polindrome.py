class Solution():
    @staticmethod
    def isPalindrome(x):
        digit_list = [str(digit) for digit in str(x)]
        reverselist=digit_list[::-1]
        if(digit_list == reverselist):
            print('Its palindrome')
            return True
        else:
            print('Not a palindrome')
            return False


Solution.isPalindrome(10)