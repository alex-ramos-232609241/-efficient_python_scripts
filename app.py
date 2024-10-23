arr = ["text1", "text2", "text3"]
arr_reverse = arr[::-1]

def create_response(data_list):
    value = "value"
    result = {}
    for val in data_list:
        result[f"{val}"] = value
            
    return result

print(create_response(arr_reverse))
