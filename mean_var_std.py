from pickle import FALSE, TRUE
from turtle import shape
import numpy as np

mylist = [0,1,2,3,4,5,6,7,8]

isprime = "TRUE"

for i in range(1,len(mylist)):
    if len(mylist)%i == 0:
        break
    else:
        isprime = "FALSE"



def calculate(ninedigit):
  if len(ninedigit) != 9 or not all([isinstance(item, int) for item in ninedigit]):
    return "Invalid Input"
  else:
    x = np.array(ninedigit)
    shaped = x.reshape(3,3)

    big_dict = {
        'mean': [np.mean(shaped, axis=0), np.mean(shaped, axis=1), np.mean(shaped)],
        'variance': [np.var(shaped, axis=0), np.var(shaped, axis=1), np.var(shaped)],
        'standard deviation': [np.std(shaped, axis=0), np.std(shaped, axis=1), np.std(shaped)],
        'min': [np.min(shaped, axis=0), np.min(shaped, axis=1),np.min(shaped)],
        'max': [np.max(shaped, axis=0),np.max(shaped, axis=1),np.max(shaped)],
        'sum': [np.sum(shaped, axis=0),np.sum(shaped, axis=1),np.sum(shaped)]
    }


    return big_dict








print(calculate(mylist))
