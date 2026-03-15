#negitive scilicing
college='amrita'
#indexing starts form last with -1
print(college[-5:-2])
#default scilicing 
print(college[:])
#prints nothing becuase of -len(str)
print(college[:-len(college)])
print(college[-len(college):])
