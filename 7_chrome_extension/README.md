# A Chrome Extension that Displays IMDb Scores on Netflix

## Description and [YouTube Tutorial]()
I often found myself opening IMDb to check reviews before starting a new Netflix tv-show or movie. After finally getting fed-up with the sub-optimal process, I built this chrome extension. Now, I don't have to open numerous tabs to search through reviews anymore!

It is important to note that this code will not work as-is because I removed my API key. If you are interested in learning about the extension's implementation and would like to get things up and running, then please checkout this **[YouTube tutorial]()** where I describe how the extension works.

Note: If you are completely new to chrome extensions, then I would advise that you start off by watching the chrome extensions series on YouTube made by `the coding train`. I used his videos as a starting point.

## What the Extension Does
Finds movie/tv show that closest resembles the title displayed on Netflix when hovering over a selection, fetches the IMDb score from the OMDbAPI, and adds a `div` to display it. It is far from perfect - the extension has few error checks, it occasionally fails silently, and the UI is pretty shoddy - but it gets the job done. Please feel free to take it and augment it as you see fit. Would love to see what you guys/gals can do!

## Example Pictures
- [Stranger Things - 8.9](https://github.com/TeluguGameboy/youtube/tree/master/7_chrome_extension/stranger_things.png)
- [Sherlock - 9.1](https://github.com/TeluguGameboy/youtube/tree/master/7_chrome_extension/sherlock.png)

## Resources Used
- Got IMDb movie scores from [OMDbAPI](http://www.omdbapi.com/)
- Learned about Chrome extensions popups using the Coding Train's [tutorial series](https://www.youtube.com/watch?9=&v=kP-UmHrxCYk)
