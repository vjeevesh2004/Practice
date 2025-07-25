'''Complete the merge_the_tools function in the editor below.
merge_the_tools has the following parameters:
string s: the string to analyze
int k: the size of substrings to analyze Prints
Print each subsequence on a new line. There will be  of them. No return value is expected.
Sample Input
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output
AB
CA
AD 
'''
def merge_the_tools(string, k):
    n = len(string)

    for i in range(0,n,k):
        substring = string[i:i+k]

        unique_chars = ""
        for char in substring:
            if char not in unique_chars:
                unique_chars += char
        print(unique_chars)

if __name__ == '__main__':
    string, k = input(), int(input())
    print(merge_the_tools(string, k))

        