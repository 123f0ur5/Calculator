from tkinter import N, SW, Button, Label, Tk

n1 = ''; n2 = ''; operator = ''; comma = False; comma2 = False; res = False

class Calculator:
    def numb(self, n):
        global n1; global n2; global operator
        if operator == '':
            n1 += str(n)
            self.refresh_value()
        else:
            n2 += str(n)
            self.refresh_value()

    def operator(self, op):
        global operator; global n2
        if n2 == '':
            operator = op
            self.refresh_value()
    
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

    def remove_comma(self, n):
        print(n)
        if ',' in str(n):
            n = str(n).replace(',','.')
            return n
        else: 
            return n
    
    def return_comma(self, n):
        print(n)
        if '.' in str(n):
            n = str(n).replace('.',',')
            return n
        else:
            return n

    def result(self):
        global n1; global n2; global operator; global res
        if n1 != '' and n2 != '' and operator != '':
            num1 = n1; num1 = float(self.remove_comma(num1))
            num2 = n2; num2 = float(self.remove_comma(num2))
        
            if operator == '+':
                n1 = num1 + num2
                n1 = str(n1)
                res = True
                self.refresh_value()
            elif operator == '-':
                n1 = num1 - num2
                n1 = str(n1)
                res = True
                self.refresh_value()
            elif operator == '*':
                n1 = num1 * num2
                n1 = str(n1)
                res = True
                self.refresh_value()
            elif operator == '/':
                n1 = num1 / num2
                n1 = str(n1)
                res = True
                self.refresh_value()
            elif operator == '%':
                n1 = num1 % num2
                n1 = str(n1)
                res = True
                self.refresh_value()
    
    def print_value(self, n, **kwargs):
        print(kwargs.get('op'))
        if kwargs.get('op') != None:
            n = self.remove_comma(n)
            self.label_value.config(text='{}{}{}'.format(n, kwargs.get('op'), kwargs.get('n_two')))
        else:
                if n%1==0:
                    print('entrei sem decimal')
                    self.label_value.config(text='{:.0f}'.format(n))
                elif n%1!=0:
                    print('entrei com decimal')
                    n = self.return_comma(n)
                    self.label_value.config(text='{}'.format(n))

    def refresh_value(self):
        global operator; global n1; global n2; global res; global comma; global comma2
        if res:
            self.print_value(float(n1))
            operator = ''; n2 = ''; res = False; comma2 = False
            if ',' in n1:
                comma = True
            else:
                comma = False
        elif operator == '':
            self.print_value(float(n1))
        else:
            self.print_value(float(n1), op = operator, n_two = n2)


    def __init__(self):
        window = Tk()
        window.title("Calculator")
        window.config(width="400", height="530")
        window.minsize(400,530)
        window.maxsize(400,530)
        
        #Creating Display Text
        self.label_value = Label(window, text='0', font=('', 40), justify='right', width='19')

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
        button_multiply = Button(window, text='x', justify='center', width='5', height='2', font=('', 18), command=lambda: self.operator('*'))
        button_divide = Button(window, text='/', justify='center', width='5', height='2', font=('', 18), command=lambda: self.operator('/'))
        button_delete = Button(window, text='del', justify='center', width='5', height='2', font=('', 18))
        button_clear = Button(window, text='C', justify='center', width='5', height='2', font=('', 18))
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

c1 = Calculator()