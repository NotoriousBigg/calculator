#A code for a simple calculator
def sum(a, b):
    return a + b
def diff(a, b):
    return a - b
def div(a, b):
    return a/b
def product(a, b):
    return a * b
def main():
    a = int(input("Enter value for A: "))
    b = int(input("Enter value for B: "))
    #sum
    print("The sum is {}".format(sum(a, b)))
    #difference
    print("The difference is {}".format(diff(a, b)))
    #division
    print("The division is {}".format(div(a, b)))
    #product
    print("The product is {}".format(product(a, b)))

main()
