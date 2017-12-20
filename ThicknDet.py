#Boa:Dialog:ThicknDet

#Optical, Copyright (C) 2005  Emanuele Centurioni
#see Optical.py

import wx

def create(parent):
    return ThicknDet(parent)

[wxID_THICKNDET, wxID_THICKNDETBTNCANCEL, wxID_THICKNDETBTNOK, 
 wxID_THICKNDETCHLINK, wxID_THICKNDETCHSELECT, wxID_THICKNDETRBBOTH, 
 wxID_THICKNDETRBR, wxID_THICKNDETRBT, wxID_THICKNDETSPINCTRL1, 
 wxID_THICKNDETSTATICBOX1, wxID_THICKNDETSTATICBOX2, wxID_THICKNDETSTATICBOX3, 
 wxID_THICKNDETSTATICBOX4, wxID_THICKNDETSTATICBOX5, wxID_THICKNDETSTATICBOX6, 
 wxID_THICKNDETSTATICTEXT1, wxID_THICKNDETSTATICTEXT2, 
 wxID_THICKNDETTXTDENSITY, wxID_THICKNDETTXTRANGEMAX, 
 wxID_THICKNDETTXTRANGEMIN, wxID_THICKNDETTXTTHICKNESS, 
] = [wx.NewId() for _init_ctrls in range(21)]

