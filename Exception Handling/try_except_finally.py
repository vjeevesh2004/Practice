try:
    i = int(input("Enter a number"))
    c = 1/i
except Exception as e:
    print(e)
    exit()

# it will get print whether program runs or not.
finally: 
    print("We are done")

