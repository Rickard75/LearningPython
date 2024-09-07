"""An Arithmetic Formatter"""
# This code is a solution to the FreeCodeCamp challenge "Arithmetic Formatter"
# The challenge is to create a function that receives a list of strings that are arithmetic problems 
# and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument.
# When the second argument is set to True, the answers should be displayed.

# Latest update: 2021-09-07
# Author: Riccardo Carroccio

# Possibe improvements:
# 1. Add a check for the correct operator insertion (only '+' and '-' are allowed)  DONE
# 2. Add a check for the correct number of problems (maximum 5)                     DONE
# 3. Add a check for the correct number of digits (maximum 4)                       DONE
# 4. Add a check for the correct type of characters (only digits are allowed)       DONE




def arithmetic_arranger(problems, show_answers=True):
    """problems is a list of strings"""
    first_row       = [] # implemento le righe come liste
    second_row      = []
    separator_row   = []
    result_row      = []
    counter         = 0  # contatore per il numero di problemi

    for pb in problems:
        addend_list = pb.split(' ')         # separo numeri e segno
        addend_1 = addend_list[0]  
        # checking addend_1 length
        if (len(addend_1) > 4):
            return "Error: Numbers cannot be more than four digits."
        if contiene_alfabetici(addend_1) == True:
            return "Error: Numbers must only contain digits"
        # checking correct operator insertion
        if (addend_list[1] == '*'):
            err = "Error: Operator must be '+' or '-'."
            return err      
        if (addend_list[1] == '/'):
            return "Error: Operator must be '+' or '-'."      
        sign     = addend_list[1]
        addend_2 = addend_list[2]
        # checking addend_2 length
        if (len(addend_2) > 4):
            return "Error: Numbers cannot be more than four digits."
        if contiene_alfabetici(addend_2) == True:
            return "Error: Numbers must only contain digits"

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
        counter += 1
        if counter > 5:
            return "Error: Too many problems."
        
    # Unire gli elementi di ciascuna lista con quattro spazi e stampare le righe risultanti
    output = '    '.join(first_row) + '\n'
    output += '    '.join(second_row) + '\n'
    output += '    '.join(separator_row)
    if show_answers:
        output += '\n' + '    '.join(result_row)

        
    return output


def contiene_alfabetici(s):
    for char in s:
        if char.isalpha():
            return True
    return False


problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems,True))

# print is here used just to control the ouput, the code instruction wanted no print calling
