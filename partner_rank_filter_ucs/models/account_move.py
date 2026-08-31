# -*- coding: utf-8 -*-
from odoo import _, api, models
from odoo.exceptions import ValidationError

_CUSTOMER_MOVE_TYPES = ("out_invoice", "out_refund", "out_receipt")
_VENDOR_MOVE_TYPES = ("in_invoice", "in_refund", "in_receipt")


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.constrains("partner_id", "move_type")
    def _check_customer_vendor_partner_ranks(self):
        for move in self:
            partner = move.partner_id
            if not partner:
                continue
            if move.move_type in _CUSTOMER_MOVE_TYPES and partner.customer_rank <= 0:
                raise ValidationError(
                    _(
                        "For customer invoices and credit notes, the contact must "
                        "have customer rank (use a customer contact)."
                    )
                )
            if move.move_type in _VENDOR_MOVE_TYPES and partner.supplier_rank <= 0:
                raise ValidationError(
                    _(
                        "For vendor bills and refunds, the contact must have "
                        "supplier rank (use a vendor contact)."
                    )
                )
