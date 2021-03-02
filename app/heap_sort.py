class LinesHeap:
    def heapify(self, arr, i, length,):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < length and arr[left].line < arr[i].line:
            smallest = left
        else:
            smallest = i
        if right < length and arr[right].line < arr[smallest].line:
            smallest = right
        if i != smallest:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, smallest, length)

    def build(self, arr):
        length = len(arr) - 1
        for i in range(int(length / 2), -1, -1):
            self.heapify(arr, i, length)
