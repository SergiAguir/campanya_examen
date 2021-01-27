# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class productos_model(models.Model):
    _name = 'cooperativa.productos_model'
    _description = 'Modelo de productos'
    _sql_constraints= _sql_constraints = [('name_uniq','UNIQUE (name)','No puede haber dos productos iguales'),]
    
    name= fields.Char(string="Nombre",required=True,help="Nombre del producto")
    descripcion= fields.Char(string="Descripcion",required=True,help="Descripcion del producto")
    precio= fields.Float(string="Precio",required=True,help="Precio del producto")
    ktotales= fields.Float(string="Kilos totales",default=0,readonly=True,help="Kilos totales")
    producto_id= fields.One2many("cooperativa.campanya_model","producto")

    @api.constrains("precio")
    def _calcPrecio(self):
        if self.precio < 0:
            raise ValidationError("El precio no puede ser menor que 0")