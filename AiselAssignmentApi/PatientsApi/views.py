from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import status
from datetime import datetime
from .models import Patient, User
from .serializers import PatientSerializer, UserLoginSerializer, UserListSerializer, UserRegistrationSerializer
from .response import rest_resp, rest_resp_list, rest_resp_snapshot, rest_resp_login, ApiStdResp

# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def patients_all(request):
    patients = Patient.objects.all().filter(deleted=False)
    serializer = PatientSerializer(patients, many=True)
    return rest_resp_list(results=serializer.data)
    return ApiStdResp.Bad


@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    valid = serializer.is_valid(raise_exception=True)
    if valid:
        return rest_resp_login(access_token=serializer.data['access'],
        refresh_token=serializer.data['refresh'], email=serializer.data['email'],
        role=serializer.data['role'])
    return ApiStdResp.FailLogin 
        


@api_view(["POST"])
@permission_classes([AllowAny])
def user_register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    valid = serializer.is_valid(raise_exception=True)
    if valid:
        serializer.save()
        return rest_resp(results=serializer.data, code=status.HTTP_201_CREATED)
    return ApiStdResp.Bad

@api_view(["GET"])
@permission_classes([IsAdminUser])
def user_all(request):
    if request.user.role != 1:
        return ApiStdResp.NoPermission
    users = User.objects.all()
    serializer = UserListSerializer(data=users, many=True)
    if serializer.is_valid():
        return rest_resp_list(results=serializer.data)
    return ApiStdResp.Bad



@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def patient_item(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if patient:
        serializer = PatientSerializer(patient)
        if serializer.is_valid():
            return rest_resp(results=serialzer.data)
    return ApiStdResp.NotFound


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def patient_new(request):
    if request.user.role != 1:
        return ApiStdResp.NoPermission
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    first_name = body['firstName']
    last_name = body['lastName']
    email = body['email']
    phone_number = body['phone']
    dob = body['dob']
    if email:
        patient, created = Patient.objects.get_or_create(email=email)
        patient.first_name = first_name
        patient.last_name = last_name
        patient.phone_number = phone_number
        patient.dob = dob
        patient.deleted = False
        patient.save()
        serializer = PatientSerializer(patient)
        return rest_resp(results=serializer.data)
    else:
        return ApiStdResp.Bad


@api_view(["POST", "DELETE"])
@permission_classes([IsAuthenticated])
def patient_delete(request, patient_id):
    if request.user.role != 1:
        return ApiStdResp.NoPermission
    patient = Patient.objects.get(id=patient_id)
    if patient:
        patient.deleted = True
        patient.deleted_at = datetime.now()
        patient.save()
        return rest_resp()
    else:
        return ApiStdResp.NotFound


@api_view(["POST"])
def patient_update(request, patient_id):
    if request.user.role != 1:
        return ApiStdResp.NoPermission
    patient = Patient.objects.get(id=patient_id)
    if patient:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        first_name = body['firstName']
        last_name = body['lastName']
        email = body['email']
        phone_number = body['phone']
        dob = body['dob']
        patient.first_name = first_name
        patient.last_name = last_name
        patient.email = email
        patient.phone_number = phone_number
        patient.dob = dob
        patient.save()
        serializer = PatientSerializer(patient)
        return rest_resp(results=serializer.data)
    else:
        return ApiStdResp.NotFound