start_index =int(input())
end_index = int(input())

convert_element = ""

for element in range(start_index,end_index + 1):
    convert_element = chr(element)
    print(convert_element, end=" ")
