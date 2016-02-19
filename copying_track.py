import c4d
from c4d import gui
#Welcome to the world of Python


def main():
    
    gui.MessageDialog('Hello World!')
    
    obj = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)
    
    source = obj[0]
    target = obj[1]
    
    if activeObject != None:
            
    # look if there is already a track
      track = obj.FindCTrack(c4d.ID_BASEOBJECT_REL_POSITION)
      
      # if not create the track
      if track == None:
         print "Sorry - no track found \n"
         #track=c4d.CTrack(activeObject, c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, 0)))
         #activeObject.InsertTrackSorted(track)