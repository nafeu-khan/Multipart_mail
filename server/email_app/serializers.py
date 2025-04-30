from rest_framework import serializers
from django.conf import settings

class EmailSendSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    education = serializers.CharField()
    contact = serializers.CharField()
    address = serializers.CharField()
    project_idea = serializers.CharField()
    screenshot = serializers.ImageField()
    recipients = serializers.ListField(
        child=serializers.EmailField(), min_length=1
    )

    def validate_recipients(self, recipients):
        allowed = settings.ALLOWED_RECIPIENT_DOMAINS
        for email in recipients:
            if not any(email.endswith(domain) for domain in allowed):
                raise serializers.ValidationError(
                    "Only Gmail, Hotmail, Yahoo, and careers@accelx.net are allowed"
                )
        return recipients

