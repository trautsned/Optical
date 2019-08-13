#Boa:Dialog:EdtStructure

#Optical, Copyright (C) 2005  Emanuele Centurioni
#see Optical.py

import wx
from copy import deepcopy
from functions import *

def create(parent):
    return EdtStructure(parent)

[wxID_EDTSTRUCTURE, wxID_EDTSTRUCTUREBTNBROWSE1, wxID_EDTSTRUCTUREBTNBROWSE2, 
 wxID_EDTSTRUCTUREBTNBROWSE3, wxID_EDTSTRUCTUREBTNCANCEL, 
 wxID_EDTSTRUCTUREBTNINSERT, wxID_EDTSTRUCTUREBTNOK, 
 wxID_EDTSTRUCTUREBTNREMOVE, wxID_EDTSTRUCTUREBTNSAVEEMA, 
 wxID_EDTSTRUCTURECHKINCOHERENT, wxID_EDTSTRUCTURECHSELECT, 
 wxID_EDTSTRUCTURESTATICBOX1, wxID_EDTSTRUCTURESTATICBOX10, 
 wxID_EDTSTRUCTURESTATICBOX2, wxID_EDTSTRUCTURESTATICBOX3, 
 wxID_EDTSTRUCTURESTATICBOX4, wxID_EDTSTRUCTURESTATICBOX5, 
 wxID_EDTSTRUCTURESTATICBOX6, wxID_EDTSTRUCTURESTATICBOX7, 
 wxID_EDTSTRUCTURESTATICBOX8, wxID_EDTSTRUCTURESTATICBOX9, 
 wxID_EDTSTRUCTURESTATICTEXT1, wxID_EDTSTRUCTURESTATICTEXT2, 
 wxID_EDTSTRUCTURESTATICTEXT3, wxID_EDTSTRUCTURETXTFILENAME1, 
 wxID_EDTSTRUCTURETXTFILENAME2, wxID_EDTSTRUCTURETXTFILENAME3, 
 wxID_EDTSTRUCTURETXTFRACTION1, wxID_EDTSTRUCTURETXTFRACTION2, 
 wxID_EDTSTRUCTURETXTFRACTION3, wxID_EDTSTRUCTURETXTNAME, 
 wxID_EDTSTRUCTURETXTROUGH, wxID_EDTSTRUCTURETXTSTRNAME, 
 wxID_EDTSTRUCTURETXTTHICKNESS, 
] = [wx.NewId() for _init_ctrls in range(34)]

