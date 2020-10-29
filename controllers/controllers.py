# -*- coding: utf-8 -*-
from odoo import http

# class Extra-addons/methodRepairPurchase(http.Controller):
#     @http.route('/extra-addons/method_repair_purchase/extra-addons/method_repair_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra-addons/method_repair_purchase/extra-addons/method_repair_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-addons/method_repair_purchase.listing', {
#             'root': '/extra-addons/method_repair_purchase/extra-addons/method_repair_purchase',
#             'objects': http.request.env['extra-addons/method_repair_purchase.extra-addons/method_repair_purchase'].search([]),
#         })

#     @http.route('/extra-addons/method_repair_purchase/extra-addons/method_repair_purchase/objects/<model("extra-addons/method_repair_purchase.extra-addons/method_repair_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-addons/method_repair_purchase.object', {
#             'object': obj
#         })