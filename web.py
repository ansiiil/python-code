file=open("index.html","w")
title=input("enter your site title:")
heading=input("enter your site heading:")
para=input("enter your site content:")
color=input("enetr your background color:")
file.write("""
<html>
           <head>
            <title%s</title>
           <body bgcolor='%s'>
                 <h1>%s</h1>
                 <p>%s</p>
            </body> 
</html>
"""%(title,color,heading,para))
print("webpage created succesfully")
