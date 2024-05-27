import random


def task1(donor, recipient):
    if donor == "O":
        return True
    if donor == "AB" and recipient == "AB":
        return True
    if donor == "A" and (recipient == "A" or recipient == "AB"):
        return True
    if donor == "B" and (recipient == "B" or recipient == "AB"):
        return True

    return False

def monte():
    
    tests = 1000000
    passed = 0
    for i in range(tests):
        donors = ["A", "B", "O"]
        recipients = ["A", "B", "AB"]
        outs = []
        for j in range(3):
            d = random.randint(0,len(donors)-1)
            r = random.randint(0,len(recipients)-1)

            d = donors.pop(d)
            r = recipients.pop(r)

            outs.append(task1(d,r))
        
        if all(outs):
            passed += 1
    
    print(passed, tests)



if __name__ == "__main__":
    monte()