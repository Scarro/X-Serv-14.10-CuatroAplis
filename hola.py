#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Sergio Carro Albarrán
SAT-ITT
"""


# Clase de la que van a heredar tanto hola como adios
# ya que tienen un funcionamiento similar
class repeat:

    def parse(self, request, rest):
        recurso = request.split()[1][1:]
        if recurso.startswith('hola'):
            self.app = 'holaApp'
        else:
            self.app = 'adiosApp'
        return recurso

    def process(self, parsedRequest):
        start = '<html><body>'
        end = '</body></html>'
        if self.app == 'holaApp':
            parsedRequest = "<h1>HOLA</h1>"
        else:
            parsedRequest = "<h1>ADIOS</h1>"
        appid = '<p>App id: ' + str(self.app) + '</p>'
        html = start + parsedRequest + appid + end
        return ('200 OK', html)


class hola(repeat):
    def __str__(self):
        return "holaApp"


class adios(repeat):
    def __str__(self):
        return "adiosApp"
