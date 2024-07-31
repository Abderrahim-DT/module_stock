# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleStage(http.Controller):
#     @http.route('/module_stage/module_stage', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_stage/module_stage/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_stage.listing', {
#             'root': '/module_stage/module_stage',
#             'objects': http.request.env['module_stage.module_stage'].search([]),
#         })

#     @http.route('/module_stage/module_stage/objects/<model("module_stage.module_stage"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_stage.object', {
#             'object': obj
#         })

