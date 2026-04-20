class MyIterator:
    def __init__(self, number_list):
        print("Init")
        self.numbers = number_list 
        self.last_number = None 

    def __next__(self): 
        if self.numbers:
            print("next")
            number = self.numbers.pop(0)
            self.last_number = number
            return number
        else:
            print("StopIteration")
            raise StopIteration

    def __iter__(self):
        return self

list1 = [1, 6, 12, 18]
iterator = MyIterator(list1)

for i in iterator:
     print(i) # will not work because object is not iterable

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

