#Optical, Copyright (C) 2005  Emanuele Centurioni
#see Optical.py

from numpy import *
import os.path 

def EMA(s):
    #computes n and k for a mixed material using
    #effective medium approximation (EMA)
    for i in range(len(s)):
        fr1,fr2,fr3=int(s[i][4]),int(s[i][5]),int(s[i][6])
        if fr1==100:#just one medium, no EMA
            filename=s[i][1]
            n,k=ReadIn3(filename)
            s[i][7]=n
            s[i][8]=k
        else:#EMA 2 or 3 mediums
            n,k=[],[]
            for j in range(2):
                nt,kt=ReadIn3(s[i][1+j])
                n.append(nt)
                k.append(kt)

            n.append(0)
            k.append(0)
            if fr3 == 0:#just 2 mediums
                n[2],k[2]=ReadIn3(s[i][2])
            else:#O.K. 3 mediums
                n[2],k[2]=ReadIn3(s[i][3])

            ln,lk=[],[]
            for j in range(3):
                lnt,lkt=[],[]
                for h in range(len(n[j])):
                    lnt.append(n[j][h][0])
                for h in range(len(k[j])):
                    lkt.append(k[j][h][0])
                ln.append(lnt)
                lk.append(lkt)
            
            lmin=max(min(ln[0]),min(ln[1]),min(ln[2]),min(lk[0]),min(lk[1]),min(lk[2]))
            lmax=min(max(ln[0]),max(ln[1]),max(ln[2]),max(lk[0]),max(lk[1]),max(lk[2]))
            
            ln=ln[0]+ln[1]+ln[2]+[lmin,lmax]
            lk=lk[0]+lk[1]+lk[2]+[lmin,lmax]
            
            ln=sortRemoveDupes(ln)
            lk=sortRemoveDupes(lk)

            lnt=ln[:]
            ln=[]
            for j in lnt:
                if lmin <= j <= lmax:
                    ln.append(j)
                    
            lkt=lk[:]
            lk=[]
            for j in lkt:
                if lmin <= j <= lmax:
                    lk.append(j)
            
            nn,nk=[],[]
            fr=[fr1,fr2,fr3]
            for lam in ln:
                ne=[]
                for h in range(3):
                    nr=Interpol(n[h],lam)
                    ni=Interpol(k[h],lam)
                    ne.append(nr+ni*(1j))
                nn.append([lam, EMA3(ne, fr).real])
                
            for lam in lk:
                ne=[]
                for h in range(3):
                    nr=Interpol(n[h],lam)
                    ni=Interpol(k[h],lam)
                    ne.append(nr+ni*(1j))
                nk.append([lam, EMA3(ne, fr).imag])
                
            s[i][7]=nn
            s[i][8]=nk
    
    return s
        
def ReadIn3(filename):
    #load n and k from an index file *.in3
    n=[]
    k=[]
    filename=filename.replace("\\","/")#for win compatibility
    in_file=open(os.path.normpath(filename),"r")
    line=in_file.readline()
    line=in_file.readline()
    line=in_file.readline()
    nn=int(CleanRecord(line))
    for i in range(nn):
        line=in_file.readline()
        answer=CleanRecord(line).split()
        n.append([int(round(float(answer[0]))), float(answer[1])])
    
    line=in_file.readline()
    nk=int(CleanRecord(line))
    for i in range(nk):
        line=in_file.readline()
        answer=CleanRecord(line).split()
        k.append([int(round(float(answer[0]))), float(answer[1])])
    in_file.close()
    
    return n,k

def CleanRecord(a):
    if a[-2:]=="\r\n":#remove from string Ms format end of record
        a=a[:-2]
    elif a[-1:]=="\n":#remove from string Unix format end of record
        a=a[:-1]
    a=a.replace(","," ")
    return a

def CleanRecord2(a):
    if a[-2:]=="\r\n":#remove from string Ms format end of record
        a=a[:-2]
    elif a[-1:]=="\n":#remove from string Unix format end of record
        a=a[:-1]
    return a

def SaveStructure(filename,structurename,s):
    #save a multilayer
    out_file=open(filename,"w")
    out_file.write(structurename+"\n")
    for i in range(len(s)):
        record = ""
        record = record+s[i][0]+","
        record = record+s[i][1]+","
        record = record+s[i][2]+","
        record = record+s[i][3]+","
        record = record+s[i][4]+","
        record = record+s[i][5]+","
        record = record+s[i][6]+","
        record = record+s[i][9]+","
        record = record+str(s[i][10])+","
        record = record+s[i][11]+"\n"        
        out_file.write(record)
    out_file.close()

