# -*- coding: utf-8 -*-
# Part of AppJetty. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProductCategory(models.Model):
    _inherit = 'product.public.category'

    include_in_megamenu = fields.Boolean(
        string="Include in mega menu", help="Include in mega menu")
    menu_id = fields.Many2one('website.menu', string="Main menu")
    description = fields.Text(string="Description",
        help="Short description which will be visible below category slider.")



    
    