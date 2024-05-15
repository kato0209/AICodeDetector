
        return {
            'name': 'Security Context',
            'code':'security',
            'context_type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
           'res_model':'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
  