output = '''NATURE:
If I could turn back time and rewrite every line
If only I could, but baby, I can't'''
head_size = 1
text_size = 20
text_color = "black"
head_color = "green"
lines = output.splitlines()
# heading
lines[0] = f'''<br><h{head_size} style="color: {head_color};">{lines[0]}</h{head_size}>'''
print(lines[0])
# poem mode  <p style="font-size: "></p>
str1 = ""
for i in lines[1:]:
    str1 = str1 + f''' {i} <br>\n'''
str1 = f'''<p style="font-size:{text_size};color:{text_color}">'''+str1+"</p>"
print(str1)
