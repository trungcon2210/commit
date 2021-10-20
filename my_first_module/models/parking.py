# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Parking_Parking(models.Model):
    _name = 'parking.parking'

    name = fields.Char('Name')
    car_ids = fields.One2many('car.car','parking_id',"Car ID")
    parking_price = fields.Float('Price Parking')
