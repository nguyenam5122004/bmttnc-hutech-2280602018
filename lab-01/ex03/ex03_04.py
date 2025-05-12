def truy_cap_phan_tu(tuple_data):
    fist_element = tuple_data[0]
    last_element = tuple_data[-1]
    return fist_element, last_element

input_tuple = eval(input("Nhập tuple, ví dụ(1,2,3): "))
fist, last = truy_cap_phan_tu(input_tuple)

print("Phần từ đầu tiên:",fist)
print("Phần từ cuối cùng:",last)