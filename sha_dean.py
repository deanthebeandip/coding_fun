from datetime import datetime
import os
import random
import math

compressor_range = 80

def compressor(in_list):
    #rand seed determined by cell 1 value, modded by 8
    rand_seed = (in_list[0] % (len(in_list))) + 1
    #make a randomizer that depends on position
    in_list = [int(in_list[len(in_list)-1-x]*math.sqrt(3)*math.pi*((x+1) *137)) % 26 + 97 for x in range(len(in_list))]
    #make a shifter as well, abc -> cab
    out_list = [in_list[x2] for x2 in range(len(in_list) - rand_seed)]
    for ri in range(rand_seed):
        out_list[ri:ri] = [in_list[len(in_list) - (ri+1)]]
    flip_list = [out_list[len(out_list)-1-f] for f in range(len(out_list))]

    return flip_list

def compressor80(in_list):
    for c in range(compressor_range):
        in_list = compressor(in_list)
    return in_list

def printlist(in_list):
    for p in range(len(in_list)):
        print(in_list[p], end = ' ')
    print('\n')

def arr_to_string(in_list):
    rs = ""
    for arr in range(len(in_list)):
        rs += chr(in_list[arr])
    return rs

def arr_to_normal(in_list):
    in_list = [(in_list[i]%26)+97 for i in range(len(in_list))]
    return in_list

def avg(in_list):
    sum = 0
    for a in range(len(in_list)):
        sum += in_list[a]
    return int(sum/len(in_list))

def avg_tracker(a_list, l_size, i_size):
    for iter in range(i_size):
        fun_list = [random.randint(0, 99) for x in range(l_size)]
        compressor80(fun_list)
        a_list.append(avg(fun_list))
    return a_list

def pull_eight(in_string):
    if len(in_string) > 8:
        return in_string[0:8], in_string[8:]
    else:
        return in_string.ljust(8, '2'), ""


def list_to_conv(w_list):

    hash_list = []

    for word in w_list:
        base_word = word
        compressor80_stack = []
        curr_eight, rest = pull_eight(base_word)
        curr_eight_arr = [ord(c) for c in curr_eight]
        compress80_arr = compressor80(curr_eight_arr)
        compressor80_stack = compress80_arr
        curr_eight = rest

        while len(curr_eight) > 0:
            curr_eight, rest = pull_eight(curr_eight) #new set, so grab first 8
            curr_eight_arr = [ord(c) for c in curr_eight] #make char into int
            compress80_arr = compressor80(curr_eight_arr) #compress 8 char into mumbo
            compressor80_stack = [compressor80_stack[cs] + compress80_arr[cs] for cs in range(8)]
            curr_eight = rest


        hash_word = arr_to_string(arr_to_normal(compressor80_stack))
        hash_list.append(hash_word )
        # print("Base word: %s \t| Hash word: %s" % (base_word, hash_word))
    return hash_list




def file_to_string(in_file):
    big_s = ""
    with open(in_file, 'r') as file:
        big_s += file.read()
    return big_s




def main():
    #Create some arrays
    hashname_list = []

    filename_list = []

    file_strings = []

    sha_file_folder = 'sha_test_files'

    #walk through
    for filename in os.listdir(sha_file_folder):
        if filename.find('.txt')>0:
            filename_list.append(filename)
            file_strings.append(file_to_string(os.path.join(sha_file_folder, filename)))

    hashname_list = list_to_conv(file_strings)
    print(hashname_list)


    #Create a Text File to See the Report better
    f= open(os.path.join(sha_file_folder, "SHA_rep.txt"),"a")
    f.write("Starting a New SHA Report " + str(datetime.now()) + '\n')

    for p in range(len(filename_list)):
        f.write(filename_list[p] + '\t'  + hashname_list[p] + '\n')
    f.close()



    '''

    #Old test to see if SHA-DEAN worked, making a list to see how the others do...
    word_list = ['baaaaaaa', 'aaaabaaa', 'aaaaaaab', 'aaaaaaaaa', 'aaaaaaaab']
    hashname_list = list_to_conv(word_list)


    #dislay the names
    print('Compressor Repeats: %d' % compressor_range)
    for h in range(len(hashname_list)):
        print( ("%s \t %s") % (word_list[h], hashname_list[h]))

    ###even older stuff just to see how "random" my numbers were...
    avg_list = []
    list_size = 2
    iter_size = 2
    avg_list = avg_tracker(avg_list, list_size, iter_size)

    for avg in avg_list:
        print(avg, end = ' ')
    print('\n')

    avg_avg = 0
    for avg_c in range(len(avg_list)):
        avg_avg += avg_list[avg_c]
    avg_avg /= len(avg_list)

    print("List num: %d, Iter num: %d, Avg of Avg: %d" % (list_size, iter_size, avg_avg))
    '''




if __name__ == "__main__":
    main()
