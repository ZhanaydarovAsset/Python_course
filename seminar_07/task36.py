def mult(num1, num2):
    return num1 * num2

def print_operation_table(operation, num_rows, num_columns):
    res = f""
    for i in range(1,num_columns+1):
        for j in range(1, num_rows+1):
            res += str(operation(i, j))+" "
        res += "\n"
    print(res)    

a = int(input('a: '))
b = int(input('b: '))
print_operation_table(mult, a, b)