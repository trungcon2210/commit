from odoo import api, fields, models
from datetime import datetime
import os


class TestCronJob(models.Model):
    _name = 'cron.job'

    @api.model
    def update_last_check(self):
        list_record_car = self.env['car.car'].search([])
        for r in list_record_car:
            r.update({
                'last_check': datetime.now()
            })
