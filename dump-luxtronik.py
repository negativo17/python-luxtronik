#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Simone Caronni <negativo17@gmail.com>
# Licensed under the GNU General Public License Version or later
#
# Based off:
# https://gist.githubusercontent.com/Bouni/cf0dc2c7c53c32deeb264803ec350e5c/raw/4ae9f92065bfc177e927c847e1583cc70929183a/dump-luxtronik.py

from luxtronik import Luxtronik

l = Luxtronik('192.168.1.12', 8889)

def cycle(title, param_array):
    print("="*104)
    print ('{:^104}'.format(title))
    print("="*104)
    print("No.".ljust(6, ' ') + "Name".ljust(50, ' ') + "Type".ljust(20, ' ') + "Value".ljust(18, ' '))
    for n, o in param_array():
        print(str(n).ljust(6, ' ') + o.name.ljust(50, ' ') + o.__class__.__name__.ljust(20, ' ') + str(o.value).ljust(18, ' '))

cycle('Parameters', l.parameters.parameters.items)
cycle('Calculations', l.calculations.calculations.items)
cycle('Visibilities', l.visibilities.visibilities.items)
