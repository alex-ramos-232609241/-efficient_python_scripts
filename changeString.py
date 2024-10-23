def solution(s):
    # TODO: Implement the solution here
    alphabetic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def get_string(data_list):
        result = ""
        if len(data_list) == 0:
            return ""
            
        value = data_list[0]
        
        if value in alphabetic:
            print(value)#z
            alphabetic_list_enum = list(enumerate(alphabetic))
            val_index = None
            for index, le in alphabetic_list_enum:
                
                if le == value:
                    val_index = index
            if val_index == 25:
                result = result + alphabetic[0]
            elif val_index == 51:
                result = result + alphabetic[26]
            else:
                result = result + alphabetic[val_index + 1]
        
        else:
            result = result + value

        

        return result + get_string(data_list[1:])

    return get_string(s)
print(solution("abc123XYz!"))