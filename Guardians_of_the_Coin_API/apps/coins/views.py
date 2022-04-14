from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from Guardians_of_the_Coin_API.apps.core.coin_util import GetTopAmountCoinList, GetTopRSICoinList, GetRSI
from Guardians_of_the_Coin_API.apps.core.authentication import FirebaseAuthentication
# Create your views here.
class CoinView(APIView):
    """
    GET /coins
    """
    def get(self, request,  **kwargs):
        GATHER_INTERVAL = getattr(settings, 'ACCESS_KEY', None)
        print(GATHER_INTERVAL)
        return Response("message", status=status.HTTP_200_OK)
    
class CoinRecommendView(APIView):
    """

    GET /coins/recommend
    """
    def get(self, request, **kwargs):
        TopCoinList =GetTopAmountCoinList("day",10)
        return Response(TopCoinList, status=status.HTTP_200_OK)
        
class CoinRSIView(APIView):
    """
    GET /coins/rsi
    """
    def get(self, request, **kwargs):
        print(request.META.get('HTTP_AUTHORIZATION'));
        TopCoinList = GetTopRSICoinList("minute240",10)
        # getData = GetRSI("KRW-MTL","minute240",14,-1);
        # return Response({"KRW-MTL":getData,"message":"success"}, status=status.HTTP_200_OK)
        return Response(TopCoinList, status=status.HTTP_200_OK)
    