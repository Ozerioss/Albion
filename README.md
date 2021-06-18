# Albion helper script

Should allow running these main features ( eventually in a GUI menu style )
* Trigger an action on a sound cue
* Trigger an action on a visual cue
* Trigger an alert when an enemy approaches / dismounts near your character 
  (useful for afk/watching on another screen)
  
  
  
# Current problems

The solution using `pyautogui.locateOnScreen()` is unfortunately not accurate enough
and does not detect some of the healthbars especially if they're overlapping with some UI

Even with a low value in confidence it did not give successful results.
After many tests tuning the confidence parameter, I have landed on the value `confidence=0.773` which had the best result in 
detecting healthbars in ideal scenarios ( ie: no UI/HUD covering it )

So the next iteration is going to be testing with OpenCV, which allows us to choose different algorithms for matching an image inside of another one, which could 
result in better / faster matching.

There's also a solution that could be tested, which would rely on checking only the edges of the screen to reduce as much as possible the false positives. It would also allow for testing a new technique which would be checking the hue of the pixels ( ie : detect the healthbar by scanning all edges of the screen and checking the RGB value)
This solution can also bring a lot of false positives but should be tested and documented nonetheless.
