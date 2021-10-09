cover_type = input("What type of cover does the book have?\n")

if cover_type == "soft":
    bound = input("Is the book perfect-bound?\n")
    if bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
elif cover_type == "hard":
    print("Books with hard covers can be more expensive!")
