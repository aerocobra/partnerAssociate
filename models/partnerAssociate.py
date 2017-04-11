# -*- partnerAssociate.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class partnerAssociate ( models.Model):
	_inherit = "res.partner"

	#state
	x_bActive				= fields.Boolean ( string = "Activo")
	x_bOldMember			= fields.Boolean ( string = "Antiguo miembro")
	x_bDirectionBoard		= fields.Boolean ( string = "Junta directiva")

	x_serialAsticCode		= fields.Integer ( string = "Codigo")
	
	x_dateSignUp			= fields.Date ( string = "F. Alta")
	x_dateUnsubscribe		= fields.Date ( string = "F. Baja")
	
	x_eUnsubscribeReason	= fields.Selection (	string = "Razon baja",
													selection = [
																('impago', 'Impago'),
																('voluntaria', 'Voluntaria')])
	
	
	#quotas
	x_fQuotaOne				= fields.Float ( string = "Mensual", digits = (3,2))
	x_fQuotaThree			= fields.Float ( string = "Trimestral", digits = (3,2))
	
	x_nAssociatedVehicles	= fields.Integer ( string = "Vehiculos asociados")
	
	x_nTIR_Block			= fields.Integer ( string = "Cuadernos", help = "Numero de cuadernos TIR")
	x_nTIR_Certificate		= fields.Integer ( string = "Certificados de garantia", help = "Numero del anyo pasado")
	x_idsTIR_Endorcement	= fields.One2many ( 'partner.associate.endorsement', 'x_idPartner')