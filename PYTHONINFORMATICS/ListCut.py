#One function modify a list removing its head and tail the other to return a new list containing all but head and tail.

sample =['a','b','c','d','e','f','g']

def modify(list1):
    list1.pop(-1)
    list1.pop(0)
    return None

def create(list1):
    return list1[1:len(list1)-1]

print "Sample list: " , sample
modify(sample)
print "Sample (modified) with head and tail cut: ", sample
print "New list with head and tail cut: ", create (sample)
print "Original list remains untouched: ", sample
