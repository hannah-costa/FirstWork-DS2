import random


##-------------------------------##
#         INSERTIONSORT           #
##-------------------------------##
# Starts with element i at index 1 and compares with elements j (sorted part of the collection),
# then puts element i in its correct position.
class InsertionSort(object):
    def sort(self, collection):
        for i in range(1, len(collection)):
            j = i - 1
            temp = collection[i]
            while j >= 0 and int(temp['weight']) < int(collection[j]['weight']):
                collection[j + 1] = collection[j]
                j = j - 1
            collection[j + 1] = temp
        return collection


##-------------------------------##
#         SELECTIONSORT           #
##-------------------------------##

class SelectionSort(object):
    def sort(self, collection):
        for i in range(len(collection)):
            smallest = i
            for j in range(i, len(collection)):
                if int(collection[smallest]['weight']) > int(collection[j]['weight']):
                    smallest = j
            collection[i], collection[smallest] = collection[smallest], collection[i]
        return collection


##-------------------------------##
#           SHELLSORT             #
##-------------------------------##

class ShellSort(object):
    def sort(self, collection):
        length = len(collection)
        h = 1
        while h < length:
            if 3 * h + 1 < length:
                h = 3 * h + 1
            else:
                break
        while h >= 1:
            for i in range(h, length):
                j = i
                while j >= h and int(collection[j]['weight']) < int(collection[j - h]['weight']):
                    collection[j], collection[j - h] = collection[j - h], collection[j]
                    j -= h
            h = (h - 1) // 3
        return collection


##-------------------------------##
#           QUICKSORT             #
##-------------------------------##
# "Randomized" quicksort. The function randomPartition() gets a random index and switches its position with the last
#  index, using the last element (random) as the pivot.
class QuickSort(object):
    def sort(self, collection, start=0, end=-1):
        if end == -1:
            end = len(collection) - 1
        if start < end:
            pivot = randomPartition(collection, start, end)

            quickSort(collection, start, pivot - 1)
            quickSort(collection, pivot + 1, end)

        return collection

    def partition(self, collection, start, end):
        # uses the last element as the pivot.
        pivot = end
        i = start - 1
        j = start
        while j < end:
            if int(collection[j]['weight']) <= int(collection[pivot]['weight']):
                i += 1
                collection[i], collection[j] = collection[j], collection[i]
            j += 1
        collection[pivot], collection[i + 1] = collection[i + 1], collection[pivot]

        # returns the new pivot position:
        return i + 1

    # Chooses a random index in the collection and switches it with the element at the last position,
    #  then calls the partition() function.
    def randomPartition(self, collection, start, end):
        pivot = random.randint(start, end)
        collection[pivot], collection[end] = collection[end], collection[pivot]
        return partition(collection, start, end)


##-------------------------------##
#  QUICKSORT - PARTIAL INSERTION  #
##-------------------------------##

class QuickSortPI(object):
    def sort(self, collection, start=0, end=-1, L=-1):
        if end == -1:
            end = len(collection) - 1
        if start < end:
            pivot = randomPartition(collection, start, end)
            # checks if the partition [start:pivot] is <= L.
            if pivot - 1 - start <= L:
                insertionSort(collection[start:pivot - 1])
            else:
                quickSortPI(collection, start, pivot - 1)
            # checks if the partition [pivot+1:end] is <= L.
            if end - pivot + 1 <= L:
                insertionSort(collection[pivot + 1:end])
            else:
                quickSortPI(collection, pivot + 1, end)

        return collection

    def partition(self, collection, start, end):
        pivot = end
        i = start - 1
        j = start
        while j < end:
            if int(collection[j]['weight']) <= int(collection[pivot]['weight']):
                i += 1
                collection[i], collection[j] = collection[j], collection[i]
            j += 1
        collection[pivot], collection[i + 1] = collection[i + 1], collection[pivot]

        # returns the new pivot position:
        return i + 1

    def randomPartition(self, collection, start, end):
        pivot = random.randint(start, end)
        collection[pivot], collection[end] = collection[end], collection[pivot]
        return partition(collection, start, end)


