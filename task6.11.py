lst = []

count = 0

sm = 0

while True:

   try:

       lst += [int(input())]

   except:

       break

print('You entered:', end=' ')

for i in lst:

   sm += i

   count += 1

   if i != lst[-1]:

       print(i, end=', ')

   else:

       print(i)

print(f'Total: {sm}')

print(f'Average: {sm / count}')


