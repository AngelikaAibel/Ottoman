#can go through hierarchy perhaps, but need a way to store the found controllers in a recursive function(global variable??)

import c4d
from c4d import gui
#Welcome to the world of Python

def copy_animation(source, target):
    

 #   doc.SetSelection(source, c4d.SELECTION_NEW) 
 #   doc.SetSelection(target, c4d.SELECTION_ADD)  


   # print "Source: %s \n" %source
   # print "Target: %s \n" %target


    # look if there is already a track
    tracks = source.GetCTracks()

   # print "Track: %s \n" %tracks

      # if not create the track
    if tracks == None:
      print "Sorry - no tracks found \n"

    for track in tracks:
        #print "Done\n"
        curve = track.GetCurve()
        target.InsertTrackSorted(track.GetClone())

def recurse_hierarchy(op, store_controllers):
    
    
    while op:
        
        #print "Object working on: %s" %op
        object_name = op.GetName()
        if op.GetType() == 5101:
            #print op
            store_controllers.append(op)
        
        recurse_hierarchy(op.GetDown(),store_controllers)
        op = op.GetNext()
        
    return store_controllers

def main():
    gui.MessageDialog('Hello World!')

    object = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)
    
    source = object[0]
    target = object[1]   
   # print source
   # print source.GetName()
   
    store_source_controllers = []
    store_target_controllers = []

    if doc:
        source_controllers = recurse_hierarchy(source, store_source_controllers)
        target_controllers = recurse_hierarchy(target, store_target_controllers)


    print "ControllerList length is: %s \n" %str(len(source_controllers))

    print source_controllers

    if len(source_controllers) == len(target_controllers):
       for s_con,t_con in zip(source_controllers, target_controllers):
          # print "%s - %s \n" %(source,target)    
           copy_animation(s_con, t_con)
    else:
        print "Sorry \n"

        
if __name__=='__main__':
    main()
