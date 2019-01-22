def no_consec_1(prefix, answer, length):
	if len(prefix) == length:
		answer.append(''.join(prefix))
		return

	prefix.append("0")
	no_consec_1(prefix, answer, length)
	prefix.pop()

	if not prefix or prefix[-1] != "1":
		prefix.append("1")
		no_consec_1(prefix, answer, length)
		prefix.pop()

answer = []
n = 4
no_consec_1([], answer, n)
print answer