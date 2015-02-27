largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    else:
        try:
            n = int(num)
        except:
            print "Invalid input"
            continue
        if largest is None or n > largest:
            largest = n
        if smallest is None or n < smallest:
            smallest = n

print "Maximum is", largest
print "Minimum is", smallest