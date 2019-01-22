def all_subseq(prefix, suffix, seen):

	s = ''.join(prefix)
	if s in seen:
		return

	seen.add(s)
	for i,s in enumerate(suffix):
		all_subseq(prefix + [s], suffix[i+1:], seen)

answer = set()
s = "abc"
all_subseq([], list(s), answer) 
for a in answer: 
	print a

answer = set()
s = "aab"
all_subseq([], list(s), answer) 
for a in answer: 
	print a