# -*- coding: utf-8 -*-
#-*- partnerUnlinkWizard.py
from openerp import tools
from openerp import models, fields, api

class partnerUnlinkWizard ( models.TransientModel):
	_name = "partner.unlink.wizard"

	e_reason	= fields.Selection (	string = "Seleccionar Razón baja",
										selection = [
													('impago', 'Impago'),
													('voluntaria', 'Voluntaria')])

	@api.multi
	def do_unlink ( self):
		self.ensure_one()
		
#		if not self.e_reason:
#			raise exceptions.ValidationError ( 'Es necesario indicar la razón de la baja')
		
		#else:
		
		patner_id = self.context.get ('active_id', False)
		
		patner_id.write({'x_bActiveMember': False})
		patner_id.write({'x_bOldMember': True})
		patner_id.write({'x_dateUnsubscribe': fields.Date.today()})
		patner_id.write({'x_eUnsubscribeReason': self.e_reason})
		#quitar ASTIC en pestaña Transporte
		self.env["partner.transport.associations"].search([('x_idPartner','=',self.id)]).unlink()