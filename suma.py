#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
Sergio Carro Albarrán
SAT GITT
"""


class suma:

    sumando1 = None

    def parse(self, request, rest):
        return rest

    def process(self, parsedRequest):
        start = '<html><body><h1>Suma:</h1>'
        end = '</body></html>'
        page = ''
        try:
            parsedRequest = int(parsedRequest)
            if self.sumando1 is None:
                self.sumando1 = parsedRequest
                page = '<p>Primer número: ' + str(parsedRequest)
                page += '</br>Introduce el segundo</p>'
            else:
                suma = self.sumando1 + parsedRequest
                page += '<p>Primer número: ' + str(self.sumando1)
                page += '</br>Segundo número: ' + str(parsedRequest)
                page += '</br><em>Suma:</em> ' + str(suma) + '</p>'
                self.sumando1 = None
            cabecera = "200 OK"
        except ValueError:
            cabecera = "400 Bad Request"
            page += '<p>Introduce un número correcto</p>'
        page += '<p>App id: ' + str(self) + '</p>'
        html = start + page + end
        return (cabecera, html)

    def __str__(self):
        return "suma app"
