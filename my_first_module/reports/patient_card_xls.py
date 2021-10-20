# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
import xlwt
from xlsxwriter.workbook import Workbook
import base64


class PatientCardXLS(models.AbstractModel):
    _name = 'report.patient.excel'
    _description = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('Patient Card')
        sheet.set_column(3, 3, 50)
        sheet.set_column(2, 2, 30)
        sheet.write(2, 2, 'name', format1)
        sheet.write(2, 3, Lines.patient_name, format2)
        sheet.write(3, 2, 'Horse', format1)
        sheet.write(3, 3, Lines.patient_horse_power, format2)


