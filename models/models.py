# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import UserError

class ReparacionCompras(models.Model):
    _inherit = 'mrp.repair'

    @api.multi
    def action_validate(self):
        now = datetime.now()
        producto_proveedor =0

        context = self._context
        current_uid = context.get('uid')
        user = self.env['res.users'].browse(current_uid)
        for i in self.operations:
            if i.product_id.product_tmpl_id.seller_ids.name.id:
                for s in i.product_id.product_tmpl_id.seller_ids:
                    producto_proveedor = s.name.id
        if producto_proveedor==False:
            raise UserError(u'No se ha establecido un proveedor en la ficha del producto')
        new_rec = self.env['purchase.order'].create({
            'partner_id': producto_proveedor,
            'date_order': now,
            'state': 'draft',
            'create_uid': user.id,
            'create_date': now,
            'write_uid': user.id,
            'write_date': now,
            'origin':self.name,
        })

        order_id=self.env['purchase.order'].search([('origin','=',self.name)],limit=1).id

        for i in self.operations:
            producto_proveedor = i.product_id.product_tmpl_id.seller_ids.name.id
            precio_compra=i.product_id.product_tmpl_id.seller_ids.price
            new_rec_lineas=self.env['purchase.order.line'].create({
                    'product_id': i.product_id.id,  # many2one must be an integer value
                    'Description':i.name,
                    'name': i.name,
                    'product_qty':i.product_uom_qty,
                    'price_unit': precio_compra,
                    'create_uid':user.id,
                    'create_date': now,
                    'write_uid':user.id,
                    'write_date':now,
                    'date_planned':now,
                    'product_uom':i.product_uom.id,
                    'order_id':order_id,
            })
        return super(ReparacionCompras, self).action_validate()


