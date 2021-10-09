search = input("Where should I look?\n")

if search == "in the bedroom":
    location = input("Where in the bedroom should I look?\n")
    if location == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")
elif search == "in the bathroom":
    location = input("Where in the bathroom should I look?\n")
    if location == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")
elif search == "in the lab":
    location = input("Where in the lab should I look?\n")
    if location == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")
