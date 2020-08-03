import json
with open('text_7.txt','r',encoding='utf-8') as comp_sol:
    dict_profit= dict()
    lst_profit=[]
    profit_plus=0
    i=0
    for firm in comp_sol:
        firm=firm.split()

        profit = int(firm[2])-int(firm[3])
        dict_profit[firm[0]] = profit
        if profit >0:
            profit_plus+=profit
            i+=1




    lst_profit.append(dict_profit)

    lst_profit.append(dict(average_profit = profit_plus/i))

    print(lst_profit)
with open ('my_file.json', 'w',encoding='utf-8') as js_obj:
    js_str = json.dumps(lst_profit,indent=4,separators=(". "," = "))
    json.dump(js_str,js_obj)
    print('Данные сохранены в файле  my_file.json')
    print(js_str)



