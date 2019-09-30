import random


##-------------------------------##
#         INSERTIONSORT           #
##-------------------------------##
# Starts with element i at index 1 and compares with elements j (sorted part of the collection),
# then puts element i in its correct position.
class InsertionSort(object):
    def __init__(self):
        self.comparisons = 0
        self.attributions = 0

    def sort(self, collection):
        for i in range(1, len(collection)):
            self.comparisons += 1
            self.attributions += 1
            j = i - 1
            self.attributions += 1
            temp = collection[i]
            self.attributions += 1
            while j >= 0 and int(temp['weight']) < int(collection[j]['weight']):
                self.comparisons += 2
                collection[j + 1] = collection[j]
                self.attributions += 1
                j = j - 1
                self.attributions += 1
            collection[j + 1] = temp
            self.attributions += 1
        return collection


##-------------------------------##
#         SELECTIONSORT           #
##-------------------------------##
class SelectionSort(object):
    def __init__(self):
        self.comparisons = 0
        self.attributions = 0

    def sort(self, collection):
        for i in range(len(collection)):
            self.comparisons += 1
            self.attributions += 1
            smallest = i
            self.attributions += 1
            for j in range(i, len(collection)):
                self.comparisons += 1
                self.attributions += 1
                if int(collection[smallest]['weight']) > int(collection[j]['weight']):
                    self.comparisons += 1
                    smallest = j
                    self.attributions += 1
            collection[i], collection[smallest] = collection[smallest], collection[i]
            self.attributions += 2
        return collection


##-------------------------------##
#           SHELLSORT             #
##-------------------------------##
class ShellSort(object):
    def __init__(self):
        self.comparisons = 0
        self.attributions = 0

    def sort(self, collection):
        length = len(collection)
        self.attributions += 1
        h = 1
        self.attributions += 1
        while h < length:
            self.comparisons += 1
            if 3 * h + 1 < length:
                self.comparisons += 1
                h = 3 * h + 1
                self.attributions += 1
            else:
                self.comparisons += 1
                break
        while h >= 1:
            self.comparisons += 1
            for i in range(h, length):
                self.comparisons += 1
                self.attributions += 1
                j = i
                self.attributions += 1
                while j >= h and int(collection[j]['weight']) < int(collection[j - h]['weight']):
                    self.comparisons += 2
                    collection[j], collection[j - h] = collection[j - h], collection[j]
                    self.attributions += 2
                    j -= h
                    self.attributions += 1
            h = (h - 1) // 3
            self.attributions += 1
        return collection


##-------------------------------##
#           QUICKSORT             #
##-------------------------------##
# "Randomized" quicksort. The function randomPartition() gets a random index and switches its position with the last
#  index, using the last element (random) as the pivot.
class QuickSort(object):
    def __init__(self):
        self.comparisons = 0
        self.attributions = 0

    def sort(self, collection, start=0, end=-1):
        if end == -1:
            self.comparisons += 1
            end = len(collection) - 1
            self.attributions += 1

        if start < end:
            self.comparisons += 1
            pivot = self.__randomPartition(collection=collection, start=start, end=end)
            self.attributions += 1
            self.sort(collection=collection, start=start, end=pivot - 1)
            self.sort(collection=collection, start=pivot + 1, end=end)

        return collection

    def __partition(self, collection, start, end):
        # uses the last element as the pivot.
        pivot = end
        self.attributions += 1
        i = start - 1
        self.attributions += 1
        j = start
        self.attributions += 1
        while j < end:
            self.comparisons += 1
            if int(collection[j]['weight']) <= int(collection[pivot]['weight']):
                self.comparisons += 1
                i += 1
                self.attributions += 1
                collection[i], collection[j] = collection[j], collection[i]
                self.attributions += 2
            j += 1
            self.attributions += 1
        collection[pivot], collection[i + 1] = collection[i + 1], collection[pivot]
        self.attributions += 2

        # returns the new pivot position:
        return i + 1

    # Chooses a random index in the collection and switches it with the element at the last position,
    #  then calls the partition() function.
    def __randomPartition(self, collection, start, end):
        pivot = random.randint(start, end)
        self.attributions += 1
        collection[pivot], collection[end] = collection[end], collection[pivot]
        self.attributions += 2
        return self.__partition(collection=collection, start=start, end=end)


