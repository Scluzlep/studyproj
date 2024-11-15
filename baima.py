for female in range(1,101):
    for male in range(1,101):
        for small in range(1,101):
            if male * 2 + female + small * 0.5 == 100 and male + female + small == 100:
                print(male,female,small)
