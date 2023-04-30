from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.template import loader
# Create your views here.


def html_generator(a):
    file = open('output_html.html', 'rb')
    response = FileResponse(file)

    return response
    # return FileResponse(as_attachment=True, filename="output_html.html")


def home_view(request):
    print('The request method is:', request.method)
    print(request.POST)
    if (request.method == "POST"):
        input_field = request.POST['text_box']
        print('The POST data is:', input_field)
        output = input_field
        print("printing:........\n", input_field, "\n")

        head_size = request.POST['head_size']
        text_size = request.POST['text_size']
        text_color = request.POST['text_color']
        head_color = request.POST['head_color']
        lines = output.splitlines()
        # heading
        lines[0] = f'''<br><h{head_size} style="color: {head_color};">{lines[0]}</h{head_size}>'''
        output1 = lines[0]+"\n"
        # poem mode  <p style="font-size: "></p>
        str1 = ""
        for i in lines[1:]:
            str1 = str1 + f''' {i} <br>\n'''
        str1 = f'''<p style="font-size:{text_size}px;color:{text_color}">'''+str1+"</p>"
        print(str1)
        output1 = output1 + str1
        with open('output_html.html', 'w') as f:
            f.write('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>TXT-TO-HTML</title>
  </head>
  <body>'''+output1+"</body></html>")

        return render(request, "home.html", {'output': output1})

    return render(request, "home.html", {'output': "OUTPUT SCREEN"})
