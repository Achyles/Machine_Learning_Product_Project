# Web scraper for the project

## CU_Course_Directory

A simple web scraper for CU Course Directory for Spring 2018 Courses
Can be modified for other terms as well.

<<<<<<< HEAD
The output for the COMS STAT IEOR deparment (in UTF-8) is in [CU_Course_Directory_info](./CU_Course_Directory_info). See the [windows_1252](./CU_Course_Directory_info/Encoding_windows_1252) folder for better result since the directory is encoded in "windows-1252". Make sure to open csv files with according encoding.
=======
The output for the COMS STAT IEOR deparments in [CU_Course_Directory_info](./CU_Course_Directory_info)
>>>>>>> ae56f9e1bb825f175f86d194eb3cf384bc9fb248


Usage sample, from terminal run:

``` bash
    python CU_Course_Directory.py 
    
    Please enter a list of four-letter department abbreviations (e.g. COMS, HIST, MATH) to get csv files of course information.
    Files will be stored by default in the current directory, you can also change the directory with "-d" flag + directory:

    COMS STAT IEOR -d out/
```

    
