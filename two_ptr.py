import string
def replace_punctuation(S, P):
	i, j = 0, 0
	s = list(S)
	p = set(P)
	slen = len(s)
	while True:
		while i < slen and s[i] not in p:
			i += 1

		if not j: j = i

		while j < slen and s[j] in p:
			j += 1

		if j >= slen:
			break

		s[i], s[j] = s[j], s[i]

	return ''.join(s[:i])

S = "@#%^&STHJYYHR!@$Y^GJH&O*H<{~^#*^<>FG?/}:&(HKL{<FJ})"
# !"#$%&'()*+,-./:;?@[\]^_`{|}~ 
P = string.punctuation
print replace_punctuation(S, P)