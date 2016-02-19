import c4d
from c4d import gui
#Welcome to the world of Python

#!! This only works on the channels that have changing animation. So i.e. if only the xchannel is animated but the target object is in a different position then it will only copy across the x animation
def main():
    
    gui.MessageDialog('Hello World!')
    
    obj = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)
    
    source = obj[0]
    target = obj[1]

    print "Source: %s \n" %source
    print "Target: %s \n" %target

    if obj != None:

    # look if there is already a track
      track = source.FindCTrack(c4d.ID_BASEOBJECT_REL_POSITION)
      
      print "Track: %s \n" %track

      # if not create the track
      if track == None:
         print "Sorry - no track found \n"
      
      curve = track.GetCurve()

      target.InsertTrackSorted(track.GetClone())
      
if __name__=='__main__':
    main()