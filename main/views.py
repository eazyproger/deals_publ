from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .myfunctions import check_correctness_file, IncorrectField, Ok, get_top
from .serializers import MySerializer


class MainAPI(APIView):
    parser_classes = (MultiPartParser, )

    def get(self, request):
        top = get_top()
        serializer = MySerializer(top, many=True)
        return Response({'response': serializer.data})

    def post(self, request):
        file = request.data['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        message = 'Status: Error, Desc: <'
        try:
            check_correctness_file(filename)
        except (UnicodeDecodeError, KeyError, ValueError, IncorrectField, MultiValueDictKeyError) as e:
            message += str(e)
            message += '> - в процессе обработки файла произошла ошибка'
        except Ok:
            message = 'Status: OK - файл был обработан без ошибок'
        fs.delete(name=filename)
        if message != '':
            return Response(message, status=status.HTTP_207_MULTI_STATUS)
        else:
            return Response(message, status=status.HTTP_200_OK)

