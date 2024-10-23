def solution(s):
    # TODO: implement find_vowels_positions
    vocals = "aeiouAEIOU"
    
    def get_vocals_index(data_list):
        if len(data_list) == 0:
            return []
        index, value = data_list[0]
        if value in vocals:
            return [index] + get_vocals_index(data_list[1:]) 
        
    
    return get_vocals_index(list(enumerate(s))) 

print(solution("HEY"))
print(solution("hEllOworLd"))
print(solution("xyzxyz"))
print(solution("aeiou"))
print(solution("AEIOUAEIOUaeiouaeiou"))

