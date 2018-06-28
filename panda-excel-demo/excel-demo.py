#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import pandas as pd


def work_sheets(xls):
    return xls.sheet_names


def main(sheet):
    with pd.ExcelFile(sheet) as xls:
        # ws = work_sheets(xls)
        # [print(x) for x in ws]
        orders = xls.parse('SalesOrders')
        orders['My_total'] = orders['Units'] * orders['Unit Cost']
        orders['My_equal'] = orders['Total'] == orders['My_total']
        [print(orders.loc[idx]) for idx, x in enumerate(orders['My_equal']) if not x]

        # print(orders)

        # mo = pd.melt(orders)
        # print(mo)
        # [print(x) for x in mo['variable'] ]
        # print(orders["Units"][0])
        # print(type(orders))
        # print(orders)
        # data = orders.values
        # print(list(data))


if __name__ == '__main__':
    main("SampleData.xlsx")
