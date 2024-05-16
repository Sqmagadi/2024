from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import GroupSerializer, UserSerializer, ProductSerializer, SpecificationSerializer, CategorySerializer, MobileBannerSerializer

from store.models import Product, Category
from .models import MobileBanner

from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status


# @api_view(['GET'])
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

# @api_view(['GET'])
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]
    


@api_view(['POST'])
def register(request):
    data = request.data
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return JsonResponse({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        return JsonResponse({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username, email=email, password=password)
    return JsonResponse({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    user = authenticate(username=email, password=password)
    if user is not None:
        return JsonResponse({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['GET'])
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny] 
    # permission_classes = [permissions.IsAuthenticated]
# @api_view(['GET'])
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny] 
    # permission_classes = [permissions.IsAuthenticated]
    
    
class MobileBannerListView(generics.ListAPIView):
    queryset = MobileBanner.objects.all()
    serializer_class = MobileBannerSerializer
    permission_classes = [permissions.AllowAny] 