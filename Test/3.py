grades = "FFFFFDCBAAA"

def get_g(jgvb):
    print(grades)
    return grades[(jgvb//10)]


def Call():
    print(grades)
    print(grades[2])
    print(grades.split("D"))

Call()

# name = input()
# grade = int(input())
# print(name,":",get_g(grade))