##-------------------------------##
#  QUICKSORT - PARTIAL INSERTION  #
##-------------------------------##
class QuickSortPI(object):
    def __init__(self):
        self.comparisons = 0
        self.attributions = 0
        self.insertionSort = None

    def sort(self, collection, start=0, end=-1, L=2):
        if end == -1:
            self.comparisons += 1
            end = len(collection) - 1
            self.attributions += 1

        if start < end:
            self.comparisons += 1
            pivot = self.__randomPartition(collection=collection, start=start, end=end)
            self.attributions += 1
            # checks if the partition [start:pivot] is <= L.
            if pivot - 1 - start <= L:
                self.comparisons += 1
                self.insertionSort = InsertionSort()
                self.insertionSort.sort(collection=collection[start:pivot - 1])
                self.attributions += self.insertionSort.attributions
                self.comparisons += self.insertionSort.comparisons
                del self.insertionSort
            else:
                self.comparisons += 1
                self.sort(collection=collection, start=start, end=pivot - 1)
            # checks if the partition [pivot+1:end] is <= L.
            if end - pivot + 1 <= L:
                self.comparisons += 1
                self.insertionSort = InsertionSort()
                self.insertionSort.sort(collection=collection[pivot + 1:end])
                self.attributions += self.insertionSort.attributions
                self.comparisons += self.insertionSort.comparisons
                del self.insertionSort
            else:
                self.comparisons += 1
                self.sort(collection=collection, start=pivot + 1, end=end)

        return collection

    def __partition(self, collection, start, end):
        pivot = end
        self.attributions += 1
        i = start - 1
        self.attributions += 1
        j = start
        self.attributions += 1
        while j < end:
            self.comparisons += 1
            if int(collection[j]['weight']) <= int(collection[pivot]['weight']):
                self.comparisons += 1
                i += 1
                self.attributions += 1
                collection[i], collection[j] = collection[j], collection[i]
                self.attributions += 2
            j += 1
            self.attributions += 1
        collection[pivot], collection[i + 1] = collection[i + 1], collection[pivot]
        self.attributions += 2
        # returns the new pivot position:
        return i + 1

    def __randomPartition(self, collection, start, end):
        pivot = random.randint(start, end)
        self.attributions += 1
        collection[pivot], collection[end] = collection[end], collection[pivot]
        self.attributions += 2
        return self.__partition(collection=collection, start=start, end=end)


##-------------------------------##
#   QUICKSORT - FINAL INSERTION   #
##-------------------------------##
class QuickSortFI(object):
    def __init__(self):
        self.comparisons = 0
        self.attributions = 0
        self.insertionSort = None

    def sort(self, collection, start=0, end=-1, L=2):
        if end == -1:
            end = len(collection) - 1

        if start < end:
            self.comparisons += 1
            pivot = self.__randomPartition(collection=collection, start=start, end=end)
            self.attributions += 1

            if pivot - 1 - start > L:
                self.comparisons += 1
                self.sort(collection=collection, start=start, end=pivot - 1)
            if end - pivot + 1 > L:
                self.comparisons += 1
                self.sort(collection=collection, start=pivot + 1, end=end)

            self.insertionSort = InsertionSort()
            self.insertionSort.sort(collection=collection[start:pivot - 1])
            self.insertionSort.sort(collection=collection[pivot + 1:end])
            self.attributions += self.insertionSort.attributions
            self.comparisons += self.insertionSort.comparisons
            del self.insertionSort

        return collection

    def __partition(self, collection, start, end):
        pivot = end
        self.attributions += 1
        i = start - 1
        self.attributions += 1
        j = start
        self.attributions += 1
        while j < end:
            self.comparisons += 1
            if int(collection[j]['weight']) <= int(collection[pivot]['weight']):
                self.comparisons += 1
                i += 1
                self.attributions += 1
                collection[i], collection[j] = collection[j], collection[i]
                self.attributions += 2
            j += 1
            self.attributions += 1
        collection[pivot], collection[i + 1] = collection[i + 1], collection[pivot]
        self.attributions += 2

        # returns the new pivot position:
        return i + 1

    def __randomPartition(self, collection, start, end):
        pivot = random.randint(start, end)
        self.attributions += 1
        collection[pivot], collection[end] = collection[end], collection[pivot]
        self.attributions += 2
        return self.__partition(collection=collection, start=start, end=end)


