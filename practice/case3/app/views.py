from django.shortcuts import render
from .models import UserName

from django.shortcuts import render
from .models import UserName

def index(request):
   greeting = None
   error = None

   if request.method == 'POST':
      name = request.POST.get('name', '').strip()
      if not name:
         error = 'Пожалуйста, введите имя.'
      else:
         UserName.objects.create(name=name)
         greeting = f'Привет, {name}!'

   return render(request, 'app/index.html', {
      'greeting': greeting,
      'error': error,
   })