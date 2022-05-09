""" FIND AN ARRAY IS SORTED OR NOT """
array = [1, 2, 3, 4, 80, 9, 12]

class checkSorted:
    def checkSortedArray(self, array):
        return self.helperSort(array, 0)

    def helperSort(self, array, index):
        if index == len(array) - 1:
            return True
        return (array[index] <= array[index + 1]) and self.helperSort(array, index+1)

check = checkSorted()
print(check.checkSortedArray(array))

""" LINEAR SEARCH WITH RECURSION """
class findInLinearSearch:
    def linearSearch(self, array, target):
        return self.helperSearch(array, target, 0)

    def returnTarget(self, array, target):
        return self.searchRetIndex(array, target, 0)

    def findAllIndex(self, array, target):
        return self.findAllHelper(array, target, 0, [])

    def findAllTwo(self, array, target):
        return self.findAllHelper2(array, target, 0)

    
    def helperSearch(self, array, target, index):
        if index == len(array):
            return False
        return (array[index] == target) or self.helperSearch(array, target, index+1)

    def searchRetIndex(self, array, target, index):
        if index == len(array):
            return -1
        if array[index] == target:
            return index
        return self.searchRetIndex(array, target, index+1)

    def findAllHelper(self, array, target, index, lst):
        if index == len(array):
            return lst
        if array[index] == target:
            lst.append(index)
    
    def findAllHelper2(self, array, target, index):
        lst = []
        if index == len(array):
            return lst
        
        if array[index] == target:
            lst.append(index)
        
        result = self.findAllHelper2(array, target, index+1)
        lst.append(result)
        return lst

search = findInLinearSearch()
print(search.returnTarget(array, 9))
print(search.findAllTwo(array, 12))

