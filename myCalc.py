## 함수 선언부
def add_func(n1, n2) :
    return n1 + n2

def diff_func(n1, n2) :
    return n1 - n2

## 전역 변수부
num1, num2, result = 300, 200, 0

## 메인 코드부
result = add_func(num1, num2)
print(num1,"+", num2, "=", result)

result = diff_func(num1, num2)
print(num1,"-", num2, "=", result)



