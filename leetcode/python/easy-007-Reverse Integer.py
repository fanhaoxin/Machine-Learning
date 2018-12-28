'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # y=[]
        # x = list(str(x))
        # if x[0]=='-':
        #     y=x[::-1]
        #     y.insert(0, '-')
        #     y.pop()
        # elif x[-1]=='0':
        #     y=x[::-1]
        #     y.pop(0)
        # else:
        #     y=x[::-1]
        # z=int(y)
        # return z
        
        if x>0:
            a=list(reversed(list(str(x))))
            if a[0]=='0':
                b=int(''.join(a[1:]))
                if b<pow(-2,31) or b>pow(2,31)-1:
                    return 0
                else:
                    return b
            else:
                b=int(''.join(a))
                if b<pow(-2,31) or b>pow(2,31)-1:
                    return 0
                else:
                    return b
        elif x<0:
            a = list(reversed(list(str(x)[1:])))
            if a[0]=='0':
                b=int(''.join(['-']+a[1:]))
                if b<pow(-2,31) or b>pow(2,31)-1:
                    return 0
                else:
                    return b
            else:
                b=int(''.join(['-']+a))
                if b < pow(-2, 31) or b > pow(2, 31) - 1:
                    return 0
                else:
                    return b
        else:
            return 0