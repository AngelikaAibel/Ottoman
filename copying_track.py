import c4d
from c4d import gui
#Welcome to the world of Python

#get all the tracks so the target will be put into the same position (improvement from v3)

def main():

    gui.MessageDialog('Hello World!')
    
    obj = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)
    
    source = obj[0]
    target = obj[1]

    print "Source: %s \n" %source
    print "Target: %s \n" %target

    if obj != None:

    # look if there is already a track
      tracks = source.GetCTracks()
      
      print "Track: %s \n" %tracks

      # if not create the track
      if tracks == None:
         print "Sorry - no tracks found \n"

      for track in tracks:
        curve = track.GetCurve()
      
        target.InsertTrackSorted(track.GetClone())
      
if __name__=='__main__':
    main()