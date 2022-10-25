def checkFunc(self, check_id,value):
        if self.env['test.model.lines'].search([('client_name','=',check_id)]):
            raise ValidationError(_("Этот пользователь уже существует"))
        else:
            self.env['test.model.lines'].create(value)   