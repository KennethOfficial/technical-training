from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    
    def __init__(self, *args, **kwargs):
        super(EstateProperty, self).__init__(*args, **kwargs)
        _logger.info("EstateProperty model initialized with state field")

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