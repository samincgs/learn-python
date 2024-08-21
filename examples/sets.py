s1 = {1,2,3}
s2 = {2,3,4}
s3 = [3,4,5]

# s4 = s1.intersection(s2, s3)

# s5 = s1.difference(s2, s3)

s6 = s1.union(s3)

# print(s6)

# practical example
l1 = [1,2,3,1,2,3]
l2 = list(set(l1))

# print(l2)



employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

# known as a membership test
if 'Samin' in developers:
    print('Found')
    
# O(n) for a list
    
# SETS are very performant when it comes to membership tests

# people who are gym_members and are employees
emp_gym = list(set(gym_members).intersection(developers))
# emp_gym = list(set(employees).intersection(set(gym_members), set(developers)))

# employees that are not gym members or developers
result = set(employees).difference(gym_members, developers)

print(result)





