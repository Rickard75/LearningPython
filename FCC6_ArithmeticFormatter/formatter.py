def arithmetic_arranger(problems, show_answers=True):
    """problems is a list of strings"""
    for pb in problems:
        addend_list = pb.split(' ')         # separo numeri e segno
        addend_1 = addend_list[0]           
        sign     = addend_list[1]
        addend_2 = addend_list[2]

        row_length = max(len(addend_list[0]),len(addend_list[2])) + 2       
        print(' '*(row_length-len(addend_list[0])) + addend_list[0])        #prima riga
        print(sign + ' '*(row_length-len(sign)-len(addend_2)) + addend_2)   #seconda riga
        print('-'*row_length)                                               #riga separatrice

        if (show_answers == True):          # controllo per visualizzazione risultato
            if (sign == '+'):
                sum = int(addend_1) + int(addend_2)
                str_sum = str(sum)
                print(' '*(row_length-len(str_sum)) + str_sum)
            elif (sign == '-'):
                sub = int(addend_1) - int(addend_2)
                str_sub = str(sub)
                print(' '*(row_length-len(str_sub)) + str_sub)
                
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

# New retry