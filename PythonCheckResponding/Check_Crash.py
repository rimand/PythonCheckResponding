import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from linenotipy import Line
line = Line(token='4nQRXaFFmESdQTv1dU0ItnPSpwuQBmggtDGsVg3ZbVe')

print("========[ Check_Crash ]========")

patterns = ["*"]
ignore_patterns = None
ignore_directories = False
case_sensitive = True

def on_modified(event):
    print("on_modified")
    pass

def on_created(event):
    print("on_created")
    line.post(message='Touchdesigner Crash', stickerPackageId=789, stickerId=10881)
    pass

my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
my_event_handler.on_created = on_created
# my_event_handler.on_modified = on_modified

path = "./"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()


while True:
    pass