from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
class TestWizards(models.TransientModel):
    _name='test.wizards'
    _description = 'Test wizards'

    partner_name = fields.Char(string='client', required=True)
    #  Функция добавить и создать 
    def test_wizards(self):
        vals={
            'name': self.partner_name
        }
       
        self.check_func(vals)#Передает в функцию проверки 
      
         
    #Функция добавить и изменить         
    def test_wizards_change(self):
        vals={
            'name': self.partner_name
        }
        record_set_partner = self.check_func(vals) #возвращат объект
        return{
            'name': _('Change'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model':'res.partner',
            'res_id': record_set_partner.id, #id user
            'target': 'new',
        } 
       
    @api.model
    def check_func(self, value):
        
        if self.env['res.partner'].search([('name','=',value['name'])]):
            raise ValidationError(_("Этот пользователь уже существует"))
        else:
            check_id=self.env['res.partner'].create(value)
            id_test_models_lines=self.env['test.model.lines'].create({'client_name':check_id.id})
            res = self.env['test.models'].browse(self._context['test_models_id']) 
            res.write({'clients':[(4,id_test_models_lines.id,0)]}) # you need to add it as list
       
        return check_id
       
        
