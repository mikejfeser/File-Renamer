#import os module
import os

#use the os.chdir method to change the working directory to the specific path you want to edit files
#note the direction of the slashes--forward slashes for path names
os.chdir('C:/Users/you/FolderThatYouWantToEdit')

#create a for loop to list out the files in the given directory
for f in os.listdir():
	f_name, f_ext = os.path.splitext(f)
	if 'NEWTEXT_' in f_name:
        	print('already there')
		#instead of print, you can also use pass
   	 else:
       	 	os.rename(f, 'NEWTEXT_' + f_name + f_ext)
	#this if-else operation means if the file in the directory already has the 'NEWTEXT' in the filename 
	#it will tell you with 'already there' and won't add the change again
  
#we use os.path.splitext to split the names of each file into its main filename and the extension it uses
#use os.rename to add the new word into the filename--putting in front of f_name will add to beginning, putting it after will add to end 
