def solution(input_string):
    # TODO: Implement the function to check whether the provided string is a palindrome or not.
    vowels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    input_string_upper = input_string.upper()
    input_string_filter = filter(lambda x: x in vowels, input_string_upper)
    input_string_list = list(input_string_filter)
    
    def is_palindrome(data_list):
        n = len(data_list)
        print(len(data_list))
        if n <= 1:
            return True
        if data_list[0] != data_list[n-1]:
            print(data_list[0])
            print(data_list[n-1])
            return False
        
        return is_palindrome(data_list[1:n-1])
    
    return is_palindrome(input_string_list)

print(solution("Hello"))
