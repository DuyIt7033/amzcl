from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from UserServices.models import Users  
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class SignupAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')  # Thay 'username' bằng chuỗi
        email = request.data.get('email')  # Thay 'email' bằng chuỗi
        password = request.data.get('password')  # Thay 'password' bằng chuỗi
        profile_pic = request.FILES.get('profile_pic')  # Lấy file ảnh từ request.FILES
        
        if username is None or email is None or password is None:
            return Response({'error': 'Xin hãy điền đủ thông tin'}, status=status.HTTP_400_BAD_REQUEST)

        user = Users.objects.create_user(username=username, email=email, password=password, profile_pic=profile_pic)
        user.save()
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        access['username'] = user.username
        access['email'] = user.email
        access['profile_pic'] = user.profile_pic.url if user.profile_pic else None  # Trả về URL của ảnh, nếu có

        return Response({'access': str(access), 'refresh': str(refresh), 'message': 'Tạo thành công'}, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    def post(self, request):
        # Lấy dữ liệu từ request
        username = request.data.get('username')
        password = request.data.get('password')

        print(f"Username: {username}, Password: {password}")  # Thêm log để kiểm tra

        # Kiểm tra dữ liệu
        if username is None or password is None:
            return Response({'error': 'Vui lòng nhập đầy đủ username và password.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Xác thực người dùng
        user = authenticate(request, username=username, password=password)
        print(f"User: {user}")  # Thêm log kiểm tra đối tượng người dùng

        if user:
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            access['username'] = user.username
            access['email'] = user.email
            access['profile_pic'] = user.profile_pic.url if user.profile_pic else None  # Trả về URL của ảnh, nếu có

            
            return Response({
                'refresh': str(refresh),
                'access': str(access),  
            })
        else:
            return Response({'error': 'Tên đăng nhập hoặc mật khẩu không đúng.'}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        return Response({'message':'Dùng Post để login'})

# API công khai (không yêu cầu đăng nhập)
class PublicAPIView(APIView):
    def get(self, request):
        return Response({"message": "Đây là API công khai, ai cũng có thể truy cập."})

# API yêu cầu JWT Token
class ProtectedAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Yêu cầu xác thực bằng JWT
    authentication_classes =  [JWTAuthentication]
    def get(self, request):
        return Response({"message": f"Chào {request.user.username}, bạn đã xác thực thành công!"})

