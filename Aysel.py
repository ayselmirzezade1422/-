my_lst = ['hello', '2', 'word', ':-)']
new_lst = []

for elem in my_lst:
    if len(elem) <= 3:
        new_lst.append(elem)

print(new_lst)