class EdtStructure(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_EDTSTRUCTURE, name='EdtStructure',
              parent=prnt, pos=wx.Point(217, 134), size=wx.Size(683, 445),
              style=wx.DEFAULT_DIALOG_STYLE, title='Edit Multilayer')
        self.SetClientSize(wx.Size(683, 445))

        self.chSelect = wx.Choice(choices=[], id=wxID_EDTSTRUCTURECHSELECT,
              name='chSelect', parent=self, pos=wx.Point(16, 40),
              size=wx.Size(208, 29), style=0)
        self.chSelect.Bind(wx.EVT_CHOICE, self.OnChSelectChoice,
              id=wxID_EDTSTRUCTURECHSELECT)
        self.chSelect.Bind(wx.EVT_ENTER_WINDOW, self.OnChSelectEnterWindow)

        self.staticBox2 = wx.StaticBox(id=wxID_EDTSTRUCTURESTATICBOX2,
              label='Name', name='staticBox2', parent=self, pos=wx.Point(8, 88),
              size=wx.Size(128, 56), style=0)

        self.txtName = wx.TextCtrl(id=wxID_EDTSTRUCTURETXTNAME, name='txtName',
              parent=self, pos=wx.Point(16, 112), size=wx.Size(112, 26),
              style=0, value='textCtrl1')

        self.staticBox3 = wx.StaticBox(id=wxID_EDTSTRUCTURESTATICBOX3,
              label='Thickness (A)', name='staticBox3', parent=self,
              pos=wx.Point(152, 88), size=wx.Size(112, 56), style=0)

        self.txtThickness = wx.TextCtrl(id=wxID_EDTSTRUCTURETXTTHICKNESS,
              name='txtThickness', parent=self, pos=wx.Point(160, 112),
              size=wx.Size(88, 26), style=0, value='textCtrl2')

        self.chkIncoherent = wx.CheckBox(id=wxID_EDTSTRUCTURECHKINCOHERENT,
              label='Incoherent', name='chkIncoherent', parent=self,
              pos=wx.Point(320, 104), size=wx.Size(103, 32), style=0)
        self.chkIncoherent.SetValue(False)

        self.staticBox4 = wx.StaticBox(id=wxID_EDTSTRUCTURESTATICBOX4,
              label='Bruggeman Effective Medium Approximation',
              name='staticBox4', parent=self, pos=wx.Point(8, 192),
              size=wx.Size(664, 184), style=0)

        self.txtFilename3 = wx.TextCtrl(id=wxID_EDTSTRUCTURETXTFILENAME3,
              name='txtFilename3', parent=self, pos=wx.Point(280, 320),
              size=wx.Size(280, 26), style=0, value='textCtrl1')

        self.txtFraction2 = wx.TextCtrl(id=wxID_EDTSTRUCTURETXTFRACTION2,
              name='txtFraction2', parent=self, pos=wx.Point(144, 288),
              size=wx.Size(48, 26), style=0, value='textCtrl2')
        self.txtFraction2.Enable(True)

        self.txtFilename1 = wx.TextCtrl(id=wxID_EDTSTRUCTURETXTFILENAME1,
              name='txtFilename1', parent=self, pos=wx.Point(280, 256),
              size=wx.Size(280, 26), style=0, value='textCtrl3')

        self.txtFilename2 = wx.TextCtrl(id=wxID_EDTSTRUCTURETXTFILENAME2,
              name='txtFilename2', parent=self, pos=wx.Point(280, 288),
              size=wx.Size(280, 26), style=0, value='textCtrl4')

        self.txtFraction3 = wx.TextCtrl(id=wxID_EDTSTRUCTURETXTFRACTION3,
              name='txtFraction3', parent=self, pos=wx.Point(144, 320),
              size=wx.Size(48, 26), style=0, value='textCtrl5')

        self.txtFraction1 = wx.TextCtrl(id=wxID_EDTSTRUCTURETXTFRACTION1,
              name='txtFraction1', parent=self, pos=wx.Point(144, 256),
              size=wx.Size(48, 26), style=0, value='textCtrl6')

        self.btnBrowse3 = wx.Button(id=wxID_EDTSTRUCTUREBTNBROWSE3,
              label='Browse', name='btnBrowse3', parent=self, pos=wx.Point(568,
              320), size=wx.Size(80, 26), style=0)
        self.btnBrowse3.Bind(wx.EVT_BUTTON, self.OnBtnBrowse3Button,
              id=wxID_EDTSTRUCTUREBTNBROWSE3)

        self.staticBox5 = wx.StaticBox(id=wxID_EDTSTRUCTURESTATICBOX5,
              label='Filenames', name='staticBox5', parent=self,
              pos=wx.Point(272, 224), size=wx.Size(392, 136), style=0)

        self.staticBox6 = wx.StaticBox(id=wxID_EDTSTRUCTURESTATICBOX6,
              label='Fractions', name='staticBox6', parent=self,
              pos=wx.Point(136, 224), size=wx.Size(104, 136), style=0)

        self.btnBrowse2 = wx.Button(id=wxID_EDTSTRUCTUREBTNBROWSE2,
              label='Browse', name='btnBrowse2', parent=self, pos=wx.Point(568,
              288), size=wx.Size(80, 26), style=0)
        self.btnBrowse2.Bind(wx.EVT_BUTTON, self.OnBtnBrowse2Button,
              id=wxID_EDTSTRUCTUREBTNBROWSE2)

        self.btnBrowse1 = wx.Button(id=wxID_EDTSTRUCTUREBTNBROWSE1,
              label='Browse', name='btnBrowse1', parent=self, pos=wx.Point(568,
              256), size=wx.Size(80, 26), style=0)
        self.btnBrowse1.Bind(wx.EVT_BUTTON, self.OnBtnBrowse1Button,
              id=wxID_EDTSTRUCTUREBTNBROWSE1)

        self.btnOK = wx.Button(id=wxID_EDTSTRUCTUREBTNOK, label='OK',
              name='btnOK', parent=self, pos=wx.Point(584, 408),
              size=wx.Size(80, 26), style=0)
        self.btnOK.Bind(wx.EVT_BUTTON, self.OnBtnOKButton,
              id=wxID_EDTSTRUCTUREBTNOK)

        self.btnRemove = wx.Button(id=wxID_EDTSTRUCTUREBTNREMOVE,
              label='Remove', name='btnRemove', parent=self, pos=wx.Point(528,
              40), size=wx.Size(72, 26), style=0)
        self.btnRemove.Bind(wx.EVT_BUTTON, self.OnBtnRemoveButton,
              id=wxID_EDTSTRUCTUREBTNREMOVE)

        self.btnInsert = wx.Button(id=wxID_EDTSTRUCTUREBTNINSERT,
              label='Insert', name='btnInsert', parent=self, pos=wx.Point(336,
              40), size=wx.Size(64, 26), style=0)
        self.btnInsert.Bind(wx.EVT_BUTTON, self.OnBtnInsertButton,
              id=wxID_EDTSTRUCTUREBTNINSERT)

        self.staticBox7 = wx.StaticBox(id=wxID_EDTSTRUCTURESTATICBOX7,
              label='Select layer', name='staticBox7', parent=self,
              pos=wx.Point(8, 16), size=wx.Size(264, 56), style=0)

        self.staticBox8 = wx.StaticBox(id=wxID_EDTSTRUCTURESTATICBOX8,
              label='Add new layer', name='staticBox8', parent=self,
              pos=wx.Point(304, 16), size=wx.Size(144, 56), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_EDTSTRUCTURESTATICBOX1,
              label='Remove current layer', name='staticBox1', parent=self,
              pos=wx.Point(480, 16), size=wx.Size(168, 56), style=0)

        self.staticText1 = wx.StaticText(id=wxID_EDTSTRUCTURESTATICTEXT1,
              label='Medium 1', name='staticText1', parent=self,
              pos=wx.Point(40, 264), size=wx.Size(80, 24), style=0)

        self.staticText2 = wx.StaticText(id=wxID_EDTSTRUCTURESTATICTEXT2,
              label='Medium 2', name='staticText2', parent=self,
              pos=wx.Point(40, 296), size=wx.Size(80, 24), style=0)

        self.staticText3 = wx.StaticText(id=wxID_EDTSTRUCTURESTATICTEXT3,
              label='Medium 3', name='staticText3', parent=self,
              pos=wx.Point(40, 328), size=wx.Size(80, 24), style=0)

        self.btnCancel = wx.Button(id=wxID_EDTSTRUCTUREBTNCANCEL,
              label='Cancel', name='btnCancel', parent=self, pos=wx.Point(456,
              408), size=wx.Size(80, 26), style=0)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.OnBtnCancelButton,
              id=wxID_EDTSTRUCTUREBTNCANCEL)

        self.staticBox9 = wx.StaticBox(id=wxID_EDTSTRUCTURESTATICBOX9,
              label='Name of the Multilayer', name='staticBox9', parent=self,
              pos=wx.Point(208, 384), size=wx.Size(200, 56), style=0)

        self.txtStrName = wx.TextCtrl(id=wxID_EDTSTRUCTURETXTSTRNAME,
              name='txtStrName', parent=self, pos=wx.Point(216, 408),
              size=wx.Size(184, 26), style=0, value='textCtrl1')

        self.btnSaveEma = wx.Button(id=wxID_EDTSTRUCTUREBTNSAVEEMA,
              label='Save', name='btnSaveEma', parent=self, pos=wx.Point(32,
              224), size=wx.Size(80, 26), style=0)
        self.btnSaveEma.Bind(wx.EVT_BUTTON, self.OnBtnSaveEmaButton,
              id=wxID_EDTSTRUCTUREBTNSAVEEMA)

        self.txtRough = wx.TextCtrl(id=wxID_EDTSTRUCTURETXTROUGH,
              name='txtRough', parent=self, pos=wx.Point(480, 112),
              size=wx.Size(80, 26), style=0, value='textCtrl1')

        self.staticBox10 = wx.StaticBox(id=wxID_EDTSTRUCTURESTATICBOX10,
              label='Top rms roughness (A)', name='staticBox10', parent=self,
              pos=wx.Point(472, 88), size=wx.Size(176, 56), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        self.parent=parent
        self.Structure=deepcopy(parent.Structure)
        self.CurDir=parent.CurDir
        self.IndexDir=parent.IndexDir
        self.StructureName=parent.StructureName
        self.UpdateFields(self.parent.StoreEdtStr[0])

    def OnBtnInsertButton(self, event):
        j=int(self.chSelect.GetSelection())
        self.UpdateStructure(j)
        #j=int(self.chInsert.GetSelection())+1
        j=int(self.chSelect.GetSelection())+1
        empty=["Untitled", "Not_selected", "Not_selected", \
        "Not_selected", "100", "0", "0", [], [], "0", 0, "0"]
        self.Structure[j:j] = [empty]
        self.UpdateFields(j)
        
    def OnBtnBrowse3Button(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.CurDir+"/"+self.IndexDir, "", "*.in3", wx.FD_OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                l=len(os.path.commonprefix([filename,self.CurDir]))
                if l>0:
                    filename=filename[l+1:]
                #filename=filename[len(os.path.commonprefix([filename,self.CurDir]))+1:]
                #self.txtFilename3.SetValue(filename[len(self.CurDir)+1:len(filename)])
                self.txtFilename3.SetValue(filename)
        finally:
            dlg.Destroy()

    def OnBtnBrowse2Button(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.CurDir+"/"+self.IndexDir, "", "*.in3", wx.FD_OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                l=len(os.path.commonprefix([filename,self.CurDir]))
                if l>0:
                    filename=filename[l+1:]
                #filename=filename[len(os.path.commonprefix([filename,self.CurDir]))+1:]                
                #self.txtFilename2.SetValue(filename[len(self.CurDir)+1:len(filename)])
                self.txtFilename2.SetValue(filename)
        finally:
            dlg.Destroy()

    def OnBtnBrowse1Button(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.CurDir+"/"+self.IndexDir, "", "*.in3", wx.FD_OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                #filename=filename[len(os.path.commonprefix([filename,self.CurDir]))+1:]
                l=len(os.path.commonprefix([filename,self.CurDir]))
                if l>0:
                    filename=filename[l+1:]
                #filename=filename[len(os.path.commonprefix([filename,self.CurDir])):]
                #self.txtFilename1.SetValue(filename[len(self.CurDir)+1:len(filename)])
                self.txtFilename1.SetValue(filename)
                
        finally:
            dlg.Destroy()
            
    def UpdateFields(self,j):
        self.chSelect.Clear()
        for i in range(len(self.Structure)):
            self.chSelect.Append(str(i)+" "+self.Structure[i][0])
        self.chSelect.Select(j)
        
        if j==0 or j==len(self.Structure)-1:
            self.btnRemove.Enable(False)
            self.txtThickness.Enable(False)
            self.chkIncoherent.Enable(False)
        else:
            self.btnRemove.Enable(True)
            self.txtThickness.Enable(True)
            self.chkIncoherent.Enable(True)
        
        if j==len(self.Structure)-1:
            self.btnInsert.Enable(False)
        else:
            self.btnInsert.Enable(True)
        
        if j==0:
            self.txtRough.Enable(False)
        else:
            self.txtRough.Enable(True)


        #a=self.chInsert.GetSelection()
        #a=self.chInsert.GetStringSelection()
        #self.chSelect.Clear(0)
        #self.chSelect.DeleteItem(i)
        
        self.txtName.SetValue(self.Structure[j][0])
        self.txtFilename1.SetValue(self.Structure[j][1])
        self.txtFilename2.SetValue(self.Structure[j][2])
        self.txtFilename3.SetValue(self.Structure[j][3])
        self.txtFraction1.SetValue(self.Structure[j][4])
        self.txtFraction2.SetValue(self.Structure[j][5])
        self.txtFraction3.SetValue(self.Structure[j][6])
        self.txtThickness.SetValue(self.Structure[j][9])
        self.chkIncoherent.SetValue(self.Structure[j][10])
        self.txtRough.SetValue(self.Structure[j][11])
        
        self.txtStrName.SetValue(self.StructureName)

    def OnChSelectChoice(self, event):
        j=int(self.chSelect.GetSelection())
        self.UpdateFields(j)

    def OnBtnRemoveButton(self, event):
        j=int(self.chSelect.GetSelection())
        del self.Structure[j]
        self.UpdateFields(j)
        
    def UpdateStructure(self,j):
        self.CheckFractions()
        
        self.Structure[j][0]=self.txtName.GetValue()
        self.Structure[j][1]=self.txtFilename1.GetValue()
        self.Structure[j][2]=self.txtFilename2.GetValue()
        self.Structure[j][3]=self.txtFilename3.GetValue()
        self.Structure[j][4]=self.txtFraction1.GetValue()
        self.Structure[j][5]=self.txtFraction2.GetValue()
        self.Structure[j][6]=self.txtFraction3.GetValue()
        self.Structure[j][9]=self.txtThickness.GetValue()
        self.Structure[j][10]=int(self.chkIncoherent.GetValue())
        self.Structure[j][11]=self.txtRough.GetValue()
        
        self.StructureName=self.txtStrName.GetValue()

    def OnChSelectEnterWindow(self, event):
        j=int(self.chSelect.GetSelection())
        self.UpdateStructure(j)

    def OnBtnCancelButton(self, event):
        self.Close()

    def OnBtnOKButton(self, event):
        j=int(self.chSelect.GetSelection())
        self.UpdateStructure(j)
        self.parent.StoreEdtStr[0]=j

        try:
            self.Structure=EMA(self.Structure)
            self.parent.Structure=deepcopy(self.Structure)
            self.parent.StructureName=self.StructureName
            self.parent.StructureSaved=False

            #check if there is at least 1 layer
            if len(self.Structure)>2:
                self.parent.btnEFlux.Enable(True)
                self.parent.btnEFluxProfile.Enable(True)
            else:
                self.parent.btnEFlux.Enable(False)
                self.parent.btnEFluxProfile.Enable(False)
            
            kmax=0#check if top medium is transparent
            for k in self.Structure[0][8]:
                kmax=max(kmax,k[1])
            if kmax!=0:
                dlg = wx.MessageDialog(self, 'Warning !! Top medium MUST BE transparent !!',
                  'Caption', wx.OK | wx.ICON_INFORMATION)
                try:
                    dlg.ShowModal()
                finally:
                    dlg.Destroy()
            
            self.Close()

        except:
            dlg = wx.MessageDialog(self, "I can't read one or more of the *.in3 files",
              'Caption', wx.OK | wx.ICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

    def CheckFractions(self):
        try:
            fr1=int(self.txtFraction1.GetValue())
        except:
            fr1=100
        if not(0 <= fr1 <= 100):
            fr1=100
        try:
            fr2=int(self.txtFraction2.GetValue())
        except:
            fr2=100-fr1
        if not(0 <= fr2 <= (100-fr1)):
            fr2=100-fr1
        fr3=100-fr1-fr2
            
        self.txtFraction1.SetValue(str(fr1))
        self.txtFraction2.SetValue(str(fr2))
        self.txtFraction3.SetValue(str(fr3))

    def OnBtnSaveEmaButton(self, event):
        j=int(self.chSelect.GetSelection())
        self.UpdateStructure(j)
        
        try:
            self.Structure=EMA(self.Structure)
            n=self.Structure[j][7]
            k=self.Structure[j][8]
            SaveIn3(self.parent.IndexDir+"/EMA.in3",n,k)
        except:
            dlg = wx.MessageDialog(self, "I can't read one or more of the *.in3 files",
              'Caption', wx.OK | wx.ICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()




        

