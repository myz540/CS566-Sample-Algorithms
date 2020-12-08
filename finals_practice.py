pal_string = "abccba"
pal_string2 = "abcdcba"
non_pal_string = "abcdba"
non_pal_string2 = "abcddba"


def iter_pal(string):
    my_list = []
    n = len(string)
    m = int(n/2)
    for i in range(0, m):
        print i, string[i]
        my_list.append(string[i])
    if n % 2 == 1:
        m += 1

    print "m: ", m
    for i in range(m, n):

        if my_list.pop() != string[i]:
            print my_list.pop(), string[i]
            return False

    return True


def rec_pal(string, i, j):
    print i, j
    if string[i] != string[j]:
        print string[i], string[j]
        return False
    if i >= j:
        print i, j
        return True
    else:
        return rec_pal(string, i+1, j-1)


def rec_print(n):
    if n is 0:
        return
    rec_print(n-1)
    print n

#print iter_pal(non_pal_string)
#print rec_pal(pal_string2, 0, 6)

rec_print(100)