##-------------------------------##
#   QUICKSORT - FINAL INSERTION   #
##-------------------------------##
class QuickSortFI(object):
    def sort(self, collection, insertionSort, start=0, end=-1, L=-1):
        if end == -1:
            end = len(collection) - 1
        if start < end:
            pivot = randomPartition(collection, start, end)

            if pivot - 1 - start > L:
                quickSortPI(collection, start, pivot-1)
            if end - pivot + 1 > L:
                quickSortPI(collection, pivot + 1, end)

            insertionSort(collection[start:pivot - 1])
            insertionSort(collection[pivot + 1:end])

        return collection

    def partition(self, collection, start, end):
        pivot = end
        i = start - 1
        j = start
        while j < end:
            if int(collection[j]['weight']) <= int(collection[pivot]['weight']):
                i += 1
                collection[i], collection[j] = collection[j], collection[i]
            j += 1
        collection[pivot], collection[i + 1] = collection[i + 1], collection[pivot]

        # returns the new pivot position:
        return i + 1

    def randomPartition(self, collection, start, end):
        pivot = random.randint(start, end)
        collection[pivot], collection[end] = collection[end], collection[pivot]
        return partition(collection, start, end)


##-------------------------------##
#           MERGESORT             #
##-------------------------------##
class MergeSort(object):
    def sort(self, collection, left=0, right=-1, collectionAux=None):
        # in the first execution, collectionAux will be none(null). collectionAux will be created and passed as
        # a parameter for the next executions.
        if right == -1:
            right = len(collection) - 1
        if collectionAux is None:
            collectionAux = collection[:]
        half = left + (right - left) // 2
        # checking whether the received collection or subcollection has more than one element.
        if left < right:
            mergeSort(collection, left, half, collectionAux)
            mergeSort(collection, half + 1, right, collectionAux)
            merge(collection, left, right, half, collectionAux)

        return collection

    def merge(self, collection, left, right, half, collectionAux):
        # cur variables will iterate through the collection and make comparisons.
        # auxCur indicates the current position in collectionAux.
        leftCur = left
        leftEnd = half
        rightCur = half + 1
        rightEnd = right
        auxCur = left

        # while none of the subcollections have reached an end.
        while leftCur <= leftEnd and rightCur <= rightEnd:
            if int(collection[leftCur]['weight']) <= int(collection[rightCur]['weight']):
                collectionAux[auxCur] = collection[leftCur]
                leftCur += 1
            else:
                collectionAux[auxCur] = collection[rightCur]
                rightCur += 1
            auxCur += 1

        # only executes when the right subcollection has reached an end and the left one hasn't.
        while leftCur <= leftEnd:
            collectionAux[auxCur] = collection[leftCur]
            auxCur += 1
            leftCur += 1

        # only executes when the left subcollection has reached an end and the right one hasn't.
        while rightCur <= rightEnd:
            collectionAux[auxCur] = collection[rightCur]
            auxCur += 1
            rightCur += 1

        # now copy every element of the sorted collectionAux to the original collection.
        for i in range(len(collection)):
            collection[i] = collectionAux[i]


##---------------------------------------##
#      MERGESORT - PARTIAL INSERTION      #
##---------------------------------------##

