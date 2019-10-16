class QuickSort:
    def __init__(self, array):
        self.array = array

    def quick_sort(self, left, right):
        if left >= right:
            return
        pivot = self.array[(left + right) // 2]
        new_border = self.partition(left, right, pivot)
        self.quick_sort(left, new_border - 1)
        self.quick_sort(new_border, right)

    def partition(self, left, right, pivot):
        while(left <= right):
            while(self.array[left] < pivot):
                left += 1

            while(self.array[right] > pivot):
                right -= 1

            if left <= right:
                self.array[left], self.array[right] = self.array[right], self.array[left]
                left += 1
                right -= 1

        return left

    def sort(self):
        self.quick_sort(0, len(self.array) - 1)
        return self.array


array = [10, 7, 8, 6, 3, 2, 12]
array = QuickSort(array).sort()
print(array)