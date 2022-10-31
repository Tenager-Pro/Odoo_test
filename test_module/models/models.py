
from odoo import api, models, fields

class TestModels(models.Model):
    _name = 'test.models'
    _description = 'Test models'

    test_name = fields.Char(string = 'Name', required=True)

    test_age = fields.Integer(string='Age')

    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
    ], required=True, default='male',string='Gender')

    notes = fields.Text(string='Notes')

    one=fields.Boolean(string='One')

    two=fields.Boolean(string='Two')

    bool_all=fields.Boolean(string='All')

    create_name = fields.Many2one(comodel_name='res.users', default=lambda self: self.env.uid, required=True) 

    image = fields.Binary(string='Image')

    responsible=fields.Many2one(comodel_name='res.users', default=lambda self: self.env.uid)
    
    clients=fields.One2many(comodel_name='test.model.lines', inverse_name='test')
    
    @api.onchange('bool_all')
    def onchange_bool_all(self):
        values = {}
        if self.bool_all:
            values['one'] = self.bool_all
            values['two'] = self.bool_all
        if ((self.bool_all==False) and (self.one==True) and (self.two==True)):
            values['one'] = self.bool_all
            values['two'] = self.bool_all
        if ((self.bool_all==False) and (self.one==False) and (self.two==True)):
            values['one'] = self.bool_all
            values['two'] = True
        if ((self.bool_all==False) and (self.one==True) and (self.two==False)):
            values['one'] = True
            values['two'] = self.bool_all
        self.update(values)

    @api.onchange('two','one')
    def onchange_bool_two(self):
        values = {}
        if ((self.one==True) and (self.two==True)):
            values['bool_all'] = True
        if ((self.one==False) or (self.two==False)):
            values['bool_all'] = False   
        self.update(values)
    def create_wizard(self):
        return{
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'test.wizards',
            'target': 'new',
            'type': 'ir.actions.act_window',
            'context': {'test_models_id': self.id}
        } 
    
 






