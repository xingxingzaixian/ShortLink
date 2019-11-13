# encoding: utf-8
"""
@version: 1.0
@author: 
@file: views
@time: 2019-10-29 22:54
"""
from redis import Redis
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_api.serializer import LinkSerializer
from utils.calc_shortlink import CalcShortLink
from shortlink.settings import REDIS_HOST, REDIS_PORT
from urllib.parse import urlsplit

class LinkView(APIView):
    authentication_classes = []
    def post(self, request):
        ser = LinkSerializer(data=request.data)
        if ser.is_valid():
            calc = CalcShortLink(ser.data)
            short_code = calc.parse()
            if short_code:
                http = urlsplit(request.build_absolute_uri(None)).scheme
                host = request.META['HTTP_HOST']
                shorturl = http + '://' + host + '/' + short_code + '/'
                return Response({'link': shorturl})
        return Response({'result': 'failure', 'message': 'Failed to get short link, please try again'})


class VisitView(APIView):
    authentication_classes = []
    def get(self, request, uid=None):
        rc = Redis(host=REDIS_HOST, port=REDIS_PORT, db=1)
        link = rc.get(uid)
        if link:
            return HttpResponseRedirect(link)
        return Response({'result': 'failure', 'message': 'You have not registered a short link yet'})