import sys

if __name__ == "__main__":
    intVar = 0
    floatVar = 0.0
    boolVar = True
    strVar = ''
    listVar = []
    tupleVar = ()
    dictVar = {}
    setVar = set()

#2018038089 이광희 과제#2

print('int형 기본크기->', sys.getsizeof(intVar))
print('float형 기본크기->', sys.getsizeof(floatVar))
print('bool형 기본크기->', sys.getsizeof(boolVar))
print('str형 기본크기->', sys.getsizeof(strVar))
print('list형 기본크기->', sys.getsizeof(strVar))
print('tuple형 기본크기->', sys.getsizeof(tupleVar))
print('dictionary형 기본크기->', sys.getsizeof(dictVar))
print('set형 기본크기->', sys.getsizeof(setVar))


