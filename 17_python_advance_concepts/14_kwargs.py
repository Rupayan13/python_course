def marks(**kwargs):
    # It will create a dictionary of all the arguments passed
    print(kwargs)
    for person in kwargs.keys():
        print(f"{person} has obtained {kwargs[person]} marks")


marks(Rupayan=95, John=98, Alice=88, Bob=76)
