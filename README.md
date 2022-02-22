# README
## Description 
When i decide to make a fan made poster for a movie or tv show i always need materials to work with , so what i did previosuly is that i searched for the movie on google , in which photos where mostlikely low-res , or took screenshots from the movie or tv show, which also mostlikely be low-res .

That's where **Poster_Maker** comes in .

## Functionallity
* What it does is scrape **IMDB** and download all the images in the photos section , And , simultaneously , scrape **IMB AWARDS** and download all available posters for reference
* It also makes a complete ready to use directory with folders for
    * *Materials* ( with IMDB images inside)
    * *Previous Posters* ( with IMB posters inside) 
    * *Finals* folder for you when you complete your project and put the end results in
    * *PSD* file created for you to start working immediately
* the scrapers run at the same time to save as much time as possible
* the images download from IMDB are in the highest quality possible

## How to run
to run the program just run the *run.exe* file either you have or don't have python installed this should work for you 

if that didn't work do the following :-

1. open your *cmd* or *terminal* > Navigate to the project folder
1. type :-

    * .venv\Scripts\activate.bat
    * pip install -r requirments.txt

## To install the packeges
in the termianl type pip install -r requirments.txt


## Notes
if you want to change the folder in which the directories are created and the photos being downloaded :-

* Open the file *Manager.py*
* Change the path value of the variable *MAIN_FOLDER* to your liking

---
### if you have any questions feel free to start an issue

    
