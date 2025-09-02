from django.shortcuts import render

# Add your view methods here    
def home(request):
    return render(request, 'home/home.html')  