class MergeSortPI(object):
    def sort(self, collection, insertionSort, left=0, right=-1, L=-1, collectionAux=None):
        # in the first execution, collectionAux will be none(null). collectionAux will be created and passed as
        # a parameter for the next executions.
        if collectionAux is None:
            collectionAux = collection[:]
        half = left + (right - left) // 2
        # checking whether the received collection or subcollection has more than one element.
        if left < right:
            if half - left <= L:
                insertionSort(collectionAux[left:half + 1])
            else:
                mergeSort(collection, left, half, collectionAux)
            if right - half + 1 <= L:
                insertionSort(collectionAux[half + 1:right])
            else:
                mergeSort(collection, half + 1, right, collectionAux)
            merge(collection, left, right, half, collectionAux)

        return collection

    def merge(self, collection, left, right, half, collectionAux):
        # cur variables will iterate through the collection and make comparisons.
        # auxCur indicates the current position in collectionAux.
        leftCur = left
        leftEnd = half
        rightCur = half + 1
        rightEnd = right
        auxCur = left

        # while none of the subcollections have reached an end.
        while leftCur <= leftEnd and rightCur <= rightEnd:
            if int(collection[leftCur]['weight']) <= int(collection[rightCur]['weight']):
                collectionAux[auxCur] = collection[leftCur]
                leftCur += 1
            else:
                collectionAux[auxCur] = collection[rightCur]
                rightCur += 1
            auxCur += 1

        # only executes when the right subcollection has reached an end and the left one hasn't.
        while leftCur <= leftEnd:
            collectionAux[auxCur] = collection[leftCur]
            auxCur += 1
            leftCur += 1

        # only executes when the left subcollection has reached an end and the right one hasn't.
        while rightCur <= rightEnd:
            collectionAux[auxCur] = collection[rightCur]
            auxCur += 1
            rightCur += 1

        # now copy every element of the sorted collectionAux to the original collection.
        for i in range(len(collection)):
            collection[i] = collectionAux[i]


##---------------------------------------##
#       MERGESORT - FINAL INSERTION       #
##---------------------------------------##

class MergeSortFI(object):
    def sort(self, collection, insertionSort, left=0, right=-1, L=-1, collectionAux=None):
        # in the first execution, collectionAux will be none(null). collectionAux will be created and passed as
        # a parameter for the next executions.
        if right == -1:
            right = len(collection) - 1
        if collectionAux is None:
            collectionAux = collection[:]
        half = left + (right - left) // 2
        # checking whether the received collection or subcollection has more than one element.
        if left < right:
            if half - left > L:
                mergeSort(collection, left, half, collectionAux)
            if right - half > L:
                mergeSort(collection, half + 1, right, collectionAux)
            merge(collection, left, right, half, collectionAux)
            insertionSort(collection)

        return collection

    def merge(self, collection, left, right, half, collectionAux):
        # cur variables will iterate through the collection and make comparisons.
        # auxCur indicates the current position in collectionAux.
        leftCur = left
        leftEnd = half
        rightCur = half + 1
        rightEnd = right
        auxCur = left

        # while none of the subcollections have reached an end.
        while leftCur <= leftEnd and rightCur <= rightEnd:
            if int(collection[leftCur]['weight']) <= int(collection[rightCur]['weight']):
                collectionAux[auxCur] = collection[leftCur]
                leftCur += 1
            else:
                collectionAux[auxCur] = collection[rightCur]
                rightCur += 1
            auxCur += 1

        # only executes when the right subcollection has reached an end and the left one hasn't.
        while leftCur <= leftEnd:
            collectionAux[auxCur] = collection[leftCur]
            auxCur += 1
            leftCur += 1

        # only executes when the left subcollection has reached an end and the right one hasn't.
        while rightCur <= rightEnd:
            collectionAux[auxCur] = collection[rightCur]
            auxCur += 1
            rightCur += 1

        # now copy every element of the sorted collectionAux to the original collection.
        for i in range(len(collection)):
            collection[i] = collectionAux[i]


if __name__ == '__main__':
    collection = [6, 1, 3, 4, 3, 2, 9, 3]
    #       [1, 2, 3, 3, 3, 4, 6, 9]
    # print(insertionSort(collection))
    # print(selectionSort(collection))
    # print(shellSort(collection))
    # print(quickSort(collection, 0, 7)) # quicksort
    # print(quickSortPI(collection, 0, 7, 2)) # quicksort with partial insertion
    # print(quickSortFI(collection, 0, 7, 2))  # quicksort with total insertion
    # print(mergeSort(collection, 0, 7))
    print(mergeSortPI(collection, 0, 7, 2))
    # print(mergeSortFI(collection, 0, 7, 2))
