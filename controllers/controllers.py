# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class IdleControl(http.Controller):
    @http.route('/idle/get_all_alerts', auth='user', type='json')
    def all_alerts(self, **kw):
        alert_rec = http.request.env['idle_control.idle_control'].sudo().search([])
        alerts = []
        for rec in alert_rec:
            alerts.append({
                'action': rec.action,
                'date': rec.date,
                'area': rec.area,
                'photos': rec.photos,
            })

        return alerts

    @http.route('/idle/create_alert', auth='user', type='json')
    def create(self, **rec):
        if http.request.render:
            if rec['device']:
                vals = {
                    'device': rec['device'],
                    'date': rec['date'],
                    'duration': rec['duration'],
                }

                new_alert = request.env['idle_control.idle_control'].sudo().create(vals)
                for item in rec['photos']:
                    val_photos = {
                        'photo': item['photo'],
                        'time': item['time'],
                        'idle_id': new_alert.id,
                    }
                    request.env['photo_control.photo_control'].sudo().create(val_photos)
                args = {'success': True, 'message': 'Success', 'id': new_alert.id}
        return args

    @http.route('/idle/ping', type='json', auth='public')
    def ping(self):
        return {'success': True}
