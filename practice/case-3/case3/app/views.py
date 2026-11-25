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

   if not greeting:
      last_user = UserName.objects.order_by('-id').first()
      if last_user:
         greeting = f'Привет, {last_user.name}!'

   return render(request, 'app/index.html', {
      'greeting': greeting,
      'error': error,
   })