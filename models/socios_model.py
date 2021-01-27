# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime
from odoo.exceptions import ValidationError

class socios_model(models.Model):
    _name = 'cooperativa.socios_model'
    _description = 'Modelo de socios'
    _sql_constraints = [('id_socio_uniq','UNIQUE (id_socio)','No puede haber dos socios con el mismo identificador'),
    ('dni_uniq','UNIQUE (dni)','No puede haber dos socios con el mismo dni'),]

    id_socio= fields.Integer(string="Id Socios",required=True,help="Id de los Socios")
    foto= fields.Binary()
    name= fields.Char(string="Nombre",required=True,help="Nombre del socio")
    apellidos= fields.Char(string="Apellidos",required=True,help="Apellidos del socio")
    dni= fields.Char(string="DNI",required=True,help="DNI del socio")
    fecha= fields.Date(string="Fecha",required=True,default=date.today(),help="Fecha")
    telf= fields.Integer(string="Telefono",required=True,size=9,help="Telefono del socio")
    email= fields.Char(string="Email",help="Email del socio")
    saldo= fields.Float(string="Saldo",readonly=True,default=0)
    socio_id= fields.Many2one("cooperativa.campanya_model","socio")
    #rpendientes= fields.One2many("cooperativa.campany_model","registros_id",string="Registros Pendientes")

    @api.constrains("dni")
    def _comprobarDNI(self):
        if len(self.dni)!=9:
            raise ValidationError("El DNI debe tener 9 caracteres")
        else:
            try:
                n=int(self.dni[:-1])
            except ValueError:
                raise ValidationError("Los primeros 8 dígitos deben ser números")

            palabra='TRWAGMYFPDXBNJZSQVHLCKE'

            if self.dni[-1].upper() == palabra[n%23]:
                return True
            else:
                
                raise ValidationError("La letra no coincide con el DNI")

    @api.constrains("telf")
    def _comprobarTelf(self):
        if self.telf <99999999:
            raise ValidationError("El telefono tiene que contener 9 numeros")


    @api.constrains("email")
    def _comprobarEmail(self):
        if len(self.email)>5:
            if "@" not in self.email:
                raise ValidationError("El email tiene que contener una @")
        else:
            raise ValidationError("El email tiene que tener mas de 5 caracteres")

    