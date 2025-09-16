from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    
    _sql_constraints = [
        ('check_name_unique', 'UNIQUE(name)', 'Property tag name must be unique'),
    ]

    # Basic Information
    name = fields.Char(required=True)
    