from tkinter import SW, Button, Label, Tk

#n1 is the first input number, n2 is the second, operator is the operation, comma is to check if the number has comma, same as comma2, ans is to check if answer was call'd
n1 = ''; n2 = ''; operator = ''; comma = False; comma2 = False; ans = False

class Calculator:
    #This function save numbers in each variable
    def numb(self, n):
        global n1; global n2; global operator
        if operator == '':
            n1 += str(n)
            self.refresh_value()
        else:
            n2 += str(n)
            self.refresh_value()
    
    #This function define the operator
    def operator(self, op):
        global operator; global n2
        if n1 != '' and n2 == '':
            operator = op
            self.refresh_value()
    
    #This function put comma in the numbers, they do all the checking if number has comma or not
    def add_comma(self):
        global n1; global n2; global operator; global comma; global comma2
        if not comma and n1 != '' and n2 == '' and operator == '':
            n1 += ','
            comma = True
            self.refresh_value()
        if not comma2 and n2 != '':
            n2 += ','
            comma2 = True
            self.refresh_value()
    
    #That function turns the number negative or positive
    def minus_op(self):
        global n1; global n2; global operator
        if n1 != '' and operator == '':
            if '-' in n1:
                n1 = n1[1:]
                self.refresh_value()
            else:
                n1 = n1.rjust(1 + len(n1), '-')
                self.refresh_value()
        elif n2 != '':
            if '-' in n2:
                n2 = n2[1:]
                self.refresh_value()
            else:
                n2 = n2.rjust(1 + len(n2), '-')
                self.refresh_value()

    #That function changes the comma for a period to transform the number in float
    def remove_comma(self, n):
        if ',' in str(n):
            n = str(n).replace(',','.')
            return n
        else: 
            return n
    
    #This function do the opposite, transforming the point into a comma
    def return_comma(self, n):
        if '.' in str(n):
            n = str(n).replace('.',',')
            return n
        else:
            return n

    #This function just format the number to remove undesirables periods or zeroes 
    def format_number(self, n):
        if float(n)%1==0:
            n = int(n)
        else:
            n = self.return_comma(n)
        n = str(n)
        return n

    #This function do the calcs depending on what operators is selected
    def result(self):
        global n1; global n2; global operator; global ans
        if n1 != '' and n2 != '' and operator != '':
            num1 = n1; num1 = float(self.remove_comma(num1))
            num2 = n2; num2 = float(self.remove_comma(num2))
        
            if operator == '+':
                n1 = num1 + num2
                n1 = self.format_number(n1)
                ans = True
                self.refresh_value()
            elif operator == '-':
                n1 = num1 - num2
                n1 = self.format_number(n1)
                ans = True
                self.refresh_value()
            elif operator == 'x':
                n1 = num1 * num2
                n1 = self.format_number(n1)
                ans = True
                self.refresh_value()
            elif operator == '/':
                n1 = num1 / num2
                n1 = self.format_number(n1)
                ans = True
                self.refresh_value()
            elif operator == '%':
                n1 = num1 % num2
                n1 = self.format_number(n1)
                ans = True
                self.refresh_value()
    
    #This function reset the program to the start, resetting all variables
    def clear(self):
        global n1; global n2; global operator; global ans; global comma2; global comma
        n1 = ''; n2 = ''; operator = ''; comma = False; comma2 = False; ans = False
        self.label_value.config(text='0')
    
    def delete(self):
        global n1; global n2; global operator; global comma; global comma2
        if n1 != '' and operator == '':
            if n1[len(n1)-1] == ',':
                comma = False
            n1 = n1[:-1]
            self.refresh_value()
        if n1 == '' and operator == '':
            self.label_value.config(text='0')
        if len(n1) == 1 and n1[0] == '-' and n2 == '' and operator == '':
            n1 = ''
            self.label_value.config(text='0')
        if n2 != '' and operator != '':
            if n2[len(n2)-1] == ',':
                comma2 = False
            n2 = n2[:-1]
            self.refresh_value()
        if n2 == '' and operator != '':
            self.label_value.config(text=n1+operator+'0')
        if len(n2) == 1 and n2[0] == '-':
            n2 = ''
            self.label_value.config(text=n1+operator+'0')
            

    #This function is responsible for updating the label that shows the numbers and operators
    def refresh_value(self):
        global n1; global n2; global operator; global ans; global comma2; global comma
        num1 = 0
        #Change the label values depending in which step the user is
        if ans:
            if n1 != '':
                num1 = float(self.remove_comma(n1))
            #Check if num1 has any decimal number if not, it transform it in int and let user put comma on the number
            if num1%1==0:
                comma = False
                num1 = int(num1)
            ans = False; n2 = ''; operator = ''; comma2 = False
            num1 = str(self.return_comma(num1))
            self.label_value.config(text=num1)
            if n1 == '0':
                n1 = ''
        elif n2 != '':
            self.label_value.config(text=n1+operator+n2)
        elif operator != '':
            self.label_value.config(text=n1+operator)
        else:
            self.label_value.config(text=n1)


    def __init__(self):
        window = Tk()
        window.title("Calculator")
        window.config(width="400", height="530")
        window.minsize(400,530)
        window.maxsize(400,530)
        
        #Creating Display Text
        self.label_value = Label(window, text='0', font=('', 32), justify='right', width='19')

        #Creating buttons
        button_zero = Button(window, text='0', justify='center', width='5', height='2', font=('', 18), command=lambda: self.numb(0))
        button_one = Button(window, text='1', justify='center', width='5', height='2', font=('', 18), command=lambda: self.numb(1))
        button_two = Button(window, text='2', justify='center', width='5', height='2', font=('', 18), command=lambda: self.numb(2))
        button_three = Button(window, text='3', justify='center', width='5', height='2', font=('', 18), command=lambda: self.numb(3))
        button_four = Button(window, text='4', justify='center', width='5', height='2', font=('', 18), command=lambda: self.numb(4))
        button_five = Button(window, text='5', justify='center', width='5', height='2', font=('', 18), command=lambda: self.numb(5))
        button_six = Button(window, text='6', justify='center', width='5', height='2', font=('', 18), command=lambda: self.numb(6))
        button_seven = Button(window, text='7', justify='center', width='5', height='2', font=('', 18), command=lambda: self.numb(7))
        button_eight = Button(window, text='8', justify='center', width='5', height='2', font=('', 18), command=lambda: self.numb(8))
        button_nine = Button(window, text='9', justify='center', width='5', height='2', font=('', 18), command=lambda: self.numb(9))
        
        #Creating Operations buttons
        button_negative = Button(window, text='-', justify='center', width='5', height='2', font=('', 18), command=lambda: self.minus_op())
        button_comma = Button(window, text=',', justify='center', width='5', height='2', font=('', 18), command=lambda: self.add_comma())
        button_equal = Button(window, text='=', justify='center', width='5', height='2', font=('', 18), command=lambda: self.result())
        button_addition = Button(window, text='+', justify='center', width='5', height='2', font=('', 18), command=lambda: self.operator('+'))
        button_subtraction = Button(window, text='_', justify='center', width='5', height='2', font=('', 18), command=lambda: self.operator('-'))
        button_multiply = Button(window, text='x', justify='center', width='5', height='2', font=('', 18), command=lambda: self.operator('x'))
        button_divide = Button(window, text='/', justify='center', width='5', height='2', font=('', 18), command=lambda: self.operator('/'))
        button_delete = Button(window, text='del', justify='center', width='5', height='2', font=('', 18), command=lambda: self.delete())
        button_clear = Button(window, text='C', justify='center', width='5', height='2', font=('', 18), command=lambda: self.clear())
        button_modulus = Button(window, text='%', justify='center', width='5', height='2', font=('', 18), command=lambda: self.operator('%'))

        
        #Positioning Label
        self.label_value.place(x=10, y=10)
        #Positioning buttons
        window.grid_anchor(SW)
        button_zero.grid(row=4, column=1, padx=10, pady=5)
        button_one.grid(row=3, column=0, padx=10, pady=5)
        button_two.grid(row=3, column=1, padx=10, pady=5)
        button_three.grid(row=3, column=2, padx=10, pady=5)
        button_four.grid(row=2, column=0, padx=10, pady=5)
        button_five.grid(row=2, column=1, padx=10, pady=5)
        button_six.grid(row=2, column=2, padx=10, pady=5)
        button_seven.grid(row=1, column=0, padx=10, pady=5)
        button_eight.grid(row=1, column=1, padx=10, pady=5)
        button_nine.grid(row=1, column=2, padx=10, pady=5)

        #Positioning Operators buttons
        button_negative.grid(row=4, column=0, padx=10, pady=5)
        button_comma.grid(row=4, column=2, padx=10, pady=5)
        button_equal.grid(row=4, column=3, padx=10, pady=5)
        button_addition.grid(row=3, column=3, padx=10, pady=5)
        button_subtraction.grid(row=2, column=3, padx=10, pady=5)
        button_multiply.grid(row=1, column=3, padx=10, pady=5)
        button_delete.grid(row=0, column=3, padx=10, pady=5)
        button_clear.grid(row=0, column=2, padx=10, pady=5)
        button_divide.grid(row=0, column=1, padx=10, pady=5)
        button_modulus.grid(row=0, column=0, padx=10, pady=5)

        window.mainloop()

Calculator()