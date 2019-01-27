![Screenshot](https://i.imgur.com/ByrrQJA.png)


Snip is a extension for Albert Launcher. It is based on 'SCReenshOT utility' (by Benedict Dudel) which uses `scrot`. 'Snip' does use the utility gnome-screenshot instead.

## Features
* Triggered with `ss `
* Default action: draw a rectacle with the mouse and get that screenshot on clipboard.
* You can select from these options:
	* Snip screen: Capture to the clipboard _[default action]_
	* Snip screen: Capture and save in _Pictures_
	* Full screenshot: Take screenshot of whole screen
 	* Full screenshot: Take screenshot without showing the pointer
	* Full screenshot: Take screenshot of actual window only

'Full screenshot' options auto save the capture to the 'Pictures' folder. Its default action its the first one. And for 'Snip screen' when capture to the clipboard (default) it's doesn't auto save, it's for paste it.  
[**Watch it in action**](https://i.imgur.com/CO1Qh8L.mp4)

### Get it
```
git clone https://github.com/thepante/albert-snip.git "~/.local/share/albert/org.albert.extension.python/modules/snip"
```
