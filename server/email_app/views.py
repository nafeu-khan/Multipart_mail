from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailSendSerializer
from .utils.email_utils import send_candidate_email
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
class SelectionEmailView(APIView):

    @swagger_auto_schema(
        request_body=EmailSendSerializer,
        responses={
            200: openapi.Response(
                description="Email sent successfully",
                examples={"application/json": {
                    "status": "success",
                    "message": "Email sent to 4 recipients"
                }}
            ),
            400: openapi.Response(
                description="Validation error",
                examples={"application/json": {
                    "status": "error",
                    "message": "Only Gmail, Hotmail, Yahoo, and careers@accelx.net are allowed"
                }}
            ),
        },
        operation_description="Send formatted selection email with embedded screenshot to allowed recipients."
    )
    def post(self, request):
        serializer = EmailSendSerializer(data=request.data)
        if serializer.is_valid():
            try:
                send_candidate_email(serializer.validated_data, request.FILES['screenshot'])
                return Response({"status": "success", "message": f"Email sent to {len(serializer.validated_data['recipients'])} recipients"})
            except Exception as e:
                return Response({"status": "error", "message": str(e)}, status=500)
        return Response({"status": "error", "message": serializer.errors}, status=400)

