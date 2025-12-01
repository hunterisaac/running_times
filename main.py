from matplotlib import pyplot as plt
import numpy as np
times = ['7:02', '6:53', '6:48', '6:41', '6:28', '6:40', '6:47', '6:06', '6:10', '6:17', '6:09', '5:55']
onlyints = []
parsed = []
number = 0
ints = []
setamount = []
end = 0
o = 0
suspicious = 0
ticknumbers = []
finaltick = []
finalticks = []
for i in times:
    for x in i:
        onlyints.append(x) #Makes all the things into individual characters and saves them to onlyints
for i in onlyints:
    try:
        onlyints.remove(':') #Removes all ':'
    except:
        break
for i in onlyints:
    try:
        a = onlyints[number]
        b = onlyints[number+1] #Re-merges into numbers into strings, but without the ':'.
        c = onlyints[number+2]
        d = a+b+c
        parsed.append(d)
        number = number+3
    except:
        break
for i in parsed:
    anumber = int(i)
    ints.append(anumber) #Makes the numbers in the parsed list integers.
amount = len(ints)
for i in range(amount):
    setamount.append(i) #The amount of scores to tell how many to plot at each solid number.
for i in setamount:
    end = i #Finds the end number for the size.
end = end-1 #Shrinks it to make it more effiecient.
f = plt.figure()
ax = f.add_subplot(111)
ax.yaxis.tick_right()
plt.xticks([])
x = np.array(setamount)
y = np.array(ints)
plt.plot(x,y)
plt.plot(0,800,'w')
plt.plot(end,800,'w')
plt.plot(0,600,'w')
plt.plot(end,600,'w')
f.canvas.draw()
numbers = ax.get_yticklabels() #Get values of the sides
numbers = list(numbers)
for i in numbers:
    o = 0
    x = str(i)
    for z in x:
        #print(x)
        if z == "'":
            try:
                sus = x[o+1]
                sussy = x[o+2]
                sussybaka = x[o+3]
                sussybakas = sus+sussy+sussybaka
                ticknumbers.append(sussybakas)
            except:
                pass
        o = o+1

for i in ticknumbers:
    i = list(i)
    i.insert(1, ':')
    for l in i:
        finaltick.append(l)
for i in finaltick:
    try:
        a = finaltick[suspicious]
        b = finaltick[suspicious+1]
        c = finaltick[suspicious+2]
        d = finaltick[suspicious+3]
        e = a+b+c+d
        finalticks.append(e)
        suspicious = suspicious+4
    except:
        break
print(finalticks)
ax.set_yticklabels(finalticks)
plt.title("My Run Scores")
plt.show()
