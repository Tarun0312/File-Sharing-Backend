from django.shortcuts import render,redirect
from rest_framework import viewsets
from opuserfileupload.models import OperationUser
from opuserfileupload.serializers import OperartionSerializer
from django.http import HttpResponse
from .models import UploadedFile
from .forms import UploadFileForm

# Create your views here.

class OperationUserViewSet(viewsets.ModelViewSet):
    queryset = OperationUser.objects.all()
    serializer_class = OperartionSerializer


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    files = UploadedFile.objects.all()
    return render(request, 'uploadfile.html', {'form': form, 'files': files})

def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response