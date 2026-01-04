# -*- coding: utf-8 -*-
# from odoo import http


# class RsBase(http.Controller):
#     @http.route('/rs_base/rs_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rs_base/rs_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rs_base.listing', {
#             'root': '/rs_base/rs_base',
#             'objects': http.request.env['rs_base.rs_base'].search([]),
#         })

#     @http.route('/rs_base/rs_base/objects/<model("rs_base.rs_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rs_base.object', {
#             'object': obj
#         })