def OpenStructure(filename):
    #load a multilayer
    s=[]
    in_file=open(filename,"r")
    line=in_file.readline()
    StructureName=CleanRecord2(line)
    while True:
        line=in_file.readline()
        if len(line)==0:
            break
        values=CleanRecord2(line).split(",")
        values[7:7]=[0]
        values[8:8]=[0]
        values[10]=int(values[10])
        if len(values)==11:#for compatibility with ver 0.15 and older
            values.append("0")
        s.append(values)
    in_file.close()
    return s,StructureName

def Interpol(a,l):
    #linear interpolation
    for i in range(len(a)):
        if a[i][0]==l:
            n=a[i][1]
            break
        if a[i][0]>l:
            n = a[i-1][1] + 1.0*(l - a[i-1][0]) / (a[i][0] - a[i-1][0]) * \
            (a[i][1] - a[i-1][1])
            break
    return n

def PrepareList(a,l):
    #prepare list for globscatmatr
    b=[]
    for i in range(len(a)):
        thickness=int(float(a[i][9]))
        roughness=int(float(a[i][11]))
        n=[]
        for lam in l:
            nr=Interpol(a[i][7],lam)
            ni=Interpol(a[i][8],lam)
            n.append(nr+ni*(1j))
        coherence=a[i][10]
        b.append([thickness, n, coherence, roughness])
    return b

def sortRemoveDupes(lst):
    """Sort the list, and remove duplicate symbols.
    """
    if len(lst) == 0:
        return lst
    lst.sort()
    lst = [lst[0]] + [lst[i] for i in range(1, len(lst))
            if lst[i] != lst[i - 1]]
    return lst

def EMA3(n, fr):
    #effective medium approximation 3 medium 
    e1,e2,e3=n[0]**2,n[1]**2,n[2]**2
    f1,f2,f3=fr[0]/100.0,fr[1]/100.0,fr[2]/100.0
    nguess=f1*n[0]+f2*n[1]+f3*n[2]
    a=-4
    b=f1*(4*e1-2*(e2+e3))+f2*(4*e2-2*(e1+e3))+f3*(4*e3-2*(e1+e2))
    c=f1*(2*e1*(e2+e3)-e2*e3)+f2*(2*e2*(e1+e3)-e1*e3)+f3*(2*e3*(e1+e2)-e1*e2)
    d=(f1+f2+f3)*(e1*e2*e3)
    e=root3(a,b,c,d)
    pn=[e[0]**(0.5),e[1]**(0.5),e[2]**(0.5)]
    distance=[abs(pn[0]-nguess), abs(pn[1]-nguess), abs(pn[2]-nguess)]
    return pn[distance.index(min(distance))]

def root3(a,b,c,d):
    #finds roots of eq ax^3+bx^2+cx+d=0
    a,b,c=b/a,c/a,d/a
    p=(-a**2)/3+b
    q=(2*a**3)/27-a*b/3+c
    u1=(-q/2+((q**2)/4+(p**3)/27)**(0.5))**(1.0/3)
    u,x=[],[]
    u.append(u1)#there are 3 roots for u
    u.append(u1*exp(2*pi/3*1j))
    u.append(u1*exp(4*pi/3*1j))
    for i in range(3):
        x.append(u[i]-p/(3*u[i])-a/3)
    return x

def CheckWaveRange(s):
    #return wavelength range that can be computed
    lmin,lmax=[],[]
    for i in range(len(s)):
        n=s[i][7]
        k=s[i][8]
        ln,lk=[],[]
        for h in range(len(n)):
            ln.append(n[h][0])
        for h in range(len(k)):
            lk.append(k[h][0])
        lmin.append(max(min(ln),min(lk)))
        lmax.append(min(max(ln),max(lk)))
    lmin=max(lmin)
    lmax=min(lmax)
    return lmin,lmax

def SaveRT(lam,T,R):
    #save computed R and T
    out_file=open("RT.dat","w")
    out_file.write("#Lam(nm)     R%(0-100)     T%(0-100)"+"\n")
    for i in range(len(lam)):
        record = ""
        record = record+str(lam[i]/10.0)+" "
        record = record+str(R[i]*100)+" "
        record = record+str(T[i]*100)+" "
        record = record+"\n"
        out_file.write(record)
    out_file.close()

