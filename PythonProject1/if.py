india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
user1=input("Enter the first city: ")
user2=input("Enter the second city: ")
if user1 in india and user2 in india:
    print("Both cities are india")
elif user1 in pakistan and user2 in pakistan:
    print("Both cities are pakistan")
elif user1 in bangladesh and user2 in bangladesh:
    print("Both cities are pakistan")
else:
    print("They are of different cities")
