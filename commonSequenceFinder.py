def solution(string1, string2):
    # TODO: Implement the function here
    string3 = ''
    len_string_1 = len(string1)
    count = 0
    while len_string_1 > count:
        index = 0
        while len(string2) > index:
            if string1[count] == string2[index]:
                string3 += string2[index]
                string2 = string2[:index] + string2[index + 1:]
                break
            index += 1
        count += 1
    return string3