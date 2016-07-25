from django.core.exceptions import ValidationError


def valid_extension_pdf(value):
    if (not value.name.endswith('.pdf')) or (not value.name.endswith('.PDF')):
        raise ValidationError("Adjuntar archivos unicamnete de  extension PDF")

