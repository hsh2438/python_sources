import re

# . 한 개의 임의의 문자
r = re.compile("a.c")
print(r.search("abd"))
print(r.search("abc"))

# ? 앞의 문자가 존재 or 미존재
r = re.compile("abc?")
print(r.search("abc"))
print(r.search("ab"))

# * 앞의 문자가 0개 이상
r = re.compile("ab*c")
print(r.search("ac"))
print(r.search("abc"))
print(r.search("abbbc"))

# + 앞의 문자가 1개 이상
r = re.compile("ab+c")
print(r.search("ac"))
print(r.search("abc"))
print(r.search("abbbc"))

# ^ 시작되는 글자를 지정
r = re.compile("^bc")
print(r.search("abc"))
print(r.search("bc"))

# {숫자} 해당 문자를 숫자만큼 반복
r = re.compile("ab{2}c")
print(r.search("abc"))
print(r.search("abbc"))
print(r.search("abbbc"))

# {숫자1, 숫자2} 해당 문자를 숫자1 이상, 숫자2 이하만큼 반복
r = re.compile("ab{2,4}c")
print(r.search("abc"))
print(r.search("abbc"))
print(r.search("abbbc"))
print(r.search("abbbbc"))
print(r.search("abbbbbc"))

# {숫자,} 해당 문자를 숫자 이상 만큼 반복
r = re.compile("ab{2,}c")
print(r.search("abc"))
print(r.search("abbc"))
print(r.search("abbbc"))
print(r.search("abbbbc"))
print(r.search("abbbbbc"))

# [문자] 문자들 중 한개의 문자와 매치, [a-zA-Z]는 알파벳 전부를 의미, [0-9]는 숫자 전부를 의미
r = re.compile("[abc]")
print(r.search("a"))
print(r.search("d"))

# [^문자] 제외한 모든 문자를 매치
r = re.compile("[^abc]")
print(r.search("a"))
print(r.search("d"))
