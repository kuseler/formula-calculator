from math import *

# i did this because I'm sick of online calculators that i have to search for online when I already know the formula for the things I want to calculate,
# but have to enter the different variables new every time

# this is now only a barebones program, but i think it might serve as a backend for django or tkinter later on.
"""
example exercise

an undamped resonant circuit has an inductivity of 1 Henry and a capacity of 1 Farad.
1. What is the frequency?
2. What is the frequency if the inductivity is now 2 Henry?
3. What would the frequency be with a new capacity of 2 Farad and the inductivity of (1) and (2)?

without this program, you have to enter them all manually, and this is only a very short formula,
imagine what a pain that would be with longer ones

1/(2*pi*sqrt(L*C))

Enter Formula: 1/2*pi*sqrt(L*C)
Enter the values of the symbols, default: {}L=1 C=1
1.5707963267948966
Enter the values of the symbols, default: {'L': '1', 'C': '1'}L=2
2.221441469079183
Enter the values of the symbols, default: {'L': '2', 'C': '1'}C=2 L=1
2.221441469079183
Enter the values of the symbols, default: {'C': '2', 'L': '1'}L=2
3.141592653589793
"""

def get_formula_symbols(previous_dic={}):
    dic = dict()
    formula_symbols = input("Enter the values of the symbols, default: {}".format(previous_dic))
    # expected format: "a=5 b=3 c=2"
    for i in formula_symbols.split():
        var,value = i.split("=")
        dic[var] = value
    for i in previous_dic.keys():
        if i not in dic.keys():
            dic[i] = previous_dic[i]
    return dic
            



def generate_equation_string(formula,dic_of_input):
    for i in dic_of_input.keys():
        formula=formula.replace(i, dic_of_input[i])
    return formula


def main():
    input_of_formula = input("Enter Formula: ")
    old_formula_symbols = dict()
    while True:
        formula_symbols = get_formula_symbols(old_formula_symbols)
        old_formula_symbols = formula_symbols
        print(eval(generate_equation_string(input_of_formula,formula_symbols)))
        
    


