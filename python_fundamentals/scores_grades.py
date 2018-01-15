#Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. print accordingly:
#Score: 60 - 69; Grade - D
#Score: 70 - 79; Grade - C
#Score: 80 - 89; Grade - B
#Score: 90 - 100; Grade - A

def scoreGrader():
    import random
    for x in range(10):
        score = random.randint(60,100)
        if score < 70:
            print "Score: {}; Grade - D".format(score)
        elif score >= 70 and score < 80:
            print "Score: {}; Grade - C".format(score)
        elif score >= 80 and score < 90:
            print "Score: {}; Grade - B".format(score)
        else:
            print "Score: {}; Grade - A".format(score)

scoreGrader()
