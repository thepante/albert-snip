![Screenshot](https://i.imgur.com/ByrrQJA.png)

Snip is a extension for [Albert Launcher](https://github.com/albertlauncher/albert). It is based on 'SCReenshOT utility' (by Benedict Dudel) which uses `scrot`. 'Snip' does use the utility gnome-screenshot instead.

## Features
Triggered with `ss `. The default action (sequence <kbd>ss</kbd> <kbd>Space</kbd> <kbd>Enter</kbd>) is to draw a rectacle with the mouse and get that screenshot on clipboard.

**You can also select between those options:**
 * Snip screen → Capture to clipboard _[default action]_
 * Snip screen → Capture and save in `Pictures`
 * Full screenshot → Take a fullscreen screenshot
 * Full screenshot → Take screenshot without showing the pointer
 * Full screenshot → Take screenshot of actual window only

> 'Full screenshot' options auto saves the capture to 'Pictures' folder. Each method default action its the first one. 'Snip screen' default method (capture to clipboard) doesn't auto save, it is for paste the snip somewhere.

[**Watch it in action**](https://i.imgur.com/CO1Qh8L.mp4) - First part is a snip and pasted on Telegram, then is a window screenshot.

## Installation
```
git clone https://github.com/thepante/albert-snip.git ~/.local/share/albert/org.albert.extension.python/modules/snip
```

