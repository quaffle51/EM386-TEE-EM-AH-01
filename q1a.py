\begin{pycode}
import isbnlib
import latextable
import texttable as tt
import re


def vertical(isbn_like):
    # isbn_like = '0303392611'

    index = 1
    rows = [['$i$', '$x_i$', '$ix_i$']]
    sum = 0
    for digit in isbn_like:
        if digit == 'X':
            digit = 10
            sum += index * 10
        else:
            sum += index * int(digit)
        rows.append([index, digit, index * int(digit)])
        index += 1
        if index == len(isbn_like):
            break

    x_10 = sum % 11

    table = tt.Texttable()
    table.set_cols_align(["r", "c", "r"])
    table.set_cols_valign(["m", "m", "m"])
    table.add_rows(rows)

    mytable = latextable.draw_latex(table,
                                    caption="$\sum_{{i=1}}^9 ix_i = {0} \\textrm{{ and }} x_{{10}} \equiv {0} \Mod{{11}} \equiv {1}$.".format(
                                        sum, x_10))
    m = re.sub(r'(^\\begin+\{table\})([a-zA-Z0-9$_\\\W]+)', r'\1[h!]\2', mytable)
    v = is_valid(isbn_like, x_10)
    return m, v


def horizontal(isbn_like):
    """

    :type isbn_like: str
    """
    # isbn_like = '0303392611'

    index = 1
    top_row = ['$i$']
    mid_row = ['$x_i$']
    bot_row = ['$ix_i$']
    for i in range(9):
        top_row.append("${}$".format(i + 1))
        mid_row.append("${}$".format(isbn_like[i]))
    sum = 0
    for digit in isbn_like:
        if digit == 'X':
            digit = 10
            sum += index * 10
        else:
            sum += index * int(digit)
        bot_row.append(index * int(digit))
        index += 1
        if index == len(isbn_like):
            break

    x_10 = sum % 11
    rows = [top_row, mid_row, bot_row]
    table = tt.Texttable()
    table.set_cols_align(['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'])
    table.set_cols_valign(['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm'])
    table.add_rows(rows)

    mytable = latextable.draw_latex(table, caption="$\sum_{{i=1}}^9 ix_i = {0} \\textrm{{ and }} x_{{10}} \\equiv {0} \Mod{{11}} \equiv {1}$.".format( sum, x_10))
    m = re.sub(r'(^\\begin+\{table\})([a-zA-Z0-9$_\\\W]+)', r'\1[h!]\2', mytable)
    v = is_valid(isbn_like, x_10)
    return m, v


def is_valid(isbn_like, x_10):
    
    valid   = r'ISBN-10 {} is valid as the calculated value of $x_{{10}}={}$ is equal to the given value of $x_{{10}} =  {}$.'.format(isbn_like, x_10, isbn_like[-1])
    invalid = r"ISBN-10 {} is invalid as the calculated value of $x_{{10}}={}$ is not equal to given value of $x_{{10}} = {}$.".format(isbn_like, x_10, isbn_like[-1])
    if isbnlib.is_isbn10(isbn_like):
        return valid
    else:
        return invalid


isbn1 = '0303392611'
isbn2 = '0099417561'
isbn3 = '1584885086'
isbn4 = '3003392611'
isbn5 = '1584885068'
isbn6 = '048627263X'

isbn_i =   '297?2357099'
isbn_ii =  '2159?7?3011'
isbn_iii = '42??325?897'


isbn_like_1, valid_1 = horizontal(isbn1)
isbn_like_2, valid_2 = horizontal(isbn2)
isbn_like_3, valid_3 = horizontal(isbn3)
isbn_like_4, valid_4 = horizontal(isbn4)
isbn_like_5, valid_5 = horizontal(isbn5)
isbn_like_6, valid_6 = horizontal(isbn6)
\end{pycode}
