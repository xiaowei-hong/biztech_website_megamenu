# -*- coding: utf-8 -*-
# Part of AppJetty. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.http import request


class WebsiteMenu(models.Model):
    _inherit = "website.menu"

    is_megamenu = fields.Boolean(string='Is megamenu...?')
    megamenu_type = fields.Selection([('2_col', '2 Columns'),
                                      ('3_col', '3 Columns'),
                                      ('4_col', '4 Columns')],
                                     default='3_col',
                                     string="Megamenu type")

    megamenu_bg = fields.Boolean(string='Want to set megamenu background', default=False)
    megamenu_bg_img_color = fields.Selection([('bg_img', 'Background image'),
                                              ('bg_color', 'Background color')],
                                              default='bg_img',
                                              string="Megamenu background selection")
    megamenu_bg_image = fields.Binary(string="Background image for megamenu")
    megamenu_bg_color = fields.Char(string="Background color for megamenu",
                                    default='#ccc',
                                    help="Background color for megamenu, for setting background color you have to pass hexacode here.")

    category_slider = fields.Boolean(string='Want to display category slider', default=False)
    carousel_header_name = fields.Char(string="Slider label",
                                       default="Latest",
                                       help="Header name for carousel slider in megamenu")
    category_slider_position = fields.Selection([('left', 'Left'), ('right', 'Right')],
        default='left', string="Category Slider Position")

    menu_icon = fields.Boolean(string='Want to display menu icon', default=False)
    menu_icon_image = fields.Binary(string="Menu Icon", help="Menu icon for your menu")

    display_menu_footer = fields.Boolean(string="Display menu footer", default=False,
        help="For displaying footer in megamenu")
    menu_footer = fields.Html(string="Footer content",
                              help="Footer name for megamenu")


    customize_menu_colors = fields.Boolean(string='Want to customize menu colors', default=False)
    main_category_color = fields.Char(string='Main category color',
        help="Set color for main category in megamenu")
    sub_category_color = fields.Char(string='Sub category color',
        help="Set color for sab category in megamenu")


class Website(models.Model):
    _inherit = 'website'

    @api.multi
    def get_public_product_category(self, submenu):
        categories = self.env['product.public.category'].search([('parent_id', '=', False),
                                                                 ('include_in_megamenu', '!=',False),
                                                                 ('menu_id', '=', submenu.id)],
                                                                 order="sequence")
        return categories
