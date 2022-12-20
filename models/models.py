# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IdleControl(models.Model):
    _name = 'idle_control.idle_control'
    _rec_name = 'action'

    action = fields.Char()
    date = fields.Char()
    area = fields.Char()
    # photos = fields.One2many('photo_control.photo_control', 'idle_id', string='Photo')


class ImageControl(models.Model):
    _name = 'photo_control.photo_control'

    idle_id = fields.Many2one('idle_control.idle_control')
    time = fields.Char()
    photo = fields.Binary(
        string="Image",
        compute="_compute_image",
        store=True,
        attachment=False
    )

    @api.model
    def create(self, vals):
        vals['photo'] = vals['photo'].split(',')[1]
        return super(ImageControl, self).create(vals)
