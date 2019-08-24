# A Chrome Extension that Displays IMDb Scores on Netflix

## Description
I always found myself opening IMDb way too often to check reviews before starting a new Netflix tv show or movie. Eventually, I got fed up with this sub optimal process. I decided to build this chrome extension so I don't have to open numerous tabs to search through reviews anymore.

It is important to note that this code will not work as-is because I removed my API key. If you are interested in learning about how to use this extension, then please checkout this **[YouTube tutorial]()** where I describe how the extension works.

Note: If you are completely new to chrome extensions, then I would advise that you start off by watching the chrome extensions series on YouTube made by `the coding train`. I used his videos as a starting point.

## What the Extension Does
Finds movie/tv show that closest resembles the title displayed on Netflix when hovering over a selection, fetches the IMDb score from the OMDbAPI, and adds a `div` to display it. It is far from perfect - the extension has few error checks, it occasionally fails silently, and the UI is pretty shoddy - but it gets the job done. Please feel free to take it and augment it as you see fit. Would love to see what you guys/gals can do!

## Examples
![](https://github.com/TeluguGameboy/youtube/tree/master/7_chrome_extension/stranger_things.png | width=250)
![](https://github.com/TeluguGameboy/youtube/tree/master/7_chrome_extension/death_note.png | width=250)

## Resources Used
- Got IMDb movie scores from [OMDbAPI](http://www.omdbapi.com/)
- Learned about Chrome extensions popups using the Coding Train's [tutorial series](https://www.youtube.com/watch?9=&v=kP-UmHrxCYk)
