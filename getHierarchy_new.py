#Lets see if changes are tracked
#script to transverse hierarchy
#http://www.cineversity.com/forums/viewthread/1307/

def GetAllObjects(obj, objList):
    if obj is None: return

    #Actions can go here
    objList.append(obj)
    #End Actions
    if (obj.GetDown()):
        GetAllObjects(obj.GetDown(), objList)
    if (obj.GetNext()):
        GetAllObjects(obj.GetNext(), objList)
    return objList

def GoDownHierarchy(obj, stop, objList):
    if obj is None: return
    if obj==stop: return
    
    #Actions can go here
    objList.append(obj)
    #End Actions
    if (obj.GetDown()):
        GoDownHierarchy(obj.GetDown(), stop, objList)
    if (obj.GetNext()):
        GoDownHierarchy(obj.GetNext(), stop, objList)

    return objList


def main():
    emptyList=[]
    allObjs=GetAllObjects(doc.GetFirstObject(), emptyList)
    null=None
    for obj in allObjs:
        name=obj.GetName()
        if len(name.split('_')>0:
            if name.split('_')[-1]=='cpk':
                null=obj
                break

    if null != None:
        emptyList2=[]
        children=GoDownHierarchy(null, null.GetNext(), emptyList2)

    if len(children)>0:
        for id, child in children:
            if id==0:
                doc.SetSelection(children, c4d.SELECTION_NEW)
            else:
                doc.SetSelection(children, c4d.SELECTION_ADD) 