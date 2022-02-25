#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 13:41:30 2022

@author: ankurpriyadarshi
"""

import sys


def count_words(file_name):
    wdcountresults = {}
    with open(file_name) as file:
        texts = file.read().replace("\n", '')
    for ws in texts.split(" "):
        if ws.lower() in wdcountresults:
            wdcountresults[ws.lower()] = wdcountresults[ws.lower()] + 1
        else:
            wdcountresults[ws.lower()] = 1
    results = dict(sorted(wdcountresults.items(), key=lambda item: item[1]))
    print(results)
 
def main():
   flname = sys.argv[1]
   count_words(flname)
if __name__== "__main__":
   main()
