import tkinter as tk
from tkinter import *
from forex_python.converter import CurrencyRates
OptionList1 = [
'USD',
'GBP',
'HKD',
'IDR',
'DKK' ,
'INR',
'CHF' ,
'MXN' ,
'CZK',
'SGD',
'THB',
'HRK',
'EUR',
'MYR',
'NOK',
'CNY' ,
'BGN' ,
'PHP',
'PLN' ,
'ZAR' ,
'CAD',
'ISK',
'BRL',
'RON',
'NZD',
'TRY' ,
'JPY' ,
'RUB',
'KRW' ,


]

OptionList2 = [
'IDR',
'GBP',
'HKD',
'DKK' ,
'INR',
'CHF' ,
'MXN' ,
'CZK',
'SGD',
'THB',
'HRK',
'EUR',
'MYR',
'NOK',
'CNY' ,
'BGN' ,
'PHP',
'PLN' ,
'ZAR' ,
'CAD',
'ISK',
'BRL',
'RON',
'NZD',
'TRY' ,
'JPY' ,
'RUB',
'KRW' ,
'USD',
]


def exChange():
    fro = variable.get()
    to = variable1.get()

    amount = float(e1.get())
    c = CurrencyRates()
    tot = c.convert(fro, to, amount)
    nsalText.set(tot)



root = tk.Tk()
root.geometry('500x450')
root.title("Currency Converter")

def cuurencyList():
    class Table:

        def __init__(self, root2):
            root2.title("Currency List")
            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root2, width=20, fg='green',
                                   font=('Sans serif', 10,'bold'))

                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])

                # take the data

    lst = [
           ('Currency Code', 'Currency', 'العملة'),
           ('USD', 'United States dollar', 'الدولار الأمريكي'),
           ('GBP', 'pound sterling', 'الجنيه الإسترليني'),
           ('HKD', 'Hong Kong dollar', 'دولار هونج'),
           ('IDR', 'Indonesian rupiah', 'روبية اندونيسية'),
           ('DKK', 'dansk krone', 'كرونة دنماركية'),
           ('INR', 'Indian Rupee', 'روبية هندية'),
           ('CHF', 'Confoederatio Helvetica Franc', 'فرنك سويسري'),
           ('MXN', 'Mexican', 'بيزو مكسيكي'),
           ('CZK', 'Czech koruna', 'كرونة تشيكية'),
           ('SGD', 'Singapore Dollar', 'دولار سنغافوري'),
           ('THB', 'Thai baht', 'بات تايلاندي '),
           ('HRK', 'Croatian Kuna', 'كونا كراوتية'),
           ('EUR', 'Euro', 'يورو'),
           ('MYR', 'Malaysia Ringgit', 'رينغيت ماليزي'),
           ('NOK', 'Norwegian Krone', 'الكرون النرويجي'),
           ('CNY', 'Chinese yuan', 'الرنمينبي'),
           ('BGN', 'Bulgarian Lev', 'الليف البلغاري'),
           ('PHP', 'Philippines Peso', 'البيزو الفلبيني'),
           ('PLN', 'Polish zloty', 'الزلوتي البولندي'),
           ('ZAR', 'South African rand', 'لراند الجنوب أفريقي'),
           ('CAD', 'Canadian dollar', 'الدولار الكندي'),
           ('ISK', 'Iceland Krona', 'الكرونا الأيسلندية'),
           ('BRL', 'BRAZIL REAL', 'الريال البرازيلي'),
           ('RON', 'Romania New Lei', 'الليو الروماني'),
           ('NZD', 'New Zealand Dollar', 'الدولار النيوزيلاندي'),
           ('TRY', 'Turkish lira', 'الليرة التركي'),
           ('JPY', 'yen', 'الين الياباني'),
           ('RUB', 'Russian ruble', 'الروبل الروسي'),
           ('KRW', 'South Korea Won', 'الون الكوري الجنوبي'),


           ]

    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    root2 = Tk()
    t = Table(root2)
#end of table currency list



tk.Label(root, text="This App Convert Currency",fg='Purple', font=('Sans serif', 14)).place(x=10, y=10)
tk.Button(root, text="Currency list", command=cuurencyList, height=2, width=11, font=('Sans serif', 10), fg='blue').place(x=380, y=10)

variable = tk.StringVar(root)
variable.set(OptionList1[0])

opt = tk.OptionMenu(root, variable, *OptionList1)
opt.config(width=6, font=('Sans serif', 16))
opt.pack(side="top")



variable1 = tk.StringVar(root)
variable1.set(OptionList2[0])

opt2 = tk.OptionMenu(root, variable1, *OptionList2)
opt2.config(width=6, font=('Sans serif', 16))
opt2.pack(side="top")

global e1
global nsalText
nsalText = tk.StringVar()
labelTest = tk.Label(text="", font=('Sans serif', 16))
labelTest.pack(side="top")



tk.Label(root, text="From", fg= 'green', font=('Sans serif', 16)).place(x=10, y=70)
tk.Label(root, text="To", fg= 'green', font=('Sans serif', 16)).place(x=10, y=120)
tk.Label(root, text="Amount",fg= 'green', font=('Sans serif', 16)).place(x=10, y=170)

tk.Label(root, text="Total:", font=('Sans serif', 16), fg='blue').place(x=10, y=325)
tk.Label(root, text="", font=('Sans serif', 22), fg='red', textvariable=nsalText).place(x=100, y=320)
tk.Button(root, text="Convert", command=exChange, height=2, width=7, font=('Sans serif', 14), fg='red').place(x=200, y=220)

e1 = tk.Entry(root)
opt.place(x=120, y=60)
opt2.place(x=120, y=120)
e1.place(x=120, y=180)


root.mainloop()