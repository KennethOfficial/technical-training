from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    
    _check_name_unique = models.Constraint(
        'UNIQUE(name)',
        'Property type name must be unique.',
    )

    # Basic Information
    name = fields.Char(required=True)
    