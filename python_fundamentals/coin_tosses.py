# write a function that calculates the number of heads or tails from a coin toss 5,000 times


def coinTossCounter():
    #initalize counts at 1 because they wont be called untill there is a head or tail tossed
    head_count = 1
    tail_count = 1
    import random
    for x in range(5000):
        random_num = round(random.random())
        if random_num == 1:
            print 'Throwing a coin...its a Head!... got {} head(s) so far'.format(head_count)
            head_count += 1
        else:
            print 'Throwing a coin...its a Tail!... got {} tails(s) so far'.format(tail_count)
            tail_count += 1

coinTossCounter()

