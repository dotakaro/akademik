# -*- coding: utf-8 -*-
from odoo import http

# class Akademik(http.Controller):
#     @http.route('/akademik/akademik/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/akademik/akademik/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('akademik.listing', {
#             'root': '/akademik/akademik',
#             'objects': http.request.env['akademik.akademik'].search([]),
#         })

#     @http.route('/akademik/akademik/objects/<model("akademik.akademik"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('akademik.object', {
#             'object': obj
#         })