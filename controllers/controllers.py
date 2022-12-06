# -*- coding: utf-8 -*-
# from odoo import http


# class StaffControl(http.Controller):
#     @http.route('/staff_control/staff_control', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/staff_control/staff_control/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('staff_control.listing', {
#             'root': '/staff_control/staff_control',
#             'objects': http.request.env['staff_control.staff_control'].search([]),
#         })

#     @http.route('/staff_control/staff_control/objects/<model("staff_control.staff_control"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('staff_control.object', {
#             'object': obj
#         })
