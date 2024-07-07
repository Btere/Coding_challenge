Question:
"""Write a function solution that, given two integers A and B, returns a string containing exactly A letters 'a' and exactly B letters 'b' with no three consecutive letters being the same (in other words, neither "aaa" nor "bbb" may occur in the returned string).

Examples:

1. Given A = 5 and B = 3, your function may return "aabaabab". Note that "abaabbaa" would also be a correct answer. Your function may return any correct answer.

2. Given A = 3 and B = 3, your function should return "ababab", "aababb", "abaabb" or any of several other strings.

3. Given A = 1 and B = 4, your function should return "bbabb", which is the only correct answer in this case.

Assume that:

A and B are integers within the range [0..100];
at least one solution exists for the given A and B.
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""

def solution(A, B):
    result = []
    while A > 0 or B > 0:
        if len(result) >= 2 and result[-1] == result[-2]:
            if result[-1] == 'a':
                result.append('b')
                B -= 1
            else:
                result.append('a')
                A -= 1
        else:
            if A > B:
                result.append('a')
                A -= 1
            else:
                result.append('b')
                B -= 1
                
    return ''.join(result)
