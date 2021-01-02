test = int(input())
while test:
    setters,problems,days = map(int,input().split(' '))

    setterProblems = []
    setterProblems.extend(map(int,input().split(' ')))

    contestDays = sum(setterProblems)//problems

    if contestDays <= days:
        print(contestDays)
    else:
        print(days)
    test -= 1
