# Copy Assignment
def sum1(arr):
    sum2 = 0

    for i in arr:
        sum2 +=i
    print('Sum of the array is {}'.format(sum2))

# Main
# array
arr=list(map(int, input("Enter the array(with a space inbetween): ").strip().split()))
print(arr)

sum1(arr)