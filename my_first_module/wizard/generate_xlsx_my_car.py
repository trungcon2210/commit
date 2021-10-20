# -*- coding: utf-8 -*-

from odoo import models, fields, api
import xlwt
from xlsxwriter.workbook import Workbook
import base64


class GenerateMyCar(models.TransientModel):
    _name = "generate.my.car"
    _description = "Generate My Car"

    max_horse_power = fields.Integer('Max Horse')

    def generate_my_car(self):
        list_record_car = self.env['car.car'].search([])
        for r in list_record_car:
            if r.horse_power <= self.max_horse_power:
                return self.env.ref('my_first_module.patient_xlsx').report_action(list_record_car)

