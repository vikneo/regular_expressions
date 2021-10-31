import re

text = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. ' \
       'Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. ' \
       'Donec quam felis, ultricies nec, pellentesque eu, -11 pretium quis, sem. Nu23lla consequat massa quis enim. ' \
       'Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, ' \
       'venenatis vitae, 12 justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. ' \
       'Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, ' \
       'consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. ' \
       'Phasellus viverra nulla ut metus varius laoreet. -33 Quisque rutrum. Aenean imperdiet. ' \
       'Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. 43 Etiam rhoncus. ' \
       'Maecenas tempus, tellus eget condimentum rhon5cus, sem quam semper libero,' \
       ' sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. ' \
       'Maecenas nec 2 odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. ' \
       'Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. ' \
       'Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, ' \
       'leo 65 eget bibendum sodales, augue velit cursus nunc,'

# Пример, дан рыбный текст.

match = re.findall(r'\b\w{4}\b', text)  # создадим шаблон который выводит все слова с длиной 4 символа
print(match)

match = re.findall(r'nec', text)  # выведем все вхождения по шаблону
print(match)

match = re.findall(r'\bnec\b', text)  # выведем все слова по шаблону
print(match)

# =========================================================================
# Практика для специальных символов такие как: \.^$?+*()[]{}

match = re.findall(r'[nN]e[cn]', text)
"""
выводим вхождения подстроки по шаблону который начинается с 
маленькой или большой буквы в данном случае "Ne или ne" и с окончаением
в квадратных скобках [cn]
"""
print(match)

""" или можно учесть любое из окончаний записав так: """
match = re.findall(r'[nN]e[a-z]', text)
print(match)

""" Так же возможен поиск цифр """
match = re.findall(r'[0-9]', text)  # ищем все вхождения чисел от 0 до 9
print(match)

match = re.findall(r'\b[0-9]+\b', text)  # а здесь ищем цифры положительные по шаблону
print(match)

match = re.findall(r'[-0-9]+', text)  # а здесь ищем все цифры по шаблону
print(match)

""" Поиск символов через отрицание "^" """
match = re.findall(r'[^-0-9]', text)  # поиск всех символов КРОМЕ чисел, \n, \t
print(match)

match = re.findall(r'[^-0-9]+', text)  # поиск всех слов КРОМЕ чисел, \n, \t
print(match)

""" Пример поиска для шестнадцатеричных значений """
test_text = '0xa, 0x5, 0xF, 0xf'
match = re.findall(r'0x[\da-fA-F]', test_text)  # на примере видно, что все значения подходят под шаблон
print(match)