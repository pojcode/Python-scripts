'''
Difference in terms of execution time between
not optimized search algorithm vs optimized search algorithm
'''
import os, random, string, time

def optimized_search(search_in:list, to_find, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(search_in) - 1
    if low > high:
        return 'ERROR, value not found'
    reference = (low + high) // 2
    if to_find == search_in[reference]:
        return f'Bingoooooo {to_find} is in index {reference} of the list'
    elif to_find < search_in[reference]:
        return optimized_search(search_in, to_find, low, reference - 1)
    else:
        return optimized_search(search_in, to_find, reference + 1, high)

def not_optimized_search(search_in:list, to_find):
    for i in range(len(search_in)):
        if search_in[i] == to_find:
            return f'Bingoooooo {to_find} is in ' \
                f'index {search_in.index(to_find)} of the list'
    return 'ERROR, value not found'

os.system('cls')

def create_elements_list():
    data_size = 5 * 10**6    # the greater, the longer in terms of time
    random_list = set()
    to_find = input('>> Element to find: ').lower().strip()
    print('\n-----| Creating Datasheet... |-----\n')
    letters = list(string.ascii_lowercase)
    always_present = True
    while len(random_list) < data_size:
        if to_find.isdigit():
            if always_present:
                random_list.add(12345678)
                always_present = False
            # list will be filled with random numbers in the range 
            # -3*data_size, 3*data_size
            random_list.add(random.randint(0, 3*data_size))
        else:
            if always_present:
                random_list.add('present')
                always_present = False
            # words and their lenght are created randomly using this range
            # 2, len(to_find) + 2 for lenght and all the letters lowercases
            n = 1
            total_words = 0
            while total_words < data_size:
                total_words = len(letters)**n
                n += 1
            word_size = random.randint(1, len(to_find) + n)
            word = ''
            while len(word) < word_size:
                word += random.choice(letters)
            random_list.add(word)
    random_list = sorted(list(random_list))
    if to_find.isdigit():
        to_find = int(to_find)
    
    return random_list, to_find

print('This script will show the difference, in terms of execution time,'
    '\nbetween not optimized search algorithm vs optimized search algorithm,'
    '\nsearching in a given size list a given value.'
    '\nGreater datasheet size will show more difference but will take longer.'
    '\nNumber 12345678 or word "present" will be always in the datasheet\n')

random_list, to_find = create_elements_list()
print(f'DATASHEET SIZE: {len(random_list)}\n')
start_time = time.time()
print(optimized_search(random_list, to_find))
end_time = time.time()
print(f'OPTIMIZED ALGORITHM execution time -> {end_time-start_time} secs\n')
start_time = time.time()
print(not_optimized_search(random_list, to_find))
end_time = time.time()
print(f'NOT OPTIMIZED ALGORITHM execution time -> {end_time-start_time} secs')
input()