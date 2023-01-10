open("name of file/file path on this PC", "r") - read or if not found - error.
open("xxx.txt", "w") - write access, clears the file contents, if not found - creates a new file.
open("xxx.txt, "a") - write only but it file content is left inact, new data is appended to the end of the existing content. If not found - creates a new file.
open("xxx.txt","w+/r+/a+") - read and write.   
