from django.http import HttpResponse
from .excel import export_userdata

# Create your views here.
def export(request):
    response = HttpResponse(content_type='application/ms-excel') # this tells browsers that the document is an MS-EXCEL file, instead of an HTML file
    response['Content-Disposition'] = 'attachment; filename="userdata.xls"' # this contains CSV filename and downloads files with that name

    return export_userdata(response)