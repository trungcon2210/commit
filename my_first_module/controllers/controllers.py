# -*- coding: utf-8 -*-
from odoo import http
import json


class MyFirstModule(http.Controller):
    @http.route('/my_first_module/my_first_module/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/get_my_car', type='json', method=['GET'], auth='public')
    def get_my_car(self, **kwargs):
        search_ids = http.request.env["car.car"].search([], limit=1,  order='horse_power desc')
        max_horse_power = search_ids.horse_power
        list_record_max_horse = http.request.env["car.car"].search([('horse_power', '=', max_horse_power)])
        list_record = []
        for r in list_record_max_horse:
            vals = {
                'id': r.id,
                'name': r.name,
                'horse_power': r.horse_power,
                'door_number': r.door_number,
                'total': r.total_speed,
                'status': r.status,
                'driver': r.driver_id.id,
                'parking': r.parking_id.id,
                'feature': r.feature_ids.id,
            }
            list_record.append(vals)
        print("List Car")
        data = json.dumps(list_record, indent=2)
        return data
