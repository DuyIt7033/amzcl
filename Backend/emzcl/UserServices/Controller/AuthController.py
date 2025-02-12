from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from UserServices.models import Users  
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from emzcl.Helpers import renderResponse
from emzcl.permission import IsSuperAdmin

class SignupAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')  # Thay 'username' bằng chuỗi
        email = request.data.get('email')  # Thay 'email' bằng chuỗi
        password = request.data.get('password')  # Thay 'password' bằng chuỗi
        profile_pic = request.FILES.get('profile_pic')  # Lấy file ảnh từ request.FILES
        

        emailCheck = Users.objects.filter(email=email)
        if emailCheck.exists():
            return renderResponse(data = 'Email Already Exists',message ='Email Already Exists', status=status.HTTP_400_BAD_REQUEST)

        usernameCheck = Users.objects.filter(username=username)
        if usernameCheck.exists():
            return renderResponse(data = 'Username Already Exists',message ='Username Already Exists', status=status.HTTP_400_BAD_REQUEST)


        if username is None or email is None or password is None:
            return renderResponse(data = 'Please fill in all information',message='Please fill in all information', status=status.HTTP_400_BAD_REQUEST)

        user = Users.objects.create_user(username=username, email=email, password=password, profile_pic=profile_pic)
        if request.data.get('domain_user_id_id'):
            user.domain_user_id= Users.objects.get(id=request.data.get('domain_user_id_id'))

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
            return renderResponse(data = 'Please fill in all information',message='Please fill in all information', status=status.HTTP_400_BAD_REQUEST)
        
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
            return renderResponse(data = 'Username or password is incorrect',message='Username or password is incorrect ', status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return renderResponse(data = 'Please use post method to login',message=' Please use post method to login', status=status.HTTP_400_BAD_REQUEST)

# API công khai (không yêu cầu đăng nhập)
class PublicAPIView(APIView):
    def get(self, request):
        return renderResponse(data ='Puclic Api',message='Puclic Api', status=status.HTTP_400_BAD_REQUEST)

# API yêu cầu JWT Token
class ProtectedAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Yêu cầu xác thực bằng JWT
    authentication_classes =  [JWTAuthentication]
    def get(self, request):
        return renderResponse(data ='This is protected API. You can access if your authentication is successful',message='This is protected API. You can access if your authentication is successful', status=status.HTTP_400_BAD_REQUEST)

class SuperAdminCheckAPI(APIView):
    authentication_classes = [JWTAuthentication]  # Chỉ cần xác thực bằng JWT
    permission_classes = [IsAuthenticated, IsSuperAdmin]  # Sau khi xác thực, kiểm tra quyền

    def get(self, request):
        return renderResponse(
            data='This is Super Admin API. You can access if your authentication is successful',
            message='This is Super Admin API. You can access if your authentication is successful',
            status=status.HTTP_200_OK  # Trả về mã trạng thái 200 OK khi thành công
        )