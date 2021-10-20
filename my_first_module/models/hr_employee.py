# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = 'HR employee inherit base'

    pin_code = fields.Char('Pin Code')
    password = fields.Char('Password')

