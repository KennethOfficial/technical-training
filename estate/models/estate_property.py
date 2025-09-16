from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    
    def _auto_init(self):
        """Override _auto_init to add debugging info when model is initialized"""
        _logger.info("EstateProperty model being initialized with state field")
        result = super(EstateProperty, self)._auto_init()
        _logger.info("EstateProperty model successfully initialized")
        return result

    # Basic Information
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda self: fields.Date.add(fields.Date.today(), months=2))
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled'),
        ], default='new')
    # Pricing
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    
    # Property Details
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    
    # Features
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ]
    )