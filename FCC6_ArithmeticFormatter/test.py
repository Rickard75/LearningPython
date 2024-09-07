def arithmetic_arranger(problems, show_answers=True):
    """problems is a list of strings"""
    first_row       = [] # implemento le righe come liste
    second_row      = []
    separator_row   = []
    result_row      = []

    for pb in problems:
        addend_list = pb.split(' ')         # separo numeri e segno
        addend_1 = addend_list[0]  
        if (len(addend_1) > 4):
            print("Error: Numbers cannot be more than four digits.")
            break
        if (addend_list[1] == '*'):
            print("Error: Operator must be '+' or '-'.")
            break      
        if (addend_list[1] == '/'):
            print("Error: Operator must be '+' or '-'.")
            break      
        sign     = addend_list[1]
        addend_2 = addend_list[2]
        if (len(addend_2) > 4):
            print("Error: Numbers cannot be more than four digits.")
            break

        row_length = max(len(addend_list[0]),len(addend_list[2])) + 2       
        first_row.append(' '*(row_length-len(addend_list[0])) + addend_list[0])        #prima riga
        second_row.append(sign + ' '*(row_length-len(sign)-len(addend_2)) + addend_2)  #seconda riga
        separator_row.append('-'*row_length)                                           #riga separatrice

        if show_answers:          # controllo per visualizzazione risultato
            if sign == '+':
                result = int(addend_1) + int(addend_2)
            elif sign == '-':
                result = int(addend_1) - int(addend_2)
            result_row.append(' '*(row_length-len(str(result))) + str(result))

    # Unire gli elementi di ciascuna lista con quattro spazi e stampare le righe risultanti
    print('    '.join(first_row))
    print('    '.join(second_row))
    print('    '.join(separator_row))
    if show_answers:
        print('    '.join(result_row))

    return problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)
