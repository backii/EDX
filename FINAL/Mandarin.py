import math

#Mandarin numbers

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):

    if int(us_num) < 10:
        return trans[us_num]
    elif int(us_num) == 10:
        return trans['10']
    else:
        return trans[str(math.floor(int(us_num)/10))] + " " + trans['10'] + " " + trans[str((int(us_num) % 10))]


print(convert_to_mandarin('23'))


######


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    if len(L) < 3:
        return sum(L)
    else:
        tmp_dec = []
        tmp_inc = []
        set_of_inc = []
        set_of_dec = []
        num = 0

        while True:

            num += 1

            if L[num] >= L[num-1]:
                tmp_inc.append(L[num-1])

                tmp_dec.append(L[num - 1])
                set_of_dec.append(tmp_dec)
                tmp_dec = []

            if L[num] < L[num-1]:

                tmp_inc.append(L[num-1])
                set_of_inc.append(tmp_inc)
                tmp_inc = []

                tmp_dec.append((L[num-1]))

            if num == len(L) - 1:
                if L[num] >= L[num-1]:
                    tmp_inc.append(L[num])
                    set_of_inc.append(tmp_inc)

                elif L[num] < L[num-1]:
                    tmp_dec.append(L[num])
                    set_of_dec.append(tmp_inc)
                break

        max_len_inc = 0
        max_len_dec = 0

        for lists in set_of_inc:

            if max_len_inc < len(lists):
                max_len_inc = len(lists)
                list_inc = lists

        for lists in set_of_dec:

            if max_len_dec < len(lists):
                max_len_dec = len(lists)
                list_dec = lists


        if max_len_inc == max_len_dec:
            return sum(list_dec) if set_of_inc.index(list_inc) > set_of_dec.index(list_dec) else sum(list_inc)

        else:
            return sum(list_dec) if max_len_inc < max_len_dec else sum(list_inc)






print(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))