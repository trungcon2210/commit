# -*- coding: utf-8 -*-

import ast
import logging
import re
from collections import namedtuple
from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.osv import expression
import odoo

_logger = logging.getLogger(__name__)


class CarCar(models.Model):
    _name = 'car.car'

    employee_id = fields.Many2one('hr.employee', 'Employee', required=True, compute='_compute_employee')
    name = fields.Char('Name')
    horse_power = fields.Integer('Horse Power')
    door_number = fields.Integer('Door Number')
    driver_id = fields.Many2one('res.partner')
    parking_id = fields.Many2one('parking.parking', 'Parking ID')
    feature_ids = fields.Many2one('car.feature')
    total_speed = fields.Integer('Total Speed', _compute="_total_speed", store=True, readonly=True)
    status = fields.Selection([
        ('new', 'New'),
        ('used', 'Used'),
        ('sold', 'Sold'),
    ], string="Status", default='new')
    car_sequence = fields.Char('Sequence')
    image = fields.Binary('Image')
    car_price = fields.Float('Price')
    last_check = fields.Datetime('Date current action', required=False, readonly=False)

    name_sequence = fields.Char(string="Service Number", readonly=True, required=True, copy=False, default='New')

    @api.depends('employee_id')
    def _compute_employee(self):
        for r in self:
            r.employee_id = r.employee_id.employee_id.id

    @api.depends('horse_power')
    def _total_speed(self):
        if self.horse_power:
            self.total_speed = self.horse_power * 5

    @api.model
    def create(self, vals):
        if vals.get('name_sequence', 'New') == 'New':
            vals['name_sequence'] = self.env['ir.sequence'].next_by_code(
                'my_first_module.my_car.sequence') or 'New'
        result = super(CarCar, self).create(vals)
        return result

    def my_method(self, a, k=None):
        _logger.info('executed with a: %s and k: %s', a, k)
        list_record_car = self.env['car.car'].search([])
        for r in list_record_car:
            r.update({
                'last_check': datetime.now()
            })

    def export_partner(self):
        self.env['car.car'].with_delay().my_method('a', k=2)
