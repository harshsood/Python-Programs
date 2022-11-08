def bubble_sort(self):
    for num in range(len(list)-1, 0, -1):
        for i in range(num):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list = [15, 2, 31, 48, 30]
bubble_sort(list)
print(list)
