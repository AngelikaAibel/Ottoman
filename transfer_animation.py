import c4d
from c4d import gui

def copy_animation(source, target):

    # look if there is a track
    tracks = source.GetCTracks()

    # if not create the track
    if tracks == None:
      print "Sorry - no tracks found \n"

    for track in tracks:
        curve = track.GetCurve()
        target.InsertTrackSorted(track.GetClone())

def recurse_hierarchy(op, store_controllers):
    
    while op:
        #Check if there is a character controller tag for object => then it is a controller
        for i in op.GetTags():
            if i.GetType() == 1022113:
               store_controllers.append(op)
        
        recurse_hierarchy(op.GetDown(),store_controllers)
        op = op.GetNext()
        
    return store_controllers

def main():
    #get active objects
    object = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)
    
    source = object[0]
    target = object[1]   

    store_source_controllers = []
    store_target_controllers = []

    #find controllers
    if doc:
        source_controllers = recurse_hierarchy(source, store_source_controllers)
        target_controllers = recurse_hierarchy(target, store_target_controllers)


    print "ControllerList length is: %s \n" %str(len(source_controllers))

    if len(source_controllers) == len(target_controllers):
       for s_con,t_con in zip(source_controllers, target_controllers):
          # print "%s - %s \n" %(source,target)    
           copy_animation(s_con, t_con)
    else:
        print "Sorry there has been an error - the rig hierarchies are not the same\n"

        
if __name__=='__main__':
    main()
