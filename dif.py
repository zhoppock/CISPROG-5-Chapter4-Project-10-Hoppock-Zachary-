def dif():
  firstFile = input("What is the first file called? ")
  secondFile = input("What is the second file called? ")

  f = open(firstFile, 'r')
  s = open(secondFile, 'r')

  print("\nAre both files the same?")

  firstText = f.read()
  secondText = s.read()

  if firstText == secondText:
    print("\nYes.")
  else:
    print("\nNo.")
    f = open(firstFile, 'r')
    s = open(secondFile, 'r')
    
    number = 1
    while True: 
      print("\nComparison of line", str(number) + ":")
      line1 = f.readline()
      line2 = s.readline()
      print("First file's line:", line1)
      print("Second file's line:",line2)

      number += 1
      if line1 != line2:
        break
    print("\nThese last printed lines are different!")
      
  f.close()
  s.close()