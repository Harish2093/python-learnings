try:
    print("I will try running this part")
except Exception  as e:
    print("I will run in case of exception")
else:
    print("I runs when there is no exception")
finally:
    print("I run all the times")