from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class PasswordComplexityValidator:
    """
    Valide que le mot de passe contient :
    - Au moins 12 caractères
    - Au moins une lettre majuscule
    - Au moins une lettre minuscule
    - Au moins un chiffre
    - Au moins un caractère spécial
    """

    def validate(self, password, user=None):
        if len(password) < 12:
            raise ValidationError(
                _("Le mot de passe doit contenir au moins 12 caractères."),
                code='password_too_short',
            )
        
        if not any(char.isupper() for char in password):
            raise ValidationError(
                _("Le mot de passe doit contenir au moins une lettre majuscule."),
                code='password_no_upper',
            )
        
        if not any(char.islower() for char in password):
            raise ValidationError(
                _("Le mot de passe doit contenir au moins une lettre minuscule."),
                code='password_no_lower',
            )
        
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                _("Le mot de passe doit contenir au moins un chiffre."),
                code='password_no_digit',
            )
        
        special_characters = "!@#$%^&*()_+-=[]{};:,.<>/?`~"
        if not any(char in special_characters for char in password):
            raise ValidationError(
                _("Le mot de passe doit contenir au moins un caractère spécial."),
                code='password_no_special',
            )
        