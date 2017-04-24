# -*- coding: utf-8 -*-
#-*- partnerAssociateHistory.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class partnerAssociateHistory ( models.Model):
	_name = "partner.associate.history"

	x_idPartner			= fields.Many2one ( "res.partner")

	x_dateSignUp			= fields.Date ( string = "F Alta", readonly=True)
	x_dateUnsubscribe		= fields.Date ( string = "F Baja", readonly=True)

	x_eUnsubscribeReason	= fields.Selection (	string = "Razón baja",
													selection = [
																('impago', 'Impago'),
																('voluntaria', 'Voluntaria')])