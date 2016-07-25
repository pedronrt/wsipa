from django.core.exceptions import ValidationError


def valid_extension_pdf(value):
    if (not value.name.endswith('.pdf')):
        raise ValidationError("Adjuntar archivos unicamnete de  extension PDF")

def valid_extension_kml(value):
    if (not value.name.endswith('.kml')):
        raise ValidationError("Adjuntar archivos unicamnete de  extension KML")