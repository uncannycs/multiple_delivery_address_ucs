# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo.tests import tagged, TransactionCase


@tagged("post_install", "-at_install", "customer_vendor_ucs")
class TestCustomerVendorUcs(TransactionCase):
    def test_invoice_requires_customer_rank(self):
        partner = self.env["res.partner"].create(
            {"name": "Rankless", "supplier_rank": 1, "customer_rank": 0}
        )
        journal = self.env["account.journal"].search(
            [("type", "=", "sale"), ("company_id", "=", self.env.company.id)], limit=1
        )
        self.assertTrue(journal, "Need a sale journal for this test.")
        income = self.env["account.account"].search(
            [("account_type", "=", "income")], limit=1
        )
        self.assertTrue(income, "Need an income account for this test.")
        with self.assertRaises(ValidationError):
            self.env["account.move"].create(
                {
                    "move_type": "out_invoice",
                    "partner_id": partner.id,
                    "journal_id": journal.id,
                    "invoice_line_ids": [
                        (
                            0,
                            0,
                            {
                                "name": "Line",
                                "quantity": 1,
                                "price_unit": 10.0,
                                "account_id": income.id,
                            },
                        )
                    ],
                }
            )
