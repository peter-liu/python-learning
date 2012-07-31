class hotkeyer():
    lasttime = 0
    lastkey = ''
    calla = None
    obj = None
    def __init__(self,cal,obje):
        hotkeyer.calla = cal
        hotkeyer.obj = obje
    def OnKeyboardEvent(self,event):
        if event.Key == 'G' and hotkeyer.lastkey =='Lcontrol':
            hotkeyer.calla(self)
            hotkeyer.lastkey = ''
            return False
        if event.Key == 'Lcontrol' != hotkeyer.lastkey:
            hotkeyer.lasttime= event.Time
            hotkeyer.lastkey = 'Lcontrol'
            return True
        if (event.Time - hotkeyer.lasttime) > 150:
            hotkeyer.lastkey = ''
            return True 
