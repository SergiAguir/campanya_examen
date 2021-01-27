# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime
from odoo.exceptions import ValidationError

class campanya_model(models.Model):
    _name = 'cooperativa.campanya_model'
    _description = 'Modelo de campanya'

    campanya= fields.Date(string="Campanya",default=datetime.year,help="Campanya")
    fecha= fields.Date(string="Fecha",default=datetime.today(),help="Fecha de la campanya")
    socio= fields.Many2one("cooperativa.socios_model", string="Socio")
    producto= fields.Many2one("cooperativa.productos_model",string="Producto")
    cantidad= fields.Float(string="Cantidad",default=0,help="Cantidad")

    @api.constrains("cantidad")
    def _comprobarCant(self):
        if self.cantidad<0:
            raise ValidationError("La cantidad tiene que ser mayor que 0")