# -*- coding: utf-8 -*-
# © 2017 Igor V. Kartashov
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "partner associate data",
    "version": "9.0.1.0",
    "summary": "specifica data to manage associations",
    "description": """
		i-vk
		v9.0.1.0
		specifica data to manage associations, applies to ASTIC
	""",
    "author": "Igor V. Kartashov",
    "license": "AGPL-3",
    "website": "http://www.astic.net",
    "category": "Partner",
    "depends":	[
				"base",
				"partnerTransport",
				],
    "data": [
		"views/partnerAssociate.xml",
		"views/partnerUnlinkWizard.xml",
		"security/ir.model.access.csv",
	],
    "installable": True,
    "application": True,
	"auto_install": False,
    "price": 0.00,
    "currency": "EUR"
}