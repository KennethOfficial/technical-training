from odoo import models
import logging

_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        # Add debugging to verify the override is working
        _logger.info("Estate Account: action_sold method called for property: %s", self.name)
        print(f"Estate Account: Selling property '{self.name}' - Invoice creation will be added here")
        
        # Call the parent method to maintain original functionality
        return super().action_sold()
