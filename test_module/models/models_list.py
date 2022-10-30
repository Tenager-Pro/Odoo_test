from odoo import api, models, fields
#Класс посредник между test.models и res.partner
class TestModelLines(models.Model):
    _name = 'test.model.lines'
    _description = 'Test models line'
    
    client_name = fields.Many2one(string='client name', comodel_name='res.partner')
    email = fields.Char(string='Email', related ="client_name.email") 
    test = fields.Many2one(comodel_name='test.models')