counter = 0

while(counter < 3):
  print('outerLoop')
  innerCounter = 0
  while(innerCounter < 10):
    print('innerLoop')
    innerCounter+=1

  counter+=1