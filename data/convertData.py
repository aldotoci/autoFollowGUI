fileObj = open('/home/yeet/Desktop/PyProjects/autoFollowGUI/data/rowdata.txt', "r") #opens the file in read mode
usernamesToFollow = fileObj.read().splitlines() #puts the file into an array
fileObj.close()