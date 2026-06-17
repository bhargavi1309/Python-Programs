nums = [10,20,30]

itr = iter(nums)#iterator object
#iterator is a object which contains a countable number of values and can be iterated upon, meaning that you can traverse through all the values. 
# It implements the iterator protocol, which consists of the methods __iter__() and __next__().

print(next(itr))
print(next(itr))
print(next(itr))