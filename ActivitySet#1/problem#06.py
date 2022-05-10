l = []
while True:
  num = input("Enter a number:")
  if num == 'done':
    break
  try:
    
      x = int(num)
  except ValueError:
    print('Invalid input')
    continue
  l.append(x)
for i in range(len(l)):
  for j in range(len(l)):
    if l[i]< l[j]:
      l[i],l[j] = l[j],l[i]
minimum = l[0]
maximum = l[-1]
print("Maximum is", maximum)
print("Minimum is", minimum)
