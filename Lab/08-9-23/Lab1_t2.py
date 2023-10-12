thistuple = ("chocolate", "mango", "vanilla", "strawberry")
newtuple=("icecream","shake","cofee","juice")
thirdtuple=thistuple+newtuple
print(thirdtuple)

newlist=list(thistuple)

newlist.append("cadberry")
thistuple=tuple(newlist)
print(thistuple)
