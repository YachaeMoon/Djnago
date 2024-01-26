#화면 안만들어서 render 필요 없음
from rest_framework.response import Response
from rest_framework.decorators import api_view

#GET 요청이 오면 함수를 호출
@api_view(['GET'])
def hello(request):
    return Response("Hello REST API")

from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def booksAPI(request):
    #GET 방식의 처리 - 조회를 요청하는 경우
    if request.method == 'GET':
        #테이블의 데이터를 전부 가져오기
        books = Book.objects.all()
        #출력하기 위해서 브라우저의 형식으로 데이터를 변환
        serializer = BookSerializer(books, many=True)
        #출력
        return Response(serializer.data)
        
    #POST 방식의 처리 - 삽입하는 경우
    elif request.method == 'POST':
        #클라이언트에서 전송된 데이터를 가지고 Model 인스턴스 생성
        serializer = BookSerializer(data = request.data)
        #유효성 검사르 ㄹ수해애서 통과하면 삽입, 실패하면 이유 출력
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
