
import numpy as np
import matplotlib.pyplot as plt

no_of_lines = 0
model_no = 0
NMR = "NMR"
start_model = 'MODEL'
end_model = 'ENDMDL'
exper_data = "EXPDATA"
ATOM = "ATOM"
model_no = []
DIFF = 4
CUTOFF_DIST = 4.5

clean_pdb = open("contacts.txt","w")

with open('2k7x.pdb') as input_pdb:
    for lines in input_pdb:
        no_of_lines += 1
        info = lines[0:6].replace(" ", "")
#        if (start_model.intersection(set(lines))): This matches letters hence, cannot be used
# The following if statement works but can't be used to check for no. of models
#        if (lines.find(start_model) == -1):
#            pass
#         else:
#            print(lines, end='')
#            model_no += 1
#        if (start_model in lines):
#           model_no += 1
        if (info == exper_data) and (NMR in lines):
            print ("This is a NMR structure")

        if (start_model == info):
            model_no.append(no_of_lines)
        
    input_pdb.seek(0)
    line_no = 0
    atom_no = []
    residue_no = []
    Co_ordinates = []
    x = [] 
    y = []
    z = []
    for lines2 in input_pdb:
        line_no += 1
        info = lines2[0:6].replace(" ", "")
        atom_name = lines2[12:16].replace(" ", "")
        if (line_no > model_no[0]) and (line_no < model_no[1]) and (info == ATOM) and (atom_name[0] != "H"):
            #print(lines2, end = '', file=clean_pdb)                
            atom_no.append(int (lines2[6:11].replace(" ", "")))
            residue_no.append(int(lines2[22:26].replace(" ", "")))
            x = float(lines2[30:38].replace(" ", ""))
            y = float(lines2[38:46].replace(" ", ""))
            z = float(lines2[46:54].replace(" ", ""))
            Co_ordinates.append([x, y, z])

print ("Total no. of lines are = ", no_of_lines, "Total no. of models are = ", len(model_no) )
print ("Model no. 1 will be chosen for contact map calculation")
#print(len(atom_no), len(residue_no), Co_ordinates)
np_co_ordinates = np.array(Co_ordinates)
#print (np_co_ordinates[None, :].shape, np_co_ordinates[:,None].shape)
#m = np_co_ordinates[None, :] - np_co_ordinates[:, None]
dist_matrix = np.sqrt (np.sum((np_co_ordinates[None, :] - np_co_ordinates[:, None])**2, -1))
print ("The no. of dimensions are ", np.ndim(dist_matrix))
result = np.where (dist_matrix <= CUTOFF_DIST )
Contacts = list(zip(result[0], result[1]))
C_alpha_contacts_matrix = []
All_atom_contacts_matrix = []
for cont in Contacts:
    if (cont[0] != cont[1]) and (abs (residue_no[cont[0]] - residue_no[cont[1]]) >= DIFF):
#        print (cont[0], cont[1])
        All_atom_contacts_matrix.append([atom_no[cont[0]], atom_no[cont[1]]])
        C_alpha_contacts_matrix.append([residue_no[cont[0]], residue_no[cont[1]]])

C_alpha_contacts_matrix_unique = np.unique(np.array(C_alpha_contacts_matrix), axis = 0)
#print(C_alpha_contacts_matrix_unique, file=clean_pdb)
#print(All_atom_contacts_matrix, file=clean_pdb)
clean_pdb.close()

# This part plots the Contact map
x = C_alpha_contacts_matrix_unique[:,0]
y = C_alpha_contacts_matrix_unique[:,1]
print (residue_no[0] , residue_no[-1])
plt.plot(x,y,'bs',ms = 2.0)
#plt.xlim([residue_no[0], residue_no[-1]])
#plt.ylim([residue_no[0], residue_no[-1]])
plt.axis([residue_no[0], residue_no[-1], residue_no[0], residue_no[-1]])
tick_range = np.arange(residue_no[0],residue_no[-1]+1, 20)
#plt.xticks(tick_range)
#plt.yticks(tick_range)
#plt.xlim([residue_no[0], residue_no[-1]])
#plt.ylim([residue_no[0], residue_no[-1]])
plt.xlabel('Residue-no')
plt.ylabel('Residue-no')
plt.axis('square')
plt.show()
# This is comment to check git
