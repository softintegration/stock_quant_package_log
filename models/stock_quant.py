# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class QuantPackage(models.Model):
    """ Inherit stock package to add product dimensions to the package """
    _name = "stock.quant.package"
    _inherit = ['stock.quant.package','mail.thread', 'mail.activity.mixin']





