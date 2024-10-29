# to choose action
API_ACTION_CHOICES = [
    ('list', 'List'),
    ('retrieve', 'Retrieve'),
    ('create', 'Create'),
    ('update', 'Update'),
    ('partial_update', 'Partial Update'),
    ('destroy', 'Destroy'),
]

# to what does meaning action
ACTION_NAME = {
    'list': 'hammasini Ko\'rish',
    'retrieve': 'detail ko\'rish',
    'create': 'Yaratish',
    'update': 'Yangilash',
    'partial_update': 'qismlarni yangilash',
    'destroy': 'O\'chirish'
}

# Define the actions for easier mapping
ACTIONS = {
    'POST': 'create',
    'GET': ['retrieve', 'list'],
    'PUT': 'update',
    'PATCH': 'partial_update',
    'DELETE': 'delete'
}