def SavePsiDelta(lam,psi,delta,e1,e2,n,k):
    #save computed psi and delta
    out_file=open("PsiDelta.dat","w")
    out_file.write("#Lam(nm)   psi(deg)   delta(deg)   e1   e2   n   k"+"\n")
    for i in range(len(lam)):
        record = ""
        record = record+str(lam[i]/10.0)+" "
        record = record+str(psi[i])+" "
        record = record+str(delta[i])+" "
        record = record+str(e1[i])+" "
        record = record+str(e2[i])+" "
        record = record+str(n[i])+" "
        record = record+str(k[i])+" "                        
        record = record+"\n"
        out_file.write(record)
    out_file.close()

def SaveA(lam,A):
    #save internal light absorption
    out_file=open("A.dat","w")
    out_file.write("#Lam(nm)      A(%)"+"\n")
    for i in range(len(lam)):
        record = ""
        record = record+str(lam[i]/10.0)+" "
        record = record+str(A[i]*100)+" "
        record = record+"\n"
        out_file.write(record)
    out_file.close()

def SaveFlux(lam,A):
    #save light energy flux
    out_file=open("Flux.dat","w")
    out_file.write("#Lam(nm)      Flux(%)"+"\n")
    for i in range(len(lam)):
        record = ""
        record = record+str(lam[i]/10.0)+" "
        record = record+str(A[i]*100)+" "
        record = record+"\n"
        out_file.write(record)
    out_file.close()


def LoadRT(Filename):
    #load experimental R and T spectra
    Exp=[]
    path=os.path.split(Filename)
    RorT=path[1][:1].lower()
    if Filename[-3:].lower()=="dat":#check data type
        RandT=path[1][:2].lower()
        if RandT=="rt":#file contains both R and T
            in_file=open(Filename,"r")
            line=in_file.readline()
            while True:
                line=in_file.readline()
                if len(line)==0:
                    break
                values=CleanRecord(line).split()
                Exp.append([int(round(float(values[0])*10)),float(values[1])/100.0,float(values[2])/100.0])
            in_file.close()
        else:
            ExpR,ExpT=[],[]
            in_file=open(Filename,"r")
            line=in_file.readline()
            while True:
                line=in_file.readline()
                if len(line)==0:
                    break
                values=CleanRecord(line).split()
                if RorT=="r":
                    ExpR.append([int(round(float(values[0]))*10),float(values[1])/100.0])
                if RorT=="t":
                    ExpT.append([int(round(float(values[0]))*10),float(values[1])/100.0])
            Filenames=[]
            if RorT=="r":
                Filenames.append(os.path.join(path[0],"T"+path[1][1:]))
                Filenames.append(os.path.join(path[0],"t"+path[1][1:]))
            elif RorT=="t":
                Filenames.append(os.path.join(path[0],"R"+path[1][1:]))
                Filenames.append(os.path.join(path[0],"r"+path[1][1:]))

            for Filename in Filenames:
                try:
                    in_file=open(Filename,"r")
                    line=in_file.readline()
                    while True:
                        line=in_file.readline()
                        if len(line)==0:
                            break
                        values=CleanRecord(line).split()
                        if RorT=="r":
                            ExpT.append([int(round(float(values[0]))*10),float(values[1])/100.0])
                        if RorT=="t":
                            ExpR.append([int(round(float(values[0]))*10),float(values[1])/100.0])
                except:
                    pass

            if len(ExpR)==0:
                ExpR=[[1,0.0],[1E6,0.0]]
            if len(ExpT)==0:
                ExpT=[[1,0.0],[1E6,0.0]]
            
            lR,lT=[],[]
            for j in range(len(ExpR)):
                lR.append(ExpR[j][0])
            for j in range(len(ExpT)):
                lT.append(ExpT[j][0])
            
            lmin=max(min(lR),min(lT))
            lmax=min(max(lR),max(lT))
            lRT=sortRemoveDupes(lR+lT)

            lRTt=lRT[:]
            lRT=[]
            for j in lRTt:
                if lmin <= j <= lmax:
                    lRT.append(j)
            
            for lam in lRT:
                R=Interpol(ExpR,lam)    
                T=Interpol(ExpT,lam)    
                Exp.append([lam,R,T])
                
    elif Filename[-3:].lower()=="wav":
        Filenames=[]
        if RorT=="r":
            Filenames.append(os.path.join(path[0],"T"+path[1][1:]))
            Filenames.append(os.path.join(path[0],"t"+path[1][1:]))            
        elif RorT=="t":
            Filenames.append(os.path.join(path[0],"R"+path[1][1:]))
            Filenames.append(os.path.join(path[0],"r"+path[1][1:]))            

        in_file=open(Filename,"r")
        for i in range(5):
            line=in_file.readline()
        values=CleanRecord(line).split()
        npoints,step=int(values[2]),int(values[3])
        line=in_file.readline()
        values=CleanRecord(line).split()
        lmin,lmax=int(values[0]),int(values[1])
        for i in range(npoints):
            lam=lmin*10+step*10*i
            line=in_file.readline()
            values=CleanRecord(line).split()
            if RorT=="r":
                Exp.append([int(lam),float(values[0])/100.0,0.0])
            elif RorT=="t":
                Exp.append([int(lam),0.0,float(values[0])/100.0])
        in_file.close()

        for Filename in Filenames:
            try:
                in_file=open(Filename,"r")
                for i in range(6):
                    line=in_file.readline()
                for i in range(npoints):
                    line=in_file.readline()
                    values=CleanRecord(line).split()
                    if RorT=="r":
                        Exp[i][2]=float(values[0])/100.0
                    elif RorT=="t":
                        Exp[i][1]=float(values[0])/100.0
                in_file.close()
            except:
                pass

    elif Filename[-3:].lower()=="csv":
            ExpR,ExpT=[],[]
            in_file=open(Filename,"r")
            #line=in_file.readline()
            while True:
                line=in_file.readline()
                if len(line)==0:
                    break
                values=CleanRecord(line).split()
                if RorT=="r":
                    ExpR.append([int(round(1.0E8/float(values[0]))),float(values[1])/100.0])
                if RorT=="t":
                    ExpT.append([int(round(1.0E8/float(values[0]))),float(values[1])/100.0])
            Filenames=[]
            if RorT=="r":
                Filenames.append(os.path.join(path[0],"T"+path[1][1:]))
                Filenames.append(os.path.join(path[0],"t"+path[1][1:]))
            elif RorT=="t":
                Filenames.append(os.path.join(path[0],"R"+path[1][1:]))
                Filenames.append(os.path.join(path[0],"r"+path[1][1:]))

            for Filename in Filenames:
                try:
                    in_file=open(Filename,"r")
                    line=in_file.readline()
                    while True:
                        line=in_file.readline()
                        if len(line)==0:
                            break
                        values=CleanRecord(line).split()
                        if RorT=="r":
                            ExpT.append([int(round(1.0E8/float(values[0]))),float(values[1])/100.0])
                        if RorT=="t":
                            ExpR.append([int(round(1.0E8/float(values[0]))),float(values[1])/100.0])
                except:
                    pass

            ExpR.reverse()
            ExpT.reverse()
            if len(ExpR)==0:
                ExpR=[[1,0.0],[1E6,0.0]]
            if len(ExpT)==0:
                ExpT=[[1,0.0],[1E6,0.0]]
            
            lR,lT=[],[]
            for j in range(len(ExpR)):
                lR.append(ExpR[j][0])
            for j in range(len(ExpT)):
                lT.append(ExpT[j][0])
            
            lmin=max(min(lR),min(lT))
            lmax=min(max(lR),max(lT))
            lRT=sortRemoveDupes(lR+lT)

            lRTt=lRT[:]
            lRT=[]
            for j in lRTt:
                if lmin <= j <= lmax:
                    lRT.append(j)
            
            for lam in lRT:
                R=Interpol(ExpR,lam)    
                T=Interpol(ExpT,lam)    
                Exp.append([lam,R,T])
    return Exp

