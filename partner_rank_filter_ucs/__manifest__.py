# -*- coding:utf-8 -*-
##############################################################################
#
#    ODOO Open Source Management Solution
#
#    ODOO Addon module by Uncannycs LLP
#    Copyright (C) 2022 Uncannycs LLP (<http://uncannycs.com>).
#
##############################################################################

{
    "name": "Partner Rank Filter UCS",
    "summary": """Partner Rank Filter UCS""",
    "version": "19.0.1.0.0",
    'author': 'Uncanny Consulting Services LLP',
    'maintainer': 'Uncanny Consulting Services LLP',
    'website': 'http://www.uncannycs.com',
    "license": "AGPL-3",
    "installable": True,
    "depends": ['sale_management', 'purchase','account'],
    "data": [
        "views/sale_purchase.xml",
    ],
    'images': ['static/description/banner.gif'],
}
