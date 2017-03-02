#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
Sergio Carro Albarrán
SAT GITT
"""

import random

class aleatorias:
    
    def parse(self, request, rest):
        return rest

    def process(self, parsedRequest):
        link = str(random.randrange(1000000000))
        cabecera = "200 OK";
        html = '<html><body><h1>' + str(parsedRequest)
        html += '</h1><a href="' + link + '">Dame dirección aleatoria'
        html += '</a></body></html>'
        return (cabecera, html)