# -*- coding: utf-8 -*-
# -*- partnerAssociate.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit
from openerp import exceptions

class partnerAssociate ( models.Model):
	_inherit = "res.partner"

	x_eCompanyType	= fields.Selection (	string = "Tipo sociedad",
											selection = [
														('sl', 'S.L.'),
														('slu', 'S.L.U.'),
														('sa', 'S.A.'),
														('sa', 'S.A.U.'),
														('otro', 'Otro')])

	#member state control
	x_strState				= fields.Char		( string = "Estado",			compute	= "show_state")

	x_bActiveMember			= fields.Boolean	( string = "Afiliado activo",	readonly = True)
	x_bOldMember			= fields.Boolean	( string = "Antiguo afiliado",	readonly = True, default= False)

	#codigo asociado
	x_serialAsticCode		= fields.Char		( string = "Código", readonly=True, copy=False)

	x_dateSignUp			= fields.Date		( string = "F Alta", readonly=True, help = "fecha de la última alta")
	x_dateUnsubscribe		= fields.Date		( string = "F Baja", readonly=True, help = "fecha de la última baja")
	
	#OJO !!! defenido en 3 lugares
	x_eUnsubscribeReason	= fields.Selection (	string		= "Razón baja",
													selection	=	[
																	('impago', 'Impago'),
																	('voluntaria', 'Voluntaria'),
																	('cese', 'Cese actividad'),
																	('otro', 'Otro')
																	]
												)

	#if belongs to direction board
	x_bDirectionBoard		= fields.Boolean ( string = "Junta directiva", help = "si pertenece o no a la junta directiva")

	#quotas
	x_nAssociatedVehicles	= fields.Integer	( string = "Vehículos asociados", inverse = "show_quota_three")
	x_fQuotaOne				= fields.Float		( string = "Mensual",		digits = (5,2), default=125.00)
	x_fQuotaPerVehicle		= fields.Float		( string = "Por vehiculo",	digits = (3,2), default=4.00, inverse = "show_quota_three")
	x_fQuotaThree			= fields.Float		( string = "Trimestral",	help="autocalculable: cuota_por_vehiculo x numero_vehiculos")

	#N autorización de transporte, codigo de 8 digitos
	x_strAuthorizationTransport	= fields.Char		( string = "Autorización transporte",	size = 8,	help = "Nº Autorización de transporte")
	x_nAuthorizationTransport	= fields.Integer	( string = "Nº copias",					help = "N de copias de autorizaciones de transporte")
	#N licencia comunitaria, codigo 10 digitos
	x_strLicenceEU				= fields.Char		( string = "Licencia comunitaria",		size = 10,	help = "Nº Licencia comunitaria")
	#N autorizacion de operador tte, codigo 8 digitos
	x_strAuthorizationOperator	= fields.Char		( string = "Autorización operador",		size = 8,	help = "Nº Autorización de operador")
	x_nEmplyees					= fields.Integer	( string = "Nº empleados",				help = "Nº de TC1, Empleados")

	#numero cuadernos del año pasado
	x_nTIR_Block			= fields.Integer		( string = "Cuadernos TIR",				help = "Numero de cuadernos TIR")
	#numero certificados de garantia del año pasado
	x_nTIR_Certificate		= fields.Integer		( string = "Certificados de garantia",	help = "Numero del año pasado")

	#control de riesgo
	x_idsTIR_Endorcement	= fields.One2many	(
													comodel_name	= "partner.associate.endorsement",
													inverse_name	= "x_idPartner",
													string			= "Avales",
													help			= "control de riesgo"
												)

	x_idsHistory			= fields.One2many	(	comodel_name	= "partner.associate.history",
													inverse_name	= "x_idPartner",
													string			= "Historial afiliaciones",
													help			= "más reciente abajo")

	@api.one
	def show_state ( self):
		if self.x_bActiveMember == True:
			self.x_strState = "Afiliado activo"
		else:
			if self.x_bOldMember == True:
				self.x_strState = "Afiliado antiguo"
			else:
				self.x_strState = "No afiliado"

	@api.one
	@api.onchange ('x_nAssociatedVehicles', 'x_fQuotaPerVehicle')
	def show_quota_three ( self):
		self.x_fQuotaThree = self.x_nAssociatedVehicles * self.x_fQuotaPerVehicle
	
	@api.one
	def do_associate ( self):
		if self.x_bOldMember == False:
			#ver partnerAssociate.xml donde esta definida 'partner.associate.code.sequence'
			self.write({'x_serialAsticCode': self.env['ir.sequence'].get('partner.associate.code.sequence')})
		self.write({'x_dateSignUp': fields.Date.today()})
		self.write({'x_bActiveMember': True})
		#añadir ASTIC en pestaña Transporte
		i = self.env["transport.associations"].search([('x_strAssociation','=','ASTIC')])[0].id
		#if not self.x_idsAssociations.search([('x_strAssociation','=', 'ASTIC')]):
		self.x_idsAssociations = [(4, i, False)]