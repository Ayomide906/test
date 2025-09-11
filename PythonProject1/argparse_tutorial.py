import argparse
def first_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="first number")
    parser.add_argument("--number2", help="second number")
    parser.add_argument("--operation", help="operation", \
                        choices=["add", "subtract", "multiply"])  # options user can choosefrom
    # to pass optional argument just put -- in front of the argument name
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)
    n1 = int(args.number1)
    n2 = int(args.number2)
    result = 0
    if args.operation == "add":
        result = n1 + n2
    elif args.operation == "subtract":
        result = n1 - n2
    elif args.operation == "multiply":
        result = n1 * n2
    elif args.operation == "divide":
        result = n1 / n2
    else:
        print("unsupported argument")
    print("Answer of the operation is :", result)
def ass_arg():
    parser=argparse.ArgumentParser()
    parser.add_argument("--Physics", help="physics score")
    parser.add_argument("--Chemistry",help="chemistry score")
    parser.add_argument("--maths", help="maths score")
    args=parser.parse_args()
    print(args.Physics)
    print(args.Chemistry)
    print(args.maths)
    mscore=int(args.maths)
    pscore=int(args.Physics)
    cscore=int(args.Chemistry)
    result=(mscore+pscore+cscore)/3
    print(round(result,2))

if __name__=='__main__':
    first_arg()