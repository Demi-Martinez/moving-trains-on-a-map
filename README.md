<h2>Python desktop application that monitors trains moving on map</h2>

This is an old prototype I developeed for the French Railways (SNCF).

This is a simple desktop application in Python that move some moving thick lines over a fixed map. The thick lines simulate train that depart and arrive following their timetable.

The architecture of this app is:
- A a file with all time tables and paths in some format that it's easy to produce or and export from another source, like XML.
- B a python process that gets the time and paths and produces some coordinates that go on a map.
- C some visualization process, in python as well, that support showing a group of dots on a map.

The second B part was of course that most interesting, I tried two approaches multithreading and a single process that once updating all trains at regular intervals.

This prototype has never seen production because the client polled a possible audience of train monitors and they didn't like. 