##-------------------------------##
#           MERGESORT             #
##-------------------------------##
class MergeSort(object):
    def __init__(self):
        self.comparisons = 0
        self.attributions = 0

    def sort(self, collection, left=0, right=-1, collectionAux=None):
        # in the first execution, collectionAux will be none(null). collectionAux will be created and passed as
        # a parameter for the next executions.
        if right == -1:
            self.comparisons += 1
            right = len(collection) - 1
            self.attributions += 1
        if collectionAux is None:
            self.comparisons += 1
            collectionAux = collection[:]
            self.attributions += 1
        half = left + (right - left) // 2
        self.attributions += 1

        # checking whether the received collection or subcollection has more than one element.
        if left < right:
            self.comparisons += 1
            self.sort(collection=collection, left=left, right=half, collectionAux=collectionAux)
            self.sort(collection=collection, left=half + 1, right=right, collectionAux=collectionAux)
            self.__merge(collection=collection, left=left, right=right, half=half, collectionAux=collectionAux)

        return collection

    def __merge(self, collection, left, right, half, collectionAux):
        # cur variables will iterate through the collection and make comparisons.
        # auxCur indicates the current position in collectionAux.
        leftCur = left
        self.attributions += 1
        leftEnd = half
        self.attributions += 1
        rightCur = half + 1
        self.attributions += 1
        rightEnd = right
        self.attributions += 1
        auxCur = left
        self.attributions += 1

        # while none of the subcollections have reached an end.
        while leftCur <= leftEnd and rightCur <= rightEnd:
            self.comparisons += 2
            if int(collection[leftCur]['weight']) <= int(collection[rightCur]['weight']):
                self.comparisons += 1
                collectionAux[auxCur] = collection[leftCur]
                self.attributions += 1
                leftCur += 1
                self.attributions += 1
            else:
                self.comparisons += 1
                collectionAux[auxCur] = collection[rightCur]
                self.attributions += 1
                rightCur += 1
                self.attributions += 1
            auxCur += 1
            self.attributions += 1

        # only executes when the right subcollection has reached an end and the left one hasn't.
        while leftCur <= leftEnd:
            self.comparisons += 1
            collectionAux[auxCur] = collection[leftCur]
            self.attributions += 1
            auxCur += 1
            self.attributions += 1
            leftCur += 1
            self.attributions += 1

        # only executes when the left subcollection has reached an end and the right one hasn't.
        while rightCur <= rightEnd:
            self.comparisons += 1
            collectionAux[auxCur] = collection[rightCur]
            self.attributions += 1
            auxCur += 1
            self.attributions += 1
            rightCur += 1
            self.attributions += 1

        # now copy every element of the sorted collectionAux to the original collection.
        for i in range(len(collection)):
            self.comparisons += 1
            self.attributions += 1
            collection[i] = collectionAux[i]
            self.attributions += 1


##---------------------------------------##
#      MERGESORT - PARTIAL INSERTION      #
##---------------------------------------##
class MergeSortPI(object):
    def __init__(self):
        self.comparisons = 0
        self.attributions = 0
        self.insertionSort = None

    def sort(self, collection, left=0, right=-1, L=2, collectionAux=None):
        # in the first execution, collectionAux will be none(null). collectionAux will be created and passed as
        # a parameter for the next executions.
        if right == -1:
            self.comparisons += 1
            right = len(collection)-1
            self.attributions += 1
        if collectionAux is None:
            self.comparisons += 1
            collectionAux = collection[:]
            self.attributions += 1
        half = left + (right - left) // 2
        self.attributions += 1
        # checking whether the received collection or subcollection has more than one element.
        if left < right:
            self.comparisons += 1
            if half - left <= L:
                self.comparisons += 1
                self.insertionSort = InsertionSort()
                self.insertionSort.sort(collection=collectionAux[left:half + 1])
                self.attributions += self.insertionSort.attributions
                self.comparisons += self.insertionSort.comparisons
                del self.insertionSort
            else:
                self.comparisons += 1
                self.sort(collection=collection, left=left, right=half, collectionAux=collectionAux)
            if right - half + 1 <= L:
                self.comparisons += 1
                self.insertionSort = InsertionSort()
                self.insertionSort.sort(collection=collectionAux[half + 1:right])
                self.attributions += self.insertionSort.attributions
                self.comparisons += self.insertionSort.comparisons
                del self.insertionSort
            else:
                self.comparisons += 1
                self.sort(collection=collection, left=half + 1, right=right, collectionAux=collectionAux)
            self.__merge(collection=collection, left=left, right=right, half=half, collectionAux=collectionAux)

        return collection

    def __merge(self, collection, left, right, half, collectionAux):
        # cur variables will iterate through the collection and make comparisons.
        # auxCur indicates the current position in collectionAux.
        leftCur = left
        self.attributions += 1
        leftEnd = half
        self.attributions += 1
        rightCur = half + 1
        self.attributions += 1
        rightEnd = right
        self.attributions += 1
        auxCur = left
        self.attributions += 1

        # while none of the subcollections have reached an end.
        while leftCur <= leftEnd and rightCur <= rightEnd:
            self.comparisons += 1
            if int(collection[leftCur]['weight']) <= int(collection[rightCur]['weight']):
                self.comparisons += 1
                collectionAux[auxCur] = collection[leftCur]
                self.attributions += 1
                leftCur += 1
                self.attributions += 1
            else:
                self.comparisons += 1
                collectionAux[auxCur] = collection[rightCur]
                self.attributions += 1
                rightCur += 1
                self.attributions += 1
            auxCur += 1
            self.attributions += 1

        # only executes when the right subcollection has reached an end and the left one hasn't.
        while leftCur <= leftEnd:
            self.comparisons += 1
            collectionAux[auxCur] = collection[leftCur]
            self.attributions += 1
            auxCur += 1
            self.attributions += 1
            leftCur += 1
            self.attributions += 1

        # only executes when the left subcollection has reached an end and the right one hasn't.
        while rightCur <= rightEnd:
            self.comparisons += 1
            collectionAux[auxCur] = collection[rightCur]
            self.attributions += 1
            auxCur += 1
            self.attributions += 1
            rightCur += 1
            self.attributions += 1

        # now copy every element of the sorted collectionAux to the original collection.
        for i in range(len(collection)):
            self.comparisons += 1
            self.attributions += 1
            collection[i] = collectionAux[i]
            self.attributions += 1


