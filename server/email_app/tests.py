from rest_framework.test import APITestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
import tempfile
from PIL import Image
import io

class SendEmailTests(APITestCase):
    def generate_image_file(self):
        image = Image.new('RGB', (100, 100), color='red')
        byte_io = io.BytesIO()
        image.save(byte_io, 'JPEG')
        byte_io.seek(0)
        return SimpleUploadedFile('screenshot.jpg', byte_io.read(), content_type='image/jpeg')

    def test_send_email_success(self):
        url = reverse('send-selection-email')
        image = self.generate_image_file()
        payload = {
            'name': 'John Doe',
            'education': 'BSc in CSE',
            'contact': '123456789',
            'address': 'Somewhere in Earth',
            'project_idea': 'A cool AI-based chatbot',
            'recipients': ['test@gmail.com', 'careers@accelx.net']
        }

        data = {
            **payload,
            'screenshot': image
        }

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('success', response.data['status'])

    def test_send_email_invalid_recipient(self):
        url = reverse('send-selection-email')
        image = self.generate_image_file()
        payload = {
            'name': 'Jane Smith',
            'education': 'BSc in Math',
            'contact': '987654321',
            'address': 'Nowhere',
            'project_idea': 'Automated grading system',
            'recipients': ['test@example.com']  
        }

        data = {
            **payload,
            'screenshot': image
        }

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Only Gmail', str(response.data['message']))
