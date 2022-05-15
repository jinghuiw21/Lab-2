def main():
    display_main_menu()
    string_num = enter_num()
    list_num = get_user_input(string_num)
    print(calc_average(list_num))
    print(calc_min_max_temperature(list_num) )


def display_main_menu():
    print("display_main_menu")
    print("Enter a sort of numbers with commas(e.g. 5,6,7,8)")


def enter_num():
    number = input()
    return number


def get_user_input(string_num):
    get_number = string_num.split(",")
    float_list = [float(i) for i in get_number]
    return float_list


def calc_average(list_num):
    sum1 = 0.0
    count = len(list_num)

    for p in list_num:
        sum1 = sum1 + p

    average = sum1 / count

    return average


def calc_min_max_temperature(list_num):
    max_num = list_num[1]
    for i in list_num:
        if i > max_num:
            max_num = i

    min_num = list_num[1]
    for i in list_num:
        if i < min_num:
            min_num = i

    return [max_num, min_num]



if __name__ == "__main__":
    main()
