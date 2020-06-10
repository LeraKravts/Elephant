from df import my_arguments, yes_list


def elephant(max_try: int,  fail_answer: str, win_answer: str, counter=0):
    """Заставляю купить слона"""
    if counter <= max_try:
        print(my_arguments[counter])
        user_answer = input('Купи слона? ')
        if user_answer in yes_list:
            print(win_answer)

        else:
            elephant(max_try, fail_answer, win_answer, counter + 1)

    else:
        print(fail_answer)


if __name__ == '__main__':
    elephant(4, 'Okeey', 'Поздравляю с покупкой!')