def Chi(R,T,Re,Te,st_dev):
    #compute chi square test
    Chi_R,Chi_T=0.0,0.0
    for i in range(len(R)):
        Chi_R=Chi_R+((Re[i]-R[i])/st_dev)**2
        Chi_T=Chi_T+((Te[i]-T[i])/st_dev)**2
    Chi_RT = (Chi_R+Chi_T)/(len(R)+len(T))
    Chi_R = Chi_R/len(R)
    Chi_T = Chi_T/len(T)
    
    return Chi_R,Chi_T,Chi_RT

def FileExists(filename):
    #check if a file exists
    try:
        in_file=open(filename,"r")
        in_file.close()
        answer=True
    except:
        answer=False
    return answer

def SaveIn3(filename,n,k):
    #save n and k in an index file *.in3
    out_file=open(filename,"w")
    out_file.write("#Generated by EMA"+"\n")
    
    ln,lk=[],[]
    for h in range(len(n)):
        ln.append(n[h][0])
    for h in range(len(k)):
        lk.append(k[h][0])
    lmin=max(min(ln),min(lk))
    lmax=min(max(ln),max(lk))
    
    out_file.write(str(lmin)+" "+str(lmax)+"\n") 

    out_file.write(str(len(n))+"\n")        
    for i in range(len(n)):
        out_file.write(str(n[i][0])+" "+str(n[i][1])+"\n") 

    out_file.write(str(len(k))+"\n")        
    for i in range(len(k)):
        out_file.write(str(k[i][0])+" "+str(k[i][1])+"\n") 
    
    out_file.close()
    
