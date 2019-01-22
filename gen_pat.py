def gen_pat(_str, cur, prefix, answer, length):
	if len(prefix) == length:
		answer.append(''.join(prefix))
		return

	app = 0
	while cur < length:
		if _str[cur] != "?":
			prefix.append(_str[cur])
			cur += 1
			app += 1
		else:
			cur += 1
			prefix.append("0")
			gen_pat(_str, cur, prefix, answer, length)
			prefix.pop()

			prefix.append("1")
			gen_pat(_str, cur, prefix, answer, length)
			prefix.pop()

	if len(prefix) == length:
		answer.append(''.join(prefix))
	while app:
		prefix.pop()
		app -= 1

answer = []
_str = "1??0?101"
prefix = []
cur = 0
length = len(_str)
gen_pat(_str, cur, prefix, answer, length)
print(answer)
