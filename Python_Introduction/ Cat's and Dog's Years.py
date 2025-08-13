test_values = [10, 1, 2]

for human_years in test_values:
    
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9 
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5
    print([human_years, cat_years, dog_years])
