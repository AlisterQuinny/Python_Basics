print("37 Alister Quinny") 
My_dict = {'apple': 10, 'banana': 2, 'cherry': 15, 'date': 5}
Sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
Sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Ascending order:", sorted_asc) 
print("Descending order:", sorted_desc)
