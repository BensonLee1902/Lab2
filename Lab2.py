

def main():
    print("ET0735 (DevOps for AIOT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average = calc_average(num_list)
    min_max= find_min_max(num_list)
    print("Average temperature is ", average, "\n")
    print("Minimum and maximum temperature is ", min_max, "\n")
    sorted_list = sort_temperature(num_list)
    median = calc_median_temperature(sorted_list)
    print("Median temperature is ", median)

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers seperated by commas(e.g. 5, 67, 32")

def get_user_input():
    print("get_user_input")
    user_input = input()
    string_list = user_input.split(",")
    float_list = []
    for i in range(len(string_list)):
        float_list.append(float(string_list[i]))
    return(float_list)

def calc_average(num_list):
    print("calc_average")
    average = sum(num_list)/len(num_list)
    return(average)

def find_min_max(num_list):
    print("find_min_max")
    min_max = [num_list[0],num_list[0]]
    for i in range(len(num_list)):
        if min_max[0] > num_list[i]:
            min_max[0] = num_list[i]
        if min_max[1] < num_list[i]:
            min_max[1]= num_list[i]
    return(min_max)

def sort_temperature(num_list):
    print("sort_temperature")
    num_list.sort()
    print(num_list)
    return(num_list)

def calc_median_temperature(sorted_list):
    print("calc_median_temperature")
    if (len(sorted_list)%2)==0:
        i = int(len(sorted_list) / 2)
        median = (sorted_list[i-1]+sorted_list[i])/2
    else:
        i = int(len(sorted_list) / 2 - 0.5)
        median = (sorted_list[i])
    return(median)

if __name__ == "__main__":
    main()
