student1 = {'name': 'soheil', 'lastname': 'latifi', 'sid': 14010122680417}
student2 = {'name': 'hooman', 'lastname': 'edraki', 'sid': 14010122268108}

lis = []
# append your varible
lis.append(student1)
lis.append(student2)



people_sorted = sorted(lis, key=lambda x: x['name'])
print(people_sorted)
people_sorted = sorted(lis, key=lambda x: x['lastname'])
print(people_sorted)
people_sorted = sorted(lis, key=lambda x: x['sid'])
print(people_sorted)
