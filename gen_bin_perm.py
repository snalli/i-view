def gen_bin_perm(prefix, answer, n, _1, _0):
	if len(prefix) == n:
		answer.append(''.join(prefix))
		return

	prefix.append("1")
	gen_bin_perm(prefix, answer, n, _1+1, _0)
	prefix.pop()

	if _0 < _1:
		prefix.append("0")
		gen_bin_perm(prefix, answer, n, _1, _0+1)
		prefix.pop()

answer = []
n = 4
gen_bin_perm([], answer, n, 0, 0)
print answer