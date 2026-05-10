from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_ppn = fields.Boolean(string="With PPN", default=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New' or vals.get('name') == _('New'):
                seq_date = None
                if 'date_order' in vals:
                    seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))

                is_ppn = vals.get('is_ppn', False)
                if is_ppn:
                    vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order.ppn', sequence_date=seq_date) or '/'
                else:
                    vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order.non.ppn', sequence_date=seq_date) or '/'

        return super(PurchaseOrder, self).create(vals_list)
