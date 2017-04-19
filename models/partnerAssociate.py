# -*- coding: utf-8 -*-
# -*- partnerAssociate.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class partnerAssociate ( models.Model):
	_inherit = "res.partner"

	#member state control
	x_strState				= fields.Char ( string = "Estado", compute="show_state")

	x_bActive				= fields.Boolean ( string = "Activo", readonly=True)
	x_bOldMember			= fields.Boolean ( string = "Antiguo miembro", readonly=True, default= False)

	#codigo asociado
	x_serialAsticCode		= fields.Char ( string = "Código", readonly=True, copy=False)

	x_dateSignUp			= fields.Date ( string = "F. Alta", readonly=True)
	x_dateUnsubscribe		= fields.Date ( string = "F. Baja", readonly=True)
	
	x_eUnsubscribeReason	= fields.Selection (	string = "Razón baja",
													selection = [
																('impago', 'Impago'),
																('voluntaria', 'Voluntaria')])

	#if belongs to direction board
	x_bDirectionBoard		= fields.Boolean ( string = "Junta directiva")

	#quotas
	x_nAssociatedVehicles	= fields.Integer ( string = "Vehículos asociados")
	x_fQuotaOne				= fields.Float ( string = "Mensual", digits = (3,2), default=125.00)
	x_fQuotaPerVehicle		= fields.Float ( string = "Por vehiculo", digits = (3,2), default=4.00)
	x_fQuotaThree			= fields.Float ( string = "Trimestral", help="cuota_por_vehiculo x numero_vehiculos", digits = (3,2), compute="show_quota_three")

	#numero cuadernos del año pasado
	x_nTIR_Block			= fields.Integer ( string = "Cuadernos", help = "Numero de cuadernos TIR")
	#numero certificados de garantia del año pasado
	x_nTIR_Certificate		= fields.Integer ( string = "Certificados de garantia", help = "Numero del anyo pasado")

	#control de riesgo
	x_idsTIR_Endorcement	= fields.One2many ( 'partner.associate.endorsement', 'x_idPartner', string = "Avales")
	x_idsHistory			= fields.One2many ( 'partner.associate.history', 'x_idPartner', string = "Historial afiliaciones")

	@api.one
	def show_state ( self):
		if self.x_bActive == True:
			self.x_strState = "Asociado activo"
		else:
			if self.x_bOldMember == True:
				self.x_strState = "Antiguo asociado"
			else:
				self.x_strState = "No asociado"
	
	
	@api.one
	def show_quota_three ( self):
		self.x_fQuotaThree = self.x_nAssociatedVehicles * self.x_fQuotaOne
	
	@api.one
	def do_associate ( self):
		if self.x_bOldMember == False:
			#ver partnerAssociate.xml donde esta definida 'partner.associate.code.sequence'
			self.write({'x_serialAsticCode': self.env['ir.sequence'].get('partner.associate.code.sequence')})
		self.write({'x_dateSignUp': fields.Date.today()})
		self.write({'x_bActive': True})

	@api.one
	def do_DEassociate ( self):
		self.write({'x_bActive': False})
		self.write({'x_bOldMember': True})
		self.write({'x_dateUnsubscribe': fields.Date.today()})