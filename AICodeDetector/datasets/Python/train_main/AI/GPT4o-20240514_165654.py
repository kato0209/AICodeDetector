
    """Defines the security context"""
    security_context = {
        'user': self.current_user,
        'roles': self.user_roles,
        'permissions': self.user_permissions,
        'is_authenticated': self.is_authenticated,
        'session_id': self.session_id,
    }
    return security_context
