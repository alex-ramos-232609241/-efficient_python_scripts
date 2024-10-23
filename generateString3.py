def solution(string1, string2):
    # TODO: Implement the function here
    n = len(string1)
    m = len(string2)
    string2_enum = list(enumerate(string2))
    string3 = ''
    i = 0
    while i < n:

        for index, value in string2_enum:
            if string1[i] == value:
                print(value)
                string3 += value
                string2_enum.pop(index)
                break
        i += 1
    return string3

print(solution('aabbccdd', 'bcda'))