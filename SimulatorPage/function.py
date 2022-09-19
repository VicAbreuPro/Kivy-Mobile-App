# Function file to process the information (TO BE FINISHED IN A FULLY FUNCTIONAL VERSION!)

# Equipments Data List
equip_list = []


# Function to test the information List (TO BE FINISHED IN A FULLY FUNCTIONAL VERSION!)
def save_list_info(equip_list_aux):

    for item in equip_list_aux:
        print(item)


# Function to calculate the values of each equipment (TO BE FINISHED IN A FULLY FUNCTIONAL VERSION!)
def consume_total(equip_list_aux):
    counter = 0
    total_c = 0
    size = len(equip_list_aux)
    print(size)
    while counter <= size:
        print("test" + str(counter))
        if counter != 0:
            if counter % 2 == 0:
                total_c += int(equip_list_aux[counter])
        counter = counter + 1
    print(str(total_c))
    return total_c
