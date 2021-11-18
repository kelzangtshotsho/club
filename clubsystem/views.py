from django.shortcuts import render, redirect
from .models import Photo, Record, Club

# Create your views here.

def index(request):
	photos = Photo.objects.all()
	context = {'photos': photos}
	return render(request, "index.html", context)

def viewPhoto(request, pk):
	photo = Photo.objects.get(id=pk)
	return render(request, 'photo.html', {'photo': photo})

def recordnow(request):
	stu = Record.objects.all()
	return render(request, 'record.html',{'stu': stu})


def addPhoto(request):

	if request.method == 'POST':
		data = request.POST

		add = Club.objects.create(
			
			Name = data['Name'],
			Email = data['Email'],
			Club = data['Club'],
			
			)
		return redirect('index')

		# print('data:', data)
		# print('Image:', Image)
		
	return render(request, 'add.html')
