from df import my_arguments, yes_list


def elephant(max_try: int, fail_answer: str, win_answer: str, counter=0, arg_number=0) -> str:
    """Заставляю купить слона"""
    if counter <= max_try:
        print(my_arguments[arg_number])
        user_answer = input('Купи слона? ')
        if user_answer in yes_list:
            return win_answer
        else:
            print('Решайся!')
        return elephant(max_try, fail_answer, win_answer, counter + 1, arg_number + 1)

    else:
        return fail_answer


if __name__ == '__main__':
    elephant(4, 'Okeey', 'Поздравляю с покупкой!')
