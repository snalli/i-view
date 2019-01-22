def substr_rm(_str, pat):
	stack = []
	j = -1
	pat_len = len(pat)
	maxlen = 0
	for i in range(len(_str)):
		if _str[i] != pat[j+1]:
			# reset
			j = -1

		if _str[i] == pat[j+1]:
			# match and push the curr pos in _str and pos that match
			stack.append((i, j+1))
			j += 1
		else:
			# push the last un-match ?
			stack.append((i, j))

		if j+1 == pat_len:
			for _ in range(pat_len):
				stack.pop()
			tmp_i, j = -1, -1
			if stack:
				tmp_i,j = stack[-1]
			maxlen = max(maxlen, i-tmp_i)

	return maxlen

_str="1011100000100"
pat="100" # ans = 6
print(substr_rm(_str, pat))
