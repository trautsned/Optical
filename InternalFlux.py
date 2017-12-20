#Boa:Dialog:InternalFlux

#Optical, Copyright (C) 2005  Emanuele Centurioni
#see Optical.py

import wx

def create(parent):
    return InternalFlux(parent)

[wxID_INTERNALFLUX, wxID_INTERNALFLUXBTNABSORPTION, 
 wxID_INTERNALFLUXBTNCANCEL, wxID_INTERNALFLUXBTNFLUX, 
 wxID_INTERNALFLUXCHSELECT, wxID_INTERNALFLUXSTATICBOX1, 
 wxID_INTERNALFLUXSTATICBOX2, wxID_INTERNALFLUXSTATICBOX3, 
 wxID_INTERNALFLUXSTATICBOX4, wxID_INTERNALFLUXSTATICBOX5, 
 wxID_INTERNALFLUXTXTPOSITION, wxID_INTERNALFLUXTXTTHICKNESS, 
] = [wx.NewId() for _init_ctrls in range(12)]

class InternalFlux(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_INTERNALFLUX, name='InternalFlux',
              parent=prnt, pos=wx.Point(355, 215), size=wx.Size(438, 277),
              style=wx.DEFAULT_DIALOG_STYLE,
              title='Internal Absorption and Energy Flux Spectra')
        self.SetClientSize(wx.Size(438, 277))

        self.chSelect = wx.Choice(choices=[], id=wxID_INTERNALFLUXCHSELECT,
              name='chSelect', parent=self, pos=wx.Point(40, 48),
              size=wx.Size(152, 34), style=0)
        self.chSelect.Bind(wx.EVT_CHOICE, self.OnChSelectChoice,
              id=wxID_INTERNALFLUXCHSELECT)

        self.btnAbsorption = wx.Button(id=wxID_INTERNALFLUXBTNABSORPTION,
              label='Compute', name='btnAbsorption', parent=self,
              pos=wx.Point(64, 144), size=wx.Size(80, 26), style=0)
        self.btnAbsorption.Bind(wx.EVT_BUTTON, self.OnBtnAbsorptionButton,
              id=wxID_INTERNALFLUXBTNABSORPTION)

        self.btnFlux = wx.Button(id=wxID_INTERNALFLUXBTNFLUX, label='Compute',
              name='btnFlux', parent=self, pos=wx.Point(296, 216),
              size=wx.Size(80, 26), style=0)
        self.btnFlux.Bind(wx.EVT_BUTTON, self.OnBtnFluxButton,
              id=wxID_INTERNALFLUXBTNFLUX)

        self.txtPosition = wx.TextCtrl(id=wxID_INTERNALFLUXTXTPOSITION,
              name='txtPosition', parent=self, pos=wx.Point(264, 160),
              size=wx.Size(88, 26), style=0, value='0')

        self.btnCancel = wx.Button(id=wxID_INTERNALFLUXBTNCANCEL,
              label='Cancel', name='btnCancel', parent=self, pos=wx.Point(64,
              216), size=wx.Size(80, 26), style=0)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.OnBtnCancelButton,
              id=wxID_INTERNALFLUXBTNCANCEL)

        self.txtThickness = wx.TextCtrl(id=wxID_INTERNALFLUXTXTTHICKNESS,
              name='txtThickness', parent=self, pos=wx.Point(288, 48),
              size=wx.Size(88, 26), style=0, value='textCtrl2')
        self.txtThickness.Enable(False)

        self.staticBox1 = wx.StaticBox(id=wxID_INTERNALFLUXSTATICBOX1,
              label='Select layer', name='staticBox1', parent=self,
              pos=wx.Point(24, 24), size=wx.Size(200, 64), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_INTERNALFLUXSTATICBOX2,
              label='Thickness (A)', name='staticBox2', parent=self,
              pos=wx.Point(272, 24), size=wx.Size(120, 64), style=0)

        self.staticBox3 = wx.StaticBox(id=wxID_INTERNALFLUXSTATICBOX3,
              label=' Position in layer (A)', name='staticBox3', parent=self,
              pos=wx.Point(256, 136), size=wx.Size(160, 64), style=0)

        self.staticBox4 = wx.StaticBox(id=wxID_INTERNALFLUXSTATICBOX4,
              label='Layer absorption', name='staticBox4', parent=self,
              pos=wx.Point(24, 112), size=wx.Size(160, 80), style=0)

        self.staticBox5 = wx.StaticBox(id=wxID_INTERNALFLUXSTATICBOX5,
              label='Energy Flux', name='staticBox5', parent=self,
              pos=wx.Point(240, 112), size=wx.Size(184, 152), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        self.parent=parent
        self.Structure=parent.Structure
        #self.CurDir=parent.CurDir
        #self.IndexDir=parent.IndexDir
        #self.StructureName=parent.StructureName
        self.parent.Dialog=["C"]
        self.UpdateFields(self.parent.StoreEFlux[0])
        self.txtPosition.SetValue(self.parent.StoreEFlux[1])

    def UpdateFields(self,j):
        self.chSelect.Clear()
        for i in range(1,len(self.Structure)-1):
            self.chSelect.Append(str(i)+" "+self.Structure[i][0])
        self.chSelect.Select(j)
        self.txtThickness.SetValue(self.Structure[j+1][9])

    def OnBtnAbsorptionButton(self, event):
        j=int(self.chSelect.GetSelection())+1
        self.parent.Dialog=["A",j]
        self.Close()
        self.parent.StoreEFlux[0]=j-1
        self.parent.StoreEFlux[1]=self.txtPosition.GetValue()

    def OnBtnFluxButton(self, event):
        j=int(self.chSelect.GetSelection())+1
        x=float(self.txtPosition.GetValue())/float(self.txtThickness.GetValue())
        self.parent.Dialog=["E",j,x]
        self.Close()
        self.parent.StoreEFlux[0]=j-1
        self.parent.StoreEFlux[1]=self.txtPosition.GetValue()


    def OnBtnCancelButton(self, event):
        self.parent.Dialog=["C"]
        self.Close()

    def OnChSelectChoice(self, event):
        j=int(self.chSelect.GetSelection())
        self.UpdateFields(j)



        