def LoadConf():
    #load some configuration values from "settings.txt"
    try:
        list=[]
        in_file=open("settings.txt","r")
        while True:
            line=in_file.readline()
            if len(line)==0:
                break
            values=CleanRecord2(line).split(",")
            if len(values)==2:
                if len(values[0])>0:
                    if values[0][:1]!="#":
                        list.append(values[0])
                        list.append(values[1])
        in_file.close()
    except:
        pass
    
    return list

def SaveFluxProfile(E):
    #save energy flux profile in multlayer 
    out_file=open("FluxProf.dat","w")
    out_file.write("#Depth (nm)      E(%)"+"\n")
    for i in range(len(E)):
        record = ""
        record = record+str(E[i][0]/10.0)+" "
        record = record+str(E[i][1]*100)+" "
        record = record+"\n"
        out_file.write(record)
    out_file.close()

def SaveAlpha(lam,A,sample):
    #save absorption coefficient generated by alpha
    out_file=open("Alpha.dat","w")
    out_file.write("#Lam(nm)      Alpha(cm^-1)      "+sample+"\n")
    for i in range(len(lam)):
        record = ""
        record = record+str(lam[i]/10.0)+" "
        record = record+str(A[i])+" "
        record = record+"\n"
        out_file.write(record)
    out_file.close()

def SaveAlphaIn3(filename,lam,n,a,sample):
    #save index of refraction generated by alpha
    out_file=open(filename,"w")
    out_file.write("#Generated by Alpha      "+sample+"\n")
    
    lmin=min(lam)
    lmax=max(lam)
    
    out_file.write(str(lmin)+" "+str(lmax)+"\n") 

    out_file.write(str(len(n))+"\n")        
    for i in range(len(n)):
        out_file.write(str(lam[i])+" "+str(n[i].real)+"\n") 

    out_file.write(str(len(a))+"\n")        
    for i in range(len(a)):
        out_file.write(str(lam[i])+" "+str(a[i]*lam[i]*1E-8/(4*pi))+"\n") 

    out_file.close()
    
def Load(Filename):
    #this subroutine is under test, please ignore it
    a=[]
    path=os.path.split(Filename)
    in_file=open(Filename,"r")
    line=in_file.readline()
    while True:
        line=in_file.readline()
        if len(line)==0:
            break
        values=CleanRecord(line).split()
        a.append([float(values[0]),float(values[1])])
    in_file.close()
    return a

def ComputeQE():
    #this subroutine is under test, please ignore it        
        AM15G=Load("am15g.dat")
        QE=Load("A.dat")
        
        lmin=QE[0][0]
        lmax=QE[len(QE)-1][0]
     
        curr=0.0
        for l in range(int(round(lmin))+1,int(round(lmax))):
            dcurr = Interpol(QE,l)*Interpol(AM15G,l)*l/1240
            curr = curr + dcurr
        return curr/1000.0
        
def ComputeE():
    #this subroutine is under test, please ignore it        
    #Energy [W/m2]
        AM15G=Load("am15g.dat")
        QE=Load("A.dat")
        
        lmin=QE[0][0]
        lmax=QE[len(QE)-1][0]
     
        E=0.0
        for l in range(int(round(lmin))+1,int(round(lmax))):
            dE = Interpol(QE,l)*Interpol(AM15G,l)
            E = E + dE
        return E

def BlackBody(T):        
    #this subroutine is under test, please ignore it        
        C1=3.74E-16 # J*m/sec
        C2=1.44E-2 # m*K
        #T = 800 #K
        #nota: lambda deve essere in metri

        RT=[]
        in_file=open("RT.dat","r")
        line=in_file.readline()
        while True:
            line=in_file.readline()
            if len(line)==0:
                break
            values=line.split()
            RT.append([int(round(float(values[0]))),float(values[1])/100.0,float(values[2])/100.0])
        in_file.close()
        
        out_file=open("BlackBody.dat","w")
        out_file.write("Lam(um)      w/um3"+"\n")
        for n in range(len(RT)):
            la=RT[n][0]# in nm
            l=la*1E-9# in m
            A=1-RT[n][1]-RT[n][2]
            q=C1*l**(-5)/(exp(C2/(l*T)) - 1)# W/m3 (overo W/m2 per unita di lunghezza d'onda)
            q=q*1E-18# W/um3
            #print l, NPh
       
            record = ""
            record = record+str(la/1000.0)+" "
            record = record+str(q*A)+" "
            record = record+"\n"
            out_file.write(record)
        out_file.close()

