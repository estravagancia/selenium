# https://www.youtube.com/watch?v=wbfcuoKzHgc
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import requests
from lxml import html
from decimal import *

h = {
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
}

url = 'https://www.xe.com/en/currencyconverter/convert/?Amount=1&From=USD&To=EUR'

page = requests.get(url,headers=h)
print(page.status_code)

tree = html.fromstring(page.content)
# print(tree)

# añadimos /text() para obtener el texto
p = tree.xpath('/html/body/div[1]/div[2]/div[2]/section/div[2]/div/main/form/div[2]/div[3]/div[1]/div[1]/p/text()')
print(p)

# t = tree.xpath('/html/body/div[1]/div[2]/div[3]/section/div/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/text()')
# print(t)


dolar = p[0].split(' ')
valor = dolar[3]
print(valor)

valor = valor.replace(',','.')
print(valor)

getcontext().prec = 4
# print(getcontext())
# moneda = Decimal(valor)
# print(moneda)
# dinero = input('cuantos $$ son estos €€ : ')
# dinero = dinero.replace(',','.')
# dinero = 1000
# print('$' + str(Decimal(float(valor)) * Decimal(float(dinero))))

actualizado = tree.xpath('/html/body/div[1]/div[2]/div[2]/section/div[2]/div/main/form/div[2]/div[3]/div[2]/div/text()')
# print(actualizado[4])

cuando = actualizado[4].split(',')
# print(cuando)
print(cuando[0])




def moneyfmt(value, places=2, curr='', sep=',', dp='.',
             pos='', neg='-', trailneg=''):
    """Convert Decimal to a money formatted string.

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank

    >>> d = Decimal('-1234567.8901')
    >>> moneyfmt(d, curr='$')
    '-$1,234,567.89'
    >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
    '1.234.568-'
    >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
    '($1,234,567.89)'
    >>> moneyfmt(Decimal(123456789), sep=' ')
    '123 456 789.00'
    >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
    '<0.02>'

    """
    q = Decimal(10) ** -places      # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = list(map(str, digits))
    build, next = result.append, digits.pop
    if sign:
        build(trailneg)
    for i in range(places):
        build(next() if digits else '0')
    if places:
        build(dp)
    if not digits:
        build('0')
    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return ''.join(reversed(result))