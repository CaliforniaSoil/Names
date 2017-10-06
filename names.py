def names():

    students = [
         {'first_name' : 'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}]
    print "Students"
    count = 0
    for i in students:
        count += 1
        print count, '-', i['first_name'], ' ', i['last_name'], '-', len(i['first_name']) + len(i['last_name'])
    
    instructors = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}]
    print "Instructors"
    count = 0
    for i in instructors:
        count += 1
        print count, '-', i['first_name'], ' ', i['last_name'], '-',len(i['first_name']) + len(i['last_name'])
names()
