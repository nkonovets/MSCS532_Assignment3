def get_data(filename): 
    filename = filename

    with open(filename, "r") as file:
        data_line = file.readline() #open file

    str_list = data_line.split(",") #split the data by comma

    num_data = [] # create an empty list

    for i in str_list:
        num_data.append(int(i)) #add each number one by one to the list

    return num_data
