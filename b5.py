def find_word(frequency, inp_str):
    table = str.maketrans("","","!.,:")
    inp_arr = inp_str.lower().translate(table).split()
    out_arr = []
    
    for i in inp_arr:
        if inp_arr.count(i) == frequency:
            out_arr.append(i)
    return(" ".join(list(set(out_arr))))

print(find_word(2,"The cat is chasing the rat. The dog is also chasing the rat."))
