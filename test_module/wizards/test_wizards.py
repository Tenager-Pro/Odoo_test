from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
class TestWizards(models.TransientModel):
    _name='test.wizards'
    _description = 'Test wizards'

    client_id = fields.Many2one(string='client', comodel_name='res.partner', required=True)

    def test_wizards(self):
        vals={
            'client_name': self.client_id.id
        }
        
        self.checkFunc(self.client_id.id,vals)
           
            
    def test_wizards_change(self):
        vals={
            'client_name': self.client_id.id
        }
        
        self.checkFunc(self.client_id.id,vals)
        

    def checkFunc(self, check_id,value):
        if self.env['test.model.lines'].search([('client_name','=',check_id)]):
            raise ValidationError(_("Этот пользователь уже существует"))
        else:
            self.env['test.model.lines'].create(value)
       
        
