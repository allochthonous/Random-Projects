import numpy as np
import matplotlib.pyplot as plt

atom_x=np.tile(np.arange(0.5,40.5,1),25)
atom_y=np.repeat(np.arange(0.5,25.5,1),40)
filelabels=['00','01','02','03','04','05','06','07','08','09','10','11','12']


seqno=1
atom_cols=np.array(['purple']*1000)
plt.figure(figsize=(16,6))
ax1=plt.subplot(1,2,1)
plt.scatter(atom_x,atom_y,color=atom_cols,s=80)
plt.axis('off')
plt.title("On formation: 1000 unstable parent atoms, 0 decayed daughter atoms", fontsize=12, y=0.99) 
ax2=plt.subplot(1,2,2)
plt.xlim(-0.25,12.25)
plt.xticks(range(13))
plt.xlabel('Number of half-lives since formation', fontsize=12)
plt.ylim(-25,1025)
plt.ylabel('Number of atoms', fontsize=12)
half_lives=[0]
parents=[1000]
daughters=[0]
plt.scatter(half_lives,parents,s=200,color='purple', edgecolor='black', label='parent',zorder=4)
plt.scatter(half_lives,daughters,s=200,color='grey', edgecolor='black', label='daughter',zorder=6)
plt.legend(loc=7,fontsize=12)
plt.tight_layout()

plt.savefig('Decay'+`seqno`+'-00.png',dpi=100)

for hl in range(1,13):
    for i in np.where(atom_cols=='purple')[0]:
        if np.random.rand()>0.5: atom_cols[i]='grey'
    ax1.scatter(atom_x,atom_y,color=atom_cols,s=90)
    daughter=len(np.where(atom_cols=='grey')[0])
    half_lives.append(hl)
    daughters.append(daughter)
    parents.append(1000-daughter)
    ax1.set_title("After "+`hl`+" half-lives: "+`1000-daughter`+" unstable parent atoms, "+` daughter`+ " decayed daughter atoms", fontsize=12, y=0.99)
    ax2.scatter(half_lives,parents,s=200,edgecolor='black',color='purple',zorder=4)
    ax2.scatter(half_lives,daughters,s=200,edgecolor='black',color='grey',zorder=6)
    ax2.plot(half_lives,parents,linewidth=2,color='purple',zorder=3)
    ax2.plot(half_lives,daughters,linewidth=2,color='grey',zorder=5)
    plt.savefig('Decay'+`seqno`+'-'+filelabels[hl]+'.png',dpi=100)    

old_half_lives=[half_lives]
old_daughters=[daughters]
old_parents=[parents]
                                        
for seqno in range(2,10):
    half_lives=[0]
    parents=[1000]
    daughters=[0]
    atom_cols=np.array(['purple']*1000)
    plt.figure(figsize=(16,6))
    ax1=plt.subplot(1,2,1)
    plt.scatter(atom_x,atom_y,color=atom_cols,s=80)
    plt.axis('off')
    plt.title("On formation: 1000 unstable parent atoms, 0 decayed daughter atoms", fontsize=12, y=0.99) 
    ax2=plt.subplot(1,2,2)
    plt.xlim(-0.25,12.25)
    plt.xticks(range(13))
    plt.xlabel('Number of half-lives since formation', fontsize=12)
    plt.ylim(-25,1025)
    plt.ylabel('Number of atoms', fontsize=12)
    
    for x,y1,y2 in zip (old_half_lives,old_parents,old_daughters):
        plt.plot(x,y1,linewidth=6,color='purple',alpha=0.2, zorder=2)
        plt.plot(x,y2,linewidth=6,color='grey',alpha=0.2, zorder=1)
    
    plt.scatter(half_lives,parents,s=200,color='purple',edgecolor='black', label='parent',zorder=4)
    plt.scatter(half_lives,daughters,s=200,color='grey', edgecolor='black',label='daughter',zorder=6)
    plt.legend(loc=7,fontsize=12)
    plt.tight_layout()
    
    plt.savefig('Decay'+`seqno`+'-00.png',dpi=100)
    
    for hl in range(1,13):
        for i in np.where(atom_cols=='purple')[0]:
            if np.random.rand()>0.5: atom_cols[i]='grey'
        ax1.scatter(atom_x,atom_y,color=atom_cols,s=90)
        daughter=len(np.where(atom_cols=='grey')[0])
        half_lives.append(hl)
        daughters.append(daughter)
        parents.append(1000-daughter)
        ax1.set_title("After "+`hl`+" half-lives: "+`1000-daughter`+" unstable parent atoms, "+` daughter`+ " decayed daughter atoms", fontsize=12, y=0.99)
        ax2.scatter(half_lives,parents,s=200,edgecolor='black',color='purple',zorder=4)
        ax2.scatter(half_lives,daughters,s=200,edgecolor='black',color='grey',zorder=6)
        ax2.plot(half_lives,parents,linewidth=2,color='purple',zorder=3)
        ax2.plot(half_lives,daughters,linewidth=2,color='grey',zorder=5)
        plt.savefig('Decay'+`seqno`+'-'+filelabels[hl]+'.png',dpi=100)  
    old_half_lives.append(half_lives)
    old_daughters.append(daughters) 
    old_parents.append(parents)
    
    
