def climb_ladder(step_rem, step_cross):
    if step_rem > step_cross:
        print("Still some way to go!")
    else:
        print("We are almost there!")


climb_ladder(5, 2)
climb_ladder(2, 5)