##---------------------------------------##
#       MERGESORT - FINAL INSERTION       #
##---------------------------------------##

class MergeSortFI(object):
    def __init__(self):
        self.comparisons = 0
        self.attributions = 0
        self.insertionSort = None

    def sort(self, collection, left=0, right=-1, L=2, collectionAux=None):
        # in the first execution, collectionAux will be none(null). collectionAux will be created and passed as
        # a parameter for the next executions.
        if right == -1:
            self.comparisons += 1
            right = len(collection) - 1
            self.attributions += 1

        if collectionAux is None:
            self.comparisons += 1
            collectionAux = collection[:]
            self.attributions += 1

        half = left + (right - left) // 2
        self.attributions += 1
        # checking whether the received collection or subcollection has more than one element.
        if left < right:
            self.comparisons += 1
            if half - left > L:
                self.comparisons += 1
                self.sort(collection=collection, left=left, right=half, collectionAux=collectionAux)
            if right - half > L:
                self.comparisons += 1
                self.sort(collection=collection, left=half + 1, right=right, collectionAux=collectionAux)
            self.__merge(collection=collection, left=left, right=right, half=half, collectionAux=collectionAux)
            self.insertionSort = InsertionSort()
            collection = self.insertionSort.sort(collectionAux)[:]
            self.attributions += 1
            self.attributions += self.insertionSort.attributions
            self.comparisons += self.insertionSort.comparisons
            del self.insertionSort  # Deletando o objeto para poder não contar os valores multiplas vezes

        return collection

    def __merge(self, collection, left, right, half, collectionAux):
        # cur variables will iterate through the collection and make comparisons.
        # auxCur indicates the current position in collectionAux.
        leftCur = left
        self.attributions += 1
        leftEnd = half
        self.attributions += 1
        rightCur = half + 1
        self.attributions += 1
        rightEnd = right
        self.attributions += 1
        auxCur = left
        self.attributions += 1

        # while none of the subcollections have reached an end.
        while leftCur <= leftEnd and rightCur <= rightEnd:
            self.comparisons += 2
            if int(collection[leftCur]['weight']) <= int(collection[rightCur]['weight']):
                self.comparisons += 1
                collectionAux[auxCur] = collection[leftCur]
                self.attributions += 1
                leftCur += 1
                self.attributions += 1
            else:
                self.comparisons += 1
                collectionAux[auxCur] = collection[rightCur]
                self.attributions += 1
                rightCur += 1
                self.attributions += 1
            auxCur += 1
            self.attributions += 1

        # only executes when the right subcollection has reached an end and the left one hasn't.
        while leftCur <= leftEnd:
            self.comparisons += 1
            collectionAux[auxCur] = collection[leftCur]
            self.attributions += 1
            auxCur += 1
            self.attributions += 1
            leftCur += 1
            self.attributions += 1

        # only executes when the left subcollection has reached an end and the right one hasn't.
        while rightCur <= rightEnd:
            self.comparisons += 1
            collectionAux[auxCur] = collection[rightCur]
            self.attributions += 1
            auxCur += 1
            self.attributions += 1
            rightCur += 1
            self.attributions += 1

        # now copy every element of the sorted collectionAux to the original collection.
        for i in range(len(collection)):
            self.comparisons += 1
            self.attributions += 1
            collection[i] = collectionAux[i]
            self.attributions += 1
