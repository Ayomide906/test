def print_patterns(num):
    print("__name__ :",__name__)
    """

    function to write ascending star
    """
    for i in range(num):
        s=""
        for j in range(i+1):
            s=s +"*"
        print(s)
if __name__ =="__main__":
    print_patterns(5)

