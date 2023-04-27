import xlwt
from ..users.models import SteamUser, SteamUserProfile, CoachProfile

def export_userdata(response):
    book = xlwt.Workbook(encoding='utf-8') #  creates a Workbook of encoding utf-8
    sheet = book.add_sheet('Users Data') # creates a Sheet named “Users Data” and all the data will be written inside this sheet

    # defining styles
    styles = dict(
        header = xlwt.easyxf('\
            font: height 320, bold on, color red;\
            pattern: pattern solid, fore_color white;\
            border: left thin, top thin, right thin, bottom thin,\
                    top_color black, bottom_color black, right_color black, left_color black;\
            align: wrap on, vert center, horiz left;\
            '),
        SteamID = xlwt.easyxf('\
            font: height 250, color white;\
            pattern: pattern solid, fore_color blue;\
            border: left thin, top thin, right thin, bottom thin;\
            align: wrap on, vert center, horiz right;\
            '),
        Username = xlwt.easyxf('\
            font: height 250, bold on, color black;\
            pattern: pattern fine_dots, fore_color white, back_color orange;\
            border: left thin, top thin, right thin, bottom thin;\
            align: wrap on, vert center, horiz left;\
            '),
        Name = xlwt.easyxf('\
            font: height 250, color black;\
            pattern: pattern solid, fore_color white;\
            border: left thin, top thin, right thin, bottom thin;\
            align: wrap on, vert center, horiz left;\
            '),
        Surname = xlwt.easyxf('\
            font: height 250, color black; \
            pattern: pattern solid, fore_color white;\
            border: left thin, top thin, right thin, bottom thin;\
            align: wrap on, vert center, horiz left;\
            '),
        Email = xlwt.easyxf('\
            font: height 250, italic on, color black;\
            pattern: pattern solid, fore_color white;\
            border: left thin, top thin, right thin, bottom thin;\
            align: wrap on, vert center, horiz left;\
            '),
        Age = xlwt.easyxf('\
            font: height 250, color black;\
            pattern: pattern solid, fore_color white;\
            border: left thin, top thin, right thin, bottom thin;\
            align: wrap on, vert center, horiz center;\
            '),
        URL = xlwt.easyxf('\
            font: height 250, italic on, color black;\
            pattern: pattern solid, fore_color white;\
            border: left thick, top thick, right thick, bottom thick,\
                    top_color red, bottom_color red, right_color red, left_color red;\
            align: wrap on, vert center, horiz left;\
            '),
    )

    columns = ['SteamID', 'Username', 'Name', 'Surname', 'Email', 'Age', 'URL']

    # body data collection
    rows = []
    users = SteamUser.objects.all().values_list('username', 'first_name', 'last_name', 'email', 'age')
    for user in users:
        (username, *basic_info) = user
        profile = SteamUserProfile.objects.all().values_list('personaname', 'profileurl')[0]
        rows.append((username, profile[0], *basic_info, profile[1]))
    
    # writing the sheet
    row_num = 0
    for row in rows:
        row_num += 1
        for col_num in range(len(columns)):
            sheet.write(0, col_num, columns[col_num], styles['header']) # Sheet header, first row
            sheet.write(row_num, col_num, row[col_num], styles[columns[col_num]]) # Sheet body, other rows

    book.save(response) # saving the workbook

    return response # excel file will automatically get downloaded
