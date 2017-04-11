# -*- coding: utf-8 -*-
# © 2017 Igor V. Kartashov
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "associate partner data",
    "version": "9.0.1.0",
    "summary": "associate partner data",
    "description": """
		author: i-vk
		v9.0.1.0
		associate partner data, applies for ASTIC
	""",
    "category": "Partner",
    "author": "Igor V. Kartashov",
    "website": "http://www.astic.net",
    "license": "AGPL-3",
    "depends": ['base'],
    "data": [
		"views/partnerAssociate.xml",
    ],
    "images": [
			"images/ivk.png",
			],
    "installable": True,
    "application": True,
	"auto_install": False,
    "price": 0.00,
    "currency": "EUR"
}