# task 4
universities = [

     ['California Institute of Technology', 2175, 37704],

     ['Harvard', 19627, 39849],

     ['Massachusetts Institute of Technology', 10566, 40732],

     ['Princeton', 7802, 37000],

     ['Rice', 5879, 35551],

     ['Stanford', 19535, 40569],

     ['Yale', 11701, 40500]

]


def enrollment_stats(universities):
    try:
        students_list=list()
        tution_list=list()
        for university_name, student_num, annual_tution in universities:
            students_list.append(student_num)
            tution_list.append(annual_tution)
        return students_list,tution_list
    except:
        print("An error occured")

def mean(list1):
    try:
        sumL=sum(list1)
        numEl=len(list1)
        return (f"{(sumL/numEl):.2f}")
    except:
        print("An error occured")

def median(list1):
    try:
        list2=list1
        list2.sort()
        i=int(len(list2)/2)
        
        # print(i)
        return list2[i]
    except:
        print("An error occured!")
try:
    students_list,tution_list=enrollment_stats(universities)
    print("******************************")
    print()
    print(f"Total students: {sum(students_list)}")
    print()
    print(f"Total tuition: $ {sum(tution_list)}")
    print()
    print()
    print()
    print(f"Student mean: {mean(students_list)}")
    print()
    print(f"Student median: {median(students_list)}")
    print()
    print()
    print()
    print(f"Tuition mean: $ {mean(students_list)}")
    print()
    print(f"Tuition median: $ {median(students_list)}")
    print()
    print("******************************")
except:
    print("An error occured")