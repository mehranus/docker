from random import randint

min_random=int(input("please input min number:"))
max_random=int(input("please input max number:"))
#docker remove contaner --> rm
#docker remove images --> rmi
#docker auto remove countaner -->  --rm tag


if(max_random < min_random):
  print("invalid input - shatting down ...")
else:
  rnd_int=randint(min_random,max_random)
  print(rnd_int)  