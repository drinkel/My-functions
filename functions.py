#Разбить строку на слова
#String to words
def words(str):
    i, j, w = 0, 0, []
    
    for i in range(len(text) + 1):
        try:
            if text[i] != ' ':
                continue
            else:
                w.append(text[j:i])
                j = i + 1
        except IndexError:
            w.append(text[j:])
    
    return w


#Отсортировать массив чисел по возрастанию
#Sort an array of numbers in ascending order
def sorting(arr):
    temparr, length = arr, len(arr)
    for i in range(1, length):
        for j in range(i):
            while i < length and temparr[i] < temparr[j]:
                temparr[j], temparr[i] = temparr[i], temparr[j]
                
    return temparr
