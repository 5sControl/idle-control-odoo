# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StaffControl(models.Model):
    _name = 'staff_control.staff_control'
    _rec_name = 'action'

    action = fields.Char()
    date = fields.Char()
    area = fields.Char()
    photo = fields.Binary(
        string="Image",
        compute="_compute_image",
        store=True,
        attachment=False
    )

    @api.model
    def create(self, vals):
        vals['photo'] = vals['photo'].split(',')[1]
        return super(StaffControl, self).create(vals)
