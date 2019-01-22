'''
https://www.geeksforgeeks.org/longest-substring-of-0s-in-a-string-formed-by-k-concatenations/
Given a binary string of length n and an integer k. 
Consider another string T which is formed by concatenating given binary string k times. 
The task is to print the maximum size of a substring of T containing only zeroes.
'''
def max_substr_0_kcat(s,k):

	slen = len(s)
	if all([__s == '0' for __s in s]):
		return slen * k

	_0_prefix_len = 0
	for __s in s:
		if __s == '0':
			_0_prefix_len += 1
			continue
		break

	_0_suffix_len = 0
	for __s in s[::-1]:
		if __s == '0':
			_0_suffix_len += 1
			continue
		break

	_0_substr_len = 0
	answer = 0
	for __s in s:
		if __s == '0':
			_0_substr_len += 1
		else:
			answer = max(answer, _0_substr_len)
			_0_substr_len = 0
	answer = max(answer, _0_substr_len)		# for str ending in 0

	return max(answer, _0_prefix_len + _0_suffix_len)

s = "00100110"
k = 5
print max_substr_0_kcat(s, k)