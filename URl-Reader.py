# Welcome To URL-Reader 1.0V With Python Language(Github:DinethGR)
#=================================================================

#Import The URL Reader Library 
import urllib.request

#Enter The URL To Open
Page = urllib.request.urlopen("https://github.com/")

#Decode & Read The URL
Text = Page.read().decode("UTF-8")

#Print The URl After Reading 
print(Text)

#=================================================================