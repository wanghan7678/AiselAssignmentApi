from django.test import TestCase
import json
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, APIClient, URLPatternsTestCase
from rest_framework import status
from .models import User, Patient
# Create your tests here.


class UserTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('PatientsApi.urls'))
    ]

    def setUp(self):
        self.user1 = User.objects.create_user(
            email='test1@test.com',
            password='abcd',
        )

        self.admin = User.objects.create_superuser()(
            email='admin@test.com',
            password='admin',
        )

    def test_login(self):
        """ Test if a user can login and get a JWT response token """
        url = reverse('user_login')
        data = {
            'email': 'admin@test.com',
            'password': 'admin'
        }
        response = self.client.post(url, data)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response_data)


class PatientTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('PatientsApi.urls'))
    ]

    def setUp(self):
        self.user1 = User.objects.create_user(
            email='test1@test.com',
            password='abcd',
        )

        self.admin = User.objects.create_superuser()(
            email='admin@test.com',
            password='admin',
        )

        self.patient_test = Patient.objects.create(
            first_name = 'Foo',
            last_name = 'Test',
            email='foo.test@tester.com',
            phone_number = '+4552003344',
            dob = '1997-10-01',
            deleted=False
        )

    def test_patient_all(self):
        url = reverse('user_login')
        data = {'email': 'admin@test.com', 'password': 'admin'}
        response = self.client.post(url, data)
        login_response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in login_response_data)
        token = login_response_data['access']

        # Test the endpoint
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = client.get(reverse('patients_all'))
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Patient.objects.count(), len(response_data['results']))