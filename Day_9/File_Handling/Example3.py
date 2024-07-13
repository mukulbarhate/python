import shutil

#  Python allows you to quickly create zip/tar archives.
# Following command will zip entire directory

# here "myzip.zip" will be created of the current working directory (. is given) and that zip file will be stored in the current working directory itself.
shutil.make_archive("myzip","zip","D:\PG-DBDA CDAC\Python\lectures\Day_9\File_Handling\With_Info")
# shutil.make_archive("withInfo","zip","D:\PG-DBDA CDAC\Python\lectures\Day_9\File_Handling\With_Info")
print("Done")
print(shutil.get_unpack_formats())
