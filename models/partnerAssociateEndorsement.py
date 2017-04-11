# -*- coding: utf-8 -*-
#-*- partnerAssociateEndorsement.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class partnerAssociateEndorsement ( models.Model):
	_name = "partner.associate.endorsement"

	x_idPartner			= fields.Many2one ( "res.partner")
	
	x_strNumber			= fields.Char ( string = "Numero aval")
	x_dateSignUp		= fields.Date ( string = "F aval")
	x_dateExpiration	= fields.Date ( string = "F vencimiento")
	x_eType				= fields.Selection (	string = "Tipo aval",
												selection = [
															('type1', 'Aval'),
															('type2', 'Deposito'),
															('type3', 'Seguro')
															])
	x_eState			= fields.Selection (	string = "Estado aval",
												selection = [
															('state1', 'En vigor'),
															('state2', 'Devuelto')
															])
	x_fAmount			= fields.Float ( string = "Importe", digits=(3,2))