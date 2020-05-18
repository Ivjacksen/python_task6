from task5 import prime_num, spis_del, divider
from task4 import F, rare_letter

def test_prime_num():
    assert prime_num(3) == True

def test_spis_del():
    assert spis_del(969) == [3, 17 ,19]

def test_divider():
    assert divider(969) == 19

def test_rare_letter():
    Names = ['Nataly', 'Andrey', 'Anna', 'Andrey']
    assert(rare_letter(F(Names, N=100)) == 'N')

def test__F():
    list_names = ('Nina', 'Anna', 'Ivan', 'Vlad', 'Elena', 'Andrey', 'Nataly')
    N = 100
    test_list = F(list_names, N)
    assert len(test_list) == N