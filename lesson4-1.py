from sys import argv

script, hours, salary, prize = argv

def work_func(a, b, c):
    res_work = int(a) * int(b) + int(c)
    return res_work


print(f'При ставке  {hours} рублей  и выработке {salary} часов, с учетом премии {prize} рублей \nРабочий сможет заработать {work_func(hours, salary, prize)} рублей')
