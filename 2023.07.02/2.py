from utils import important_message

def main() -> None:

    """Запрашивает у пользователя сообщение и выводит его в stdout с помощью функции important_message из другого модуля."""
    
    text = input(' Введите текст: ')
    
    print(f'\n{important_message(text)}\n')
    
    return None

 # C:\Users\Asus\OneDrive\Рабочий стол\Program\dz_python\Bashlykov\2023.07.02
 # 22:10:45 > python -i 2.py
# >>> main()
 # Введите текст: ntrcdgadfgdh

#=====================================================================================================================#
#                                                                                                                     #
#                                                    ntrcdgadfgdh                                                     #
#                                                                                                                     #
#=====================================================================================================================#

# >>> text = 'Обратите внимание на очень важное сообщение от команды разработчиков этой великолепной программы!!!Обратите внимание на очень важное сообщение от команды разработчиков этой великолепной программы!!!'
# >>> msg = important_message(text)
# >>> print(msg)
#=====================================================================================================================#
#                                                                                                                     #
#     Обратите внимание на очень важное сообщение от команды разработчиков этой великолепной программы!!!Обратите     #
#             внимание на очень важное сообщение от команды разработчиков этой великолепной программы!!!              #
#                                                                                                                     #
#=====================================================================================================================#
# >>>