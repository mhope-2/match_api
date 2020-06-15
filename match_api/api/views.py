from django.shortcuts import render
from rest_framework import generics, permissions, status, views
from pathlib import Path
from rest_framework import permissions
from django.http import JsonResponse
import pickle

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


# Create your views here.
class Predict(views.APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):

        homeTeam_En = request.data["home"]
        awayTeam_En = request.data["away"]
        hOdds = request.data['hOdds']
        dOdds = request.data['dOdds']
        aOdds = request.data['aOdds']

        root = Path(".")
        my_path = root/"models"/"match.pkl"

        with open(my_path, 'rb') as file:
            model = pickle.load(file)

        try:
            # Give prediction
            outcome = np.array(model.predict(np.array([[homeTeam_En, awayTeam_En, hOdds, dOdds, aOdds]])))
        except Exception as err:
            return JsonResponse(str(err), status=status.HTTP_400_BAD_REQUEST, safe=False)

        response_dict = {query: outcome}

        return JsonResponse(response_dict, status=status.HTTP_200_OK)


# LOGIN CLASS
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return JsonResponse({'error':'Please provide both username and password'},status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({'error':'invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return JsonResponse({'token': token.key}, status=status.HTTP_200_OK)

