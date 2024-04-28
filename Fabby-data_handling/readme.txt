Basic Instructions on using the tools in the folder 

    #The files in this kit are used to convert, split and visualise data

    #The python files are used to handle all data , use 'python' instead of 'python3' at the prompt to avoid any library issues

    #The 'speed_vs_time.py' and 'alt_vs_time.py' both use matplot library for plots, their normal behaviour is to open as a different window if run as a program, in the end if executed in a notebook.They read a csv file and look for headers speed and time for speed_vs_time and alt and time for alt_vs_time the time is in the format 'YYYY/MM/DD HH:MM:SS+ZZ'
    
    #'generate_map.py' uses folium to draw a polyline on a map using the csv file containing longitude and latitude as headers named lon and lat.The output file is named 'trip_map.html'.Usually in JupyterLab , the map won't show until the 'Trust HTML' button on the top left side of the html tab is clicked.
'GPRMC.py' is used to obtain a csv file (time_coordinate_speed.csv) from a txt file (track.txt) containing nmea sentences , the program searches for RMC sentences (starting with $GPRMC) , parses them and saves speed , coorddinates and time to the output csv file


The Files being processed by the programs are , at the moment , hardcoded into the programs, and assigned to the variable 'filename' in case of 'generate_map.py', system arguments will be introduced in next updates
