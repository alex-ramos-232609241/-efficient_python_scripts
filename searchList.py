def search_list(data_list, element):
    if len(data_list) == 0:
        return False
    
    if data_list[0] == element:
        return True
    
    return search_list(data_list[1:], element)

print(search_list([1, 5, 7, 15], 17 ))    
    