#2 different half lives simulation 

atom_cols=np.array(['purple']*1000)
atom2_cols=np.array(['green']*1000)
plt.figure(figsize=(16,12))
ax1=plt.subplot(2,2,1)
plt.scatter(atom_x,atom_y,color=atom_cols,s=40)
plt.title("On formation: 1000 unstable parent atoms, 0 decayed daughter atoms", fontsize=12, y=0.99) 
plt.axis('off')
ax2=plt.subplot(2,2,2)
plt.xlim(-0.28,16.28)
plt.xticks(range(17))
plt.xlabel('Number of half-lives since formation', fontsize=12)
plt.ylim(-50,1050)
plt.ylabel('Number of atoms', fontsize=12)
half_lives=[0]
parents=[1000]
daughters=[0]
plt.scatter(half_lives,parents,s=200,color='purple', edgecolor='black', label='parent',zorder=4)
plt.scatter(half_lives,daughters,s=200,color='0.6', edgecolor='black', label='daughter',zorder=6)
plt.legend(loc=7,fontsize=12)
ax3=plt.subplot(2,2,3)
plt.scatter(atom_x,atom_y,color=atom2_cols,s=40)
plt.title("On formation: 1000 unstable parent atoms, 0 decayed daughter atoms", fontsize=12, y=0.99) 
plt.axis('off')
plt.tight_layout()
ax4=plt.subplot(2,2,4)
plt.xlim(-0.07,4.07)
plt.xticks(range(5))
plt.xlabel('Number of half-lives since formation', fontsize=12)
plt.ylim(-50,1050)
plt.ylabel('Number of atoms', fontsize=12)
half_lives2=[0]
parents2=[1000]
daughters2=[0]
plt.scatter(half_lives2,parents2,s=200,color='green', edgecolor='black', label='parent',zorder=4)
plt.scatter(half_lives2,daughters2,s=200,color='0.8', edgecolor='black', label='daughter',zorder=6)
plt.legend(loc=7,fontsize=12)
plt.tight_layout()

plt.savefig('DualDecay'+'-0.png',dpi=100)

half_life1=1
half_life2=4

for hl in range(1,17):
    for i in np.where(atom_cols=='purple')[0]:
        if np.random.rand()>np.exp(-0.693*1/half_life1): atom_cols[i]='0.6'
    ax1.scatter(atom_x,atom_y,color=atom_cols,s=42)
    daughter=len(np.where(atom_cols=='0.6')[0])
    half_lives.append(hl)
    daughters.append(daughter)
    parents.append(1000-daughter)
    ax1.set_title("After "+`hl`+" half-lives: "+`1000-daughter`+" unstable parent atoms, "+` daughter`+ " decayed daughter atoms", fontsize=12, y=0.99)
    ax2.scatter(half_lives,parents,s=200,edgecolor='black',color='purple',zorder=4)
    ax2.scatter(half_lives,daughters,s=200,edgecolor='black',color='0.6',zorder=6)
    ax2.plot(half_lives,parents,linewidth=2,color='purple',zorder=3)
    ax2.plot(half_lives,daughters,linewidth=2,color='0.6',zorder=5)
    
    for i in np.where(atom2_cols=='green')[0]:
        if np.random.rand()>np.exp(-0.693*1/half_life2): atom2_cols[i]='0.8'
    ax3.scatter(atom_x,atom_y,color=atom2_cols,s=42)
    daughter2=len(np.where(atom2_cols=='0.8')[0])
    half_lives2.append(hl/4.)
    daughters2.append(daughter2)
    parents2.append(1000-daughter2)
    ax3.set_title("After "+`hl/4.`+" half-lives: "+`1000-daughter2`+" unstable parent atoms, "+` daughter2`+ " decayed daughter atoms", fontsize=12, y=0.99)
    ax4.scatter(half_lives2,parents2,s=200,edgecolor='black',color='green',zorder=4)
    ax4.scatter(half_lives2,daughters2,s=200,edgecolor='black',color='0.8',zorder=6)
    ax4.plot(half_lives2,parents2,linewidth=2,color='green',zorder=3)
    ax4.plot(half_lives2,daughters2,linewidth=2,color='0.8',zorder=5)
    
    plt.savefig('DualDecay-'+`hl`+'.png',dpi=100)
