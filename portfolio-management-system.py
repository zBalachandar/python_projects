# models.py

from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Holding(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.symbol} - {self.quantity}"
Then, create views to handle CRUD operations for portfolios and holdings:

python
Copy code
# views.py

from rest_framework import viewsets
from .models import Portfolio, Holding
from .serializers import PortfolioSerializer, HoldingSerializer
from rest_framework.permissions import IsAuthenticated

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

class HoldingViewSet(viewsets.ModelViewSet):
    queryset = Holding.objects.all()
    serializer_class = HoldingSerializer
    permission_classes = [IsAuthenticated]
Next, create serializers to convert model instances to JSON and vice versa:

python
Copy code
# serializers.py

from rest_framework import serializers
from .models import Portfolio, Holding

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'user', 'name']

class HoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holding
        fields = ['id', 'portfolio', 'symbol', 'quantity', 'purchase_price']
Finally, configure URLs to route requests to the appropriate views:

python
Copy code
# urls.py

from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'portfolios', views.PortfolioViewSet)
router.register(r'holdings', views.HoldingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
Remember, this is a simplified example. In a real-world application, you would need to add authentication, validation, error handling, and additional features such as market data integration and quantitative analysis.



'''Since this is just a code example and not a complete Django project, you can follow these steps to export the code:

Create a new directory on your local machine where you want to store the code for your Django project.

Inside the directory, create a new folder named portfolio_management_system.

Inside the portfolio_management_system folder, create the following files: models.py, views.py, serializers.py, and urls.py.

Copy and paste the code provided for each file into their respective files in your local directory'''

#Ensure you have Django and Django REST Framework installed in your Python environment. You can install them using pip:
Copy code
pip install django djangorestframework

#Initialize a new Django project by running the following command in your terminal or command prompt within your project directory:
django-admin startproject myproject
#Replace myproject with the name you want to give your Django project.
#Move the portfolio_management_system folder containing your code into the myproject folder.
#Navigate to the myproject directory:
bash

code : cd myproject

#Run the development server:

code : python manage.py runserver
Visit http://localhost:8000 in your web browser to see your Django project running.

Remember that this is just a basic setup. You'll need to configure your Django project further, including database setup, user authentication, and additional features depending on your requirements.





