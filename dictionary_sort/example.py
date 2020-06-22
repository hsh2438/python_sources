dic = {'b':3, 'a':1, 'c':2}

sorted(dic.items())
# [('a', 1), ('b', 3), ('c', 2)]

sorted(dic.items(), key=lambda x:x[1])
# [('a', 1), ('c', 2), ('b', 3)]

sorted(dic.items(), reverse=True)
# [('c', 2), ('b', 3), ('a', 1)]

sorted(dic.items(), key=lambda x:x[1], reverse=True)
# [('b', 3), ('c', 2), ('a', 1)]
