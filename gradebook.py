




eren = {
 "name": "Eren",
 "homework": [90.0,97.0,75.0,92.0],
 "quizzes": [88.0,40.0,94.0],
 "tests": [75.0,90.0]
}

mikasa = {
"name": "Mikasa",
"homework": [100.0, 92.0, 98.0, 100.0],
"quizzes": [82.0, 83.0, 91.0],
"tests": [89.0, 97.0]
}

armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

students=[armin,mikasa, eren]
for students in students:
    print("Name:", students["name"], '\n', "Homework:", students["homework"], '\n', "Quizzes:", students["quizzes"], '\n', "Tests:", students["tests"])

def average(numbers):
    total=sum(numbers)
    total=float(sum(numbers))
    av=total/len(numbers)
    return(av)

def get_average(students):
    homework=average(students["homework"])
    quiz= average(students["quizzes"])
    test=average(students["quizzes"])
    #homework=10%, quizzes=30%, tests=60%
    homework_weight_av=(0.1)*(homework)
    quiz_weight_av=0.3*quiz
    test_weight_av=0.6*test
    sum_grade=quiz_weight_av+homework_weight_av+test_weight_av
    return sum_grade

def get_letter_grade(score):

    if score >= 90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=60:
        return 'D'
    else:
        return 'F'
#This is an example of how this program will work for individuals for example, Armin
#Note: since Illoyd is not in the student list, I will suse Armin in his place...making a separte list is an option though...
print("Armin's average is:", get_average(armin))
print ("Armin's average is by grade letter:", get_letter_grade (get_average(armin)), "\N{loudly crying face}")
                                                                                      #emoji to express feeling for getting an F
#class average section
def get_class_average(students):
        result=[]
        for students in students:
           result.append(get_average(students))
        return average(result)

print ("Class average is:", get_class_average([armin, mikasa,eren]))
print("Class average by grade letter is:" ,get_letter_grade(get_class_average([armin,mikasa,eren])), "\N{loudly crying face}")
                                                                                                      #emoji  to express feelings for the class average
        
