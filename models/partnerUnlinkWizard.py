# -*- coding: utf-8 -*-
#-*- partnerUnlinkWizard.py
from openerp import tools
from openerp import models, fields, api
from openerp import exceptions

class partnerUnlinkWizard ( models.TransientModel):
	_name = "partner.unlink.wizard"

	e_reason	= fields.Selection (	string = "Seleccionar Razón baja",
										selection = [
													('impago', 'Impago'),
													('voluntaria', 'Voluntaria')],
										help="Indicar la razón de la baja"
									)

	@api.multi
	def do_unlink ( self):
		self.ensure_one()
		
		if not self.e_reason:
			raise exceptions.ValidationError ( 'Es necesario indicar la razón de la baja')
		
		#else:
		partner_id = self.env.context.get ('active_ids', True)[0]
		x_partner = self.env["res.partner"].search([('id','=', partner_id)])
		
		x_partner.write({'x_bActiveMember': False})
		x_partner.write({'x_bOldMember': True})
		x_partner.write({'x_dateUnsubscribe': fields.Date.today()})
		x_partner.write({'x_eUnsubscribeReason': self.e_reason})
		#quitar ASTIC en pestaña Transporte, as1 es ASTIC
		i = self.env["transport.associations"].search([('x_strAssociation','=','ASTIC')])[0].id
		if i != 1:
			strA = "ERR UNLINK id value[" + str (i) + "]"
			raise exceptions.ValidationError ( strA)

		#if x_partner.x_idsAssociations.search([('id','=',i)]):
		x_partner.x_idsAssociations = [( 3, i, False)]

		#historial afiliación
		self.env["partner.associate.history"].create ( {
														'x_idPartner': partner_id,
														'x_dateSignUp': x_partner.x_dateSignUp,
														'x_dateUnsubscribe': x_partner.x_dateUnsubscribe,
														'x_eUnsubscribeReason': self.e_reason
														})