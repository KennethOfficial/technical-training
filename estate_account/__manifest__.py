{
    "name": "Estate Account",
    "version": "18.0.1.0.1",
    "application": False,  # This is a module, not an app
    "depends": ["estate", "account"],  # Depends on both estate and account modules
    'data': [
        # Empty for now - will add data files as needed
    ],
    "installable": True,
    'license': 'LGPL-3',
}
