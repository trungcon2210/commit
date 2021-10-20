# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CarFeature(models.Model):
    _name = 'car.feature'

    name = fields.Char('Name')