# -*- coding: utf-8 -*-
# -*- partnerAssociate.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class partnerAssociate ( models.Model):
	_inherit = "res.partner"

	#member state control
	x_bActive				= fields.Boolean ( string = "Activo", readonly=True)
	x_bOldMember			= fields.Boolean ( string = "Antiguo miembro", readonly=True, default= False)

	x_dateSignUp			= fields.Date ( string = "F. Alta", readonly=True)
	x_dateUnsubscribe		= fields.Date ( string = "F. Baja", readonly=True)
	
	x_eUnsubscribeReason	= fields.Selection (	string = "Razon baja",
													selection = [
																('impago', 'Impago'),
																('voluntaria', 'Voluntaria')])

	#member position in the association
	x_bDirectionBoard		= fields.Boolean ( string = "Junta directiva")

	#quotas
	x_nAssociatedVehicles	= fields.Integer ( string = "Vehículos asociados", inverse="calc_quota_three")
	x_fQuotaOne				= fields.Float ( string = "Mensual", digits = (3,2))
	x_fQuotaThree			= fields.Float ( string = "Trimestral", help="4€ per vehicle", digits = (3,2))
	
	#risk control
	x_nTIR_Block			= fields.Integer ( string = "Cuadernos", help = "Numero de cuadernos TIR")
	x_nTIR_Certificate		= fields.Integer ( string = "Certificados de garantia", help = "Numero del anyo pasado")
	x_idsTIR_Endorcement	= fields.One2many ( 'partner.associate.endorsement', 'x_idPartner')

	#member code
	x_serialAsticCode		= fields.Char ( string = "Código", readonly=True, copy=False)
	
	@api.one
	def do_associate ( self):
		self.write({'x_serialAsticCode': self.env['ir.sequence'].get('partner.associate.code.sequence')})
		self.write({'x_dateSignUp': fields.Date.today()})
		self.write({'x_bActive': True})

	@api.one
	def do_DEassociate ( self):
		self.write({'x_bActive': False})
		self.write({'x_bOldMember': True})
		self.write({'x_dateUnsubscribe': fields.Date.today()})

	@api.one
	def calc_quota_three ( self):
		self.x_fQuotaThree = self.x_nAssociatedVehicles * 4