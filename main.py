student1 = {'name': 'soheil', 'lastname': 'latifi', 'sid': 14010122680417}
student2 = {'name': 'hooman', 'lastname': 'edraki', 'sid': 14010122268108}
student3 = {'name': 'maria','lastname':' delkash', 'sid':1401012268099}
student4 = {'name':'sophia', 'lastname':'delkash',  'sid': 1401012268081}
student5 = {'name':'mehrsa', 'lastname':'joolani',  'sid': 1401012268057}

student6 = {'name':'Nima', 'lastname':'Haddad',  'sid': 1401012268054}

lis = []
# append your varible
lis.append(student1)
lis.append(student2)
lis.append(student3)
lis.append(student4)
lis.append(student5)
lis.append(student6)


people_sorted = sorted(lis, key=lambda x: x['name'])
print(people_sorted)
people_sorted = sorted(lis, key=lambda x: x['lastname'])
print(people_sorted)
people_sorted = sorted(lis, key=lambda x: x['sid'])
print(people_sorted)
