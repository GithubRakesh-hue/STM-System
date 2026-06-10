students={101:"Aarav",102:'Priya',103:'Rohit',104:'Sneha'}

marks={
    101:{
        'test1':78,
        'test2':85,
        'test3':90
    },
    102:{
        'test1':56,
        'test2':35,
        'test3':48
        },
    103:{
        'test1':89,
        'test2':84,
        'test3':96
        },
    104:{
        'test1':86,
        'test2':80,
        'test3':93
        }   
}

while True:
    print("\n" + "="*40)
    print("                MENU")
    print("="*40)
    print("Press 1 : Display all students")
    print("Press 2 : Add marks with test")
    print("Press 3 : Print students test and marks details")
    print("Press 4 : Print the average marks")
    print("Press 5 : Topper of the all test with marks")
    print("Press 6 : Student in batch with average marks topper")
    print("Press 7 : Student in batch with lowest average marks")
    print("Press 8 : Student in batch with average marks > 80")
    print("Press 9 : Report Card")
    print("Press 10: Batch performance")
    print("Press 0 : Exit")
    print("="*40)
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        # 1] display all student
        print('\nDisplaying all students Roll No. with Name...')
        for roll,name in students.items():
            print(f'Roll No. : {roll}  |   Name : {name}')
        print()

    elif choice == '2':
        #2] add marks with test
        print('Adding Marks of new test with test name...')
        test_name=input("Enter the test name : ")
        roll = int(input("Enter the roll no. of the student : "))
        m= int(input(f'Enter the marks of {roll} : '))
        d={}
        d[test_name]=m
        marks[roll]=d
        print(marks,'\n')

    elif choice == '3':
        #3] printing students test and marks details
        print('Students test name and thier roll number...')
        roll=int(input('Enter the student roll : '))
        for i,j in marks[roll].items():
            print(f'Test : {i} | Marks : {j}\n')

    elif choice == '4':
        #4] printing the average marks
        print('Displaying the average marks of all students...')
        roll=int(input('Enter the student roll no. : '))
        print(f'Roll : {roll} | Name : {students[roll]}')
        for st_roll in marks.keys():
            if st_roll == roll:
                sum=0
                count=0
                for j in marks[st_roll].values():
                    sum=sum+j
                    count+=1
                avg=sum/count
                print(f'The average marks are : {avg:.2f}\n')

    elif choice == '5':
        # 5]topper of the all test with marks
        print('Displaying topper by testwise...')
        testname=[]

        for i in marks[101]:
            testname.append(i)

        for test in testname :
            hs = 0
            st_name=''
            for st_id in marks:
                score=marks[st_id].get(test)
                if score > hs :
                    hs=score
                    tp=students[st_id]
            print(f'Test : {test}  |  Student Roll No. : {st_id}  |  Student Name : {tp}  | Score : {hs}\n ')

    elif choice == '6':
        # 6] student in batch with average marks topper
        print('Student in batch  topper with average marks...')
        avg_marks={}
        for roll in students:
            sum=0
            count=0
            for test,m in marks[roll].items():
                sum = sum + m
                count+=1
            avg=sum/count
            avg_marks[roll]=round(avg,2)

        hs=0
        std_id=0
        for roll, avg in avg_marks.items():
            if avg > hs :
                hs = avg
                std_id = roll
        print(f'Student Roll No. : {std_id}  |  Student Name : {students[std_id]}  |  Average Marks : {hs}\n')

    elif choice == '7':
        #7] student in batch with lowest average marks
        print('Student in Batch with lowest average marks...')
        avg_marks={}
        for roll in students:
            sum=0
            count=0
            for test,m in marks[roll].items():
                sum = sum + m
                count+=1
            avg=sum/count
            avg_marks[roll]=round(avg,2)

        ls=avg_marks[101]
        std_id=0
        for roll, avg in avg_marks.items():
            if avg < ls :
                ls = avg
                std_id = roll
        print(f'Student Roll No. : {std_id}  |  Student Name : {students[std_id]}  |  Average Marks : {ls}\n')

    elif choice == '8':
        #8] student in batch with average marks > 80
        print('Student in Batch with average marks greater than 80...')
        avg_marks={}
        for roll in students:
            sum=0
            count=0
            for test,m in marks[roll].items():
                sum = sum + m
                count+=1
            avg=sum/count
            avg_marks[roll]=round(avg,2)

        for roll, avg in avg_marks.items():
            if avg > 80 :
                  print(f'Student Roll No. : {roll}  |  Student Name : {students[roll]}  |  Average Marks : {avg}')
        print()

    elif choice == '9':
        # 9] Report Card
        print('Student Report Card...\n')
        avg_marks={}
        total={}
        grade={}
        for roll in students:
            sum=0
            count=0
            for test,m in marks[roll].items():
                sum = sum + m
                count+=1
            avg=sum/count

            if sum > 80:
                grade[roll]='A'
            elif sum > 70:
                grade[roll]='B'
            else :
                grade[roll]='C'
                
            total[roll]=sum
            avg_marks[roll]=round(avg,2)
            
        for roll in students:
            print('-'*52)
            print(f'| Student Roll No. : {roll}   |  Student Name  : {students[roll]} |')
            print(f'| {marks[roll]}           |')
            print(f'| Total Marks      :  {total[roll]}  |  Average Marks :  {avg_marks[roll]}|')
            print(f'| Grade  : {grade[roll]}                                        |')
            print('-'*52)
        print()

    elif choice == '10':
        # 10] Batch performance
        avg_marks={}
        for roll in students:
            sum=0
            count=0
            for test,m in marks[roll].items():
                sum = sum + m
                count+=1
            avg=sum/count
            avg_marks[roll]=round(avg,2)

        hs=0
        ls=avg_marks[101]
        std_id=0
        std_id2=0
        for roll, avg in avg_marks.items():
            if avg < ls :
                ls = avg
                std_id = roll
            if avg > hs:
                hs= avg
                std_id2=roll
        count=0
        sum=0
        for roll in students:
            count+=1
        for m in avg_marks.values():
                sum=sum+m
        avg=sum/count

        print('Batch performance...')
        print(f'Total number of students : {count}')
        print(f'Average marks of batch : {round(avg,2)}')
        print(f'Topper Student Detail : Student Roll No. : {std_id2}  |  Student Name : {students[std_id2]}  |  Average Marks : {hs}')
        print(f'Lowest Student Detail : Student Roll No. : {std_id}  |  Student Name : {students[std_id]}  |  Average Marks : {ls}\n')
        
    elif choice == '0':
        print("Exiting program...")
        break
        
    else:
        print("Invalid choice! Please select a valid option from the menu.\n")