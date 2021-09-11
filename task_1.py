names = ['aLfred', 'djonataN', 'irOn MAN', 'vasYa']
upper_list=list(map(lambda x:x.upper(),names))
print(upper_list)


numbers = [4, 17, 3, 90, 28, 55]
print(list(filter(lambda x: x % 2, numbers)))

from functools import reduce
numbers = [4, 17, 3, 90, 28, 55]
a = 28274400
b = 424116000
print(b/a)
numbers.append(15)
sum_all = reduce(lambda x,y: x * y, numbers)
print(sum_all)

palindromes = ['hello', 'sentences where punctuation', 45,'Able was I, ere I saw Elba', 34.0, 78.87, 'found', 'level', '12/11/21', 'radar','stats']
a = (palindromes[3], palindromes[7], palindromes[8], palindromes[9],palindromes[10])
print(list(a))


# dns 

