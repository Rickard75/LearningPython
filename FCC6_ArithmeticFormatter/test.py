def arithmetic_arranger(problems, show_answers=True):
    """problems is a list of strings"""
    first_row       = [] # implemento le righe come liste
    second_row      = []
    separator_row   = []
    result_row      = []

    for pb in problems:
        addend_list = pb.split(' ')         # separo numeri e segno
        addend_1 = addend_list[0]  
        # checking addend_1 length
        if (len(addend_1) > 4):
            print("Error: Numbers cannot be more than four digits.")
            break
        if contiene_alfabetici(addend_1) == True:
            print("Error: Numbers must only contain digits")
            break
        # checking correct operator insertion
        if (addend_list[1] == '*'):
            print("Error: Operator must be '+' or '-'.")
            break      
        if (addend_list[1] == '/'):
            print("Error: Operator must be '+' or '-'.")
            break      
        sign     = addend_list[1]
        addend_2 = addend_list[2]
        # checking addend_2 length
        if (len(addend_2) > 4):
            print("Error: Numbers cannot be more than four digits.")
            break
        if contiene_alfabetici(addend_2) == True:
            print("Error: Numbers must only contain digits")
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

def contiene_alfabetici(s):
    for char in s:
        if char.isalpha():
            return True
    return False

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123b + 49"],True)
