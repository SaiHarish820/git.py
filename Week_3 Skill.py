
## List program
list =['abc', 123, 'sai', 84974]
print(list)
print(list[0])
print(list[1:3])
print(list[2:])

##   Tuple Program
tuple = ('abcd',1234,"sai","Harish")
tinytuple = (123 , "john")
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tinytuple*2) #repeats the list
print(tuple+tinytuple) #prints concatenated tuples


###  Dictionary program


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
dict[3] = "This is Three"
print(dict['one'])
print(dict[2] , dict[3])
tinydict = { 'name ': 'john', 'code' : 6345 ,'dept' : "CSE"}
print(tinydict)

##   To split and join the given string

str = "My name is Harish"
print(str.split(" "))
print("-".join(str.split()))

### Finding the Maximum Elements

list1 = [10,20,30,40,50,60]
print("The Maximum number in the List is: " , max(list1))
print("The sum of the elements: " , sum(list1))