class ThicknDet(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_THICKNDET, name='ThicknDet',
              parent=prnt, pos=wx.Point(321, 146), size=wx.Size(354, 369),
              style=wx.DEFAULT_DIALOG_STYLE, title='Thickness determination')
        self.SetClientSize(wx.Size(354, 369))

        self.btnOK = wx.Button(id=wxID_THICKNDETBTNOK, label='OK', name='btnOK',
              parent=self, pos=wx.Point(224, 272), size=wx.Size(80, 26),
              style=0)
        self.btnOK.Bind(wx.EVT_BUTTON, self.OnBtnOKButton,
              id=wxID_THICKNDETBTNOK)

        self.chSelect = wx.Choice(choices=[], id=wxID_THICKNDETCHSELECT,
              name='chSelect', parent=self, pos=wx.Point(32, 40),
              size=wx.Size(152, 34), style=0)
        self.chSelect.Bind(wx.EVT_CHOICE, self.OnChSelectChoice,
              id=wxID_THICKNDETCHSELECT)

        self.staticBox1 = wx.StaticBox(id=wxID_THICKNDETSTATICBOX1,
              label='Select layer', name='staticBox1', parent=self,
              pos=wx.Point(16, 16), size=wx.Size(184, 72), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_THICKNDETSTATICBOX2,
              label='Fit on ...', name='staticBox2', parent=self,
              pos=wx.Point(16, 256), size=wx.Size(160, 100), style=0)

        self.rbR = wx.RadioButton(id=wxID_THICKNDETRBR, label='Reflectance',
              name='rbR', parent=self, pos=wx.Point(32, 272), size=wx.Size(116,
              28), style=0)
        self.rbR.SetValue(True)

        self.rbT = wx.RadioButton(id=wxID_THICKNDETRBT, label='Transmittance',
              name='rbT', parent=self, pos=wx.Point(32, 296), size=wx.Size(128,
              28), style=0)
        self.rbT.SetValue(False)

        self.rbBoth = wx.RadioButton(id=wxID_THICKNDETRBBOTH, label='Both',
              name='rbBoth', parent=self, pos=wx.Point(32, 320),
              size=wx.Size(116, 28), style=0)
        self.rbBoth.SetValue(False)

        self.txtThickness = wx.TextCtrl(id=wxID_THICKNDETTXTTHICKNESS,
              name='txtThickness', parent=self, pos=wx.Point(224, 48),
              size=wx.Size(80, 26), style=0, value='textCtrl1')
        self.txtThickness.Enable(False)

        self.staticBox3 = wx.StaticBox(id=wxID_THICKNDETSTATICBOX3,
              label='Thickness (A)', name='staticBox3', parent=self,
              pos=wx.Point(208, 16), size=wx.Size(128, 72), style=0)

        self.spinCtrl1 = wx.SpinCtrl(id=wxID_THICKNDETSPINCTRL1, initial=1,
              max=16, min=0, name='spinCtrl1', parent=self, pos=wx.Point(288,
              208), size=wx.Size(15, 26), style=wx.SP_ARROW_KEYS)
        self.spinCtrl1.Show(True)
        self.spinCtrl1.Enable(True)
        self.spinCtrl1.Bind(wx.EVT_SPINCTRL, self.OnSpinCtrl1Spinctrl,
              id=wxID_THICKNDETSPINCTRL1)

        self.staticBox4 = wx.StaticBox(id=wxID_THICKNDETSTATICBOX4,
              label='Search range (A)', name='staticBox4', parent=self,
              pos=wx.Point(16, 176), size=wx.Size(320, 72), style=0)

        self.txtRangeMin = wx.TextCtrl(id=wxID_THICKNDETTXTRANGEMIN,
              name='txtRangeMin', parent=self, pos=wx.Point(72, 208),
              size=wx.Size(80, 26), style=0, value='textCtrl1')
        self.txtRangeMin.Enable(False)

        self.txtRangeMax = wx.TextCtrl(id=wxID_THICKNDETTXTRANGEMAX,
              name='txtRangeMax', parent=self, pos=wx.Point(192, 208),
              size=wx.Size(80, 26), style=0, value='textCtrl1')
        self.txtRangeMax.Enable(False)

        self.btnCancel = wx.Button(id=wxID_THICKNDETBTNCANCEL, label='Cancel',
              name='btnCancel', parent=self, pos=wx.Point(224, 312),
              size=wx.Size(80, 26), style=0)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.OnBtnCancelButton,
              id=wxID_THICKNDETBTNCANCEL)

        self.staticText1 = wx.StaticText(id=wxID_THICKNDETSTATICTEXT1,
              label='From', name='staticText1', parent=self, pos=wx.Point(24,
              211), size=wx.Size(38, 20), style=0)

        self.staticText2 = wx.StaticText(id=wxID_THICKNDETSTATICTEXT2,
              label='to', name='staticText2', parent=self, pos=wx.Point(165,
              211), size=wx.Size(14, 20), style=0)

        self.chLink = wx.Choice(choices=[], id=wxID_THICKNDETCHLINK,
              name='chLink', parent=self, pos=wx.Point(32, 120),
              size=wx.Size(152, 34), style=0)
        self.chLink.Bind(wx.EVT_CHOICE, self.OnChLinkChoice,
              id=wxID_THICKNDETCHLINK)

        self.staticBox5 = wx.StaticBox(id=wxID_THICKNDETSTATICBOX5,
              label='Link to layer', name='staticBox5', parent=self,
              pos=wx.Point(16, 96), size=wx.Size(184, 72), style=0)

        self.txtDensity = wx.TextCtrl(id=wxID_THICKNDETTXTDENSITY,
              name='txtDensity', parent=self, pos=wx.Point(224, 120),
              size=wx.Size(80, 26), style=0, value='1')

        self.staticBox6 = wx.StaticBox(id=wxID_THICKNDETSTATICBOX6,
              label='Relative density', name='staticBox6', parent=self,
              pos=wx.Point(208, 96), size=wx.Size(128, 72), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

        self.parent=parent
        self.Structure=parent.Structure
        #self.CurDir=parent.CurDir
        #self.IndexDir=parent.IndexDir
        #self.StructureName=parent.StructureName
        self.spinCtrl1.SetValue(self.parent.StoreThickDet[2])
        self.UpdateFields(self.parent.StoreThickDet[0],self.parent.StoreThickDet[1])
        if self.parent.StoreThickDet[3]=="R":
            self.rbR.SetValue(True)
        elif self.parent.StoreThickDet[3]=="T":
            self.rbT.SetValue(True)
        else:
            self.rbBoth.SetValue(True)    
        self.txtDensity.SetValue(str(self.parent.StoreThickDet[4]))
                
    def UpdateFields(self,j,l):
        self.chSelect.Clear()
        for i in range(1,len(self.Structure)-1):
            self.chSelect.Append(str(i)+" "+self.Structure[i][0])
        self.chSelect.Select(j)
        self.chLink.Clear()
        self.chLink.Append("None")
        for i in range(1,len(self.Structure)-1):
            if i!=j+1:
                self.chLink.Append(str(i)+" "+self.Structure[i][0])
        self.chLink.Select(l)

        if l!=0:
            self.txtDensity.Enable(True)
        else:
            self.txtDensity.Enable(False)
        
        self.txtThickness.SetValue(self.Structure[j+1][9])
        Thickness=int(float(self.Structure[j+1][9]))
        self.txtRangeMax.SetValue(str(Thickness-1+2*2**self.spinCtrl1.GetValue()))
        self.txtRangeMin.SetValue(str(Thickness-2*2**self.spinCtrl1.GetValue()))

    def OnChSelectChoice(self, event):
        j=int(self.chSelect.GetSelection())
        k=int(self.chLink.GetSelection())
        self.UpdateFields(j,k)

    def OnSpinCtrl1Spinctrl(self, event):
        Thickness=int(float(self.txtThickness.GetValue()))
        self.txtRangeMax.SetValue(str(Thickness-1+2*2**self.spinCtrl1.GetValue()))
        self.txtRangeMin.SetValue(str(Thickness-2*2**self.spinCtrl1.GetValue()))

    def OnBtnCancelButton(self, event):
        self.parent.Dialog=["C"]
        self.Close()

    def OnBtnOKButton(self, event):
        j=int(self.chSelect.GetSelection())+1
        k=int(self.chLink.GetSelection())
        self.parent.StoreThickDet[0]=j-1
        self.parent.StoreThickDet[1]=k
        if k>=j:
            k=k+1
        range=self.spinCtrl1.GetValue()
        self.parent.StoreThickDet[2]=range
        if self.rbR.GetValue()==True:
            FitOn="R"
        elif self.rbT.GetValue()==True:
            FitOn="T"
        else:
            FitOn="RT"
        self.parent.StoreThickDet[3]=FitOn
        Density=float(self.txtDensity.GetValue())
        self.parent.StoreThickDet[4]=Density
        self.parent.Dialog=[FitOn,j,range,k,Density]
        self.Close()

    def OnChLinkChoice(self, event):
        j=int(self.chSelect.GetSelection())
        k=int(self.chLink.GetSelection())
        self.UpdateFields(j,k)




        
        


