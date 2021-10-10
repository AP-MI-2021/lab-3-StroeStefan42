def get_longest_all_even(lst: list[int]):
    lst2=[]
    lstmax=[]
    nr=0
    nrmax=-1
    for i in lst:
        if i%2==0:
            lst2.append(i)
            nr=nr+1
            if nr > nrmax:
                lstmax=lst2
                nrmax=nr
        if i%2==1:
            nr=0
            lst2=[]
    return lstmax

def test_get_longest_all_even():
    assert get_longest_all_even([36, 11, 12, 28, 26, 19]) == [12, 28, 26]
    assert get_longest_all_even([36, 14, 12, 25, 23, 11]) == [36, 14, 12]
    assert get_longest_all_even([35, 11, 15, 23, 26, 19]) == [26]
    assert get_longest_all_even([36, 10, 12, 28, 26, 19]) == [36, 10, 12, 28, 26]


def cifprim(n):
    while(n!=0):
        if(n%10!=2 and n%10!=3 and n%10!=5 and n%10!=7):
            return False
        n=n//10
    return True

def get_longest_prime_digits(lst: list[int]):
    lst2=[]
    lstmax=[]
    nr=0
    nrmax=-1
    for i in lst:
        if cifprim(i)==True:
            lst2.append(i)
            nr=nr+1
            if nr > nrmax:
                lstmax=lst2
                nrmax=nr
        if cifprim(i)==False:
            nr=0
            lst2=[]
    return lstmax

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([22, 25, 337, 16, 29, 14]) == [22, 25, 337]
    assert get_longest_prime_digits([2, 3, 4, 5]) == [2, 3]
    assert get_longest_prime_digits([11, 22, 33, 55, 66]) == [22, 33, 55]
    assert get_longest_prime_digits([14]) == []


def main():
    while True:
        print('1. Citire date')
        print('2. Determinare cea mai lungă subsecvență cu proprietatea 1')
        print('3. Determinare cea mai lungă subsecvență cu proprietatea 2')
        print('x. Iesire din program')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            lst = []
            n = int(input())
            for i in range(n):
                lst.append(int(input()))
        elif optiune == '2':
            lstf = []
            lstf = get_longest_all_even(lst)
            print(lstf)
        elif optiune == '3':
            lstf = []
            lstf = get_longest_prime_digits(lst)
            print(lstf)
        elif optiune == 'x':
            break
if __name__ == '__main__':
    main()


