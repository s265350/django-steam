import xlwt
from django.http import HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def export(request):
    response = HttpResponse(content_type='application/ms-excel') # this tells browsers that the document is an MS-EXCEL file, instead of an HTML file
    response['Content-Disposition'] = 'attachment; filename="users.xls"' # this contains CSV filename and downloads files with that name

    book = xlwt.Workbook(encoding='utf-8') #  creates a Workbook of encoding utf-8
    sheet = book.add_sheet('Users Data') # creates a Sheet named “Users Data” and all the data will be written inside this sheet

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'First Name', 'Last Name', 'Email Address', ]

    for col_num in range(len(columns)):
        sheet.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            sheet.write(row_num, col_num, row[col_num], font_style)

    book.save(response) # saving the workbook and Excel file will automatically get downloaded

    return response