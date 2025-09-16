from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _order = "price desc"
    
    _sql_constraints = [
        ('check_offer_price', 'CHECK(price > 0)', 'Offer price must be strictly positive'),
    ]

    # Basic Information
    price = fields.Float()
    status = fields.Selection(
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ], copy=False)
    validity = fields.Integer(default=7, string='Validity (days)')
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline', string='Deadline')
    
    # Relationships
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)
    
    # Computed Methods
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            # Use create_date if available, otherwise use today as fallback
            base_date = record.create_date.date() if record.create_date else fields.Date.today()
            record.date_deadline = base_date + timedelta(days=record.validity)
    
    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline and record.create_date:
                # Calculate validity based on deadline and create_date
                base_date = record.create_date.date()
                delta = record.date_deadline - base_date
                record.validity = delta.days
            elif record.date_deadline:
                # If no create_date, use today as fallback
                today = fields.Date.today()
                delta = record.date_deadline - today
                record.validity = delta.days
    
    # Button Action Methods (Public - no underscore prefix)
    def action_accept(self):
        for record in self:
            # Refuse all other offers for this property first
            other_offers = record.property_id.offer_ids.filtered(lambda o: o.id != record.id)
            other_offers.write({'status': 'refused'})
            
            # Accept this offer
            record.status = 'accepted'
            
            # Set buyer and selling price on the property
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price
        return True
    
    def action_refuse(self):
        for record in self:
            record.status = 'refused'
        return True
