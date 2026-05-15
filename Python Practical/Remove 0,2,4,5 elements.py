print("37 Alister Quinny")
my_list=['a','b','c','d','e','f','g']

for index in sorted([0,2,4,5], reverse=True):
    my_list.pop(index)
print(my_list)
