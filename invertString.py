def solution(input_string):
    # TODO: implement the function
    vowels = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vowels_with_index = list(enumerate(vowels))
    def get_vocal_transform(data_list):
        if len(data_list) == 0:
            return ""
        
        seed = data_list[0]
        result = ""
        if seed in vowels:
            def filter_for_vocal(v):
                idx, val = v
                return val == seed
         
            filter_result = filter(filter_for_vocal, vowels_with_index)
        
            index, value = list(filter_result)[0]

            if index <= 25:
                new_index = index + 26
            else:
                new_index = index - 26
            result = result + vowels[new_index]
        else:
            result = result + seed
        return result + get_vocal_transform(data_list[1:])
    
    return get_vocal_transform(input_string)

print(solution("alexenriqueRAMOSIPANAQUE25$"))