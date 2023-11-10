import os
import subdirs
from subdirs import *
from pathlib import Path

realm_mapping = [realm]
root_dir = 'archive/am5/am5/am5f3b1r0/c96L65_am5f3b1r0_pdclim1850F/gfdl.ncrc5-deploy-prod-openmp/pp'
freq_mapping = [freq]
chunk_freq = '1yr'

#atmos.000301-000312.vas.nc
def main():
    # Create directory
    realm_ctr = (len(subdirs.realm))
    i = 0
    for j in range(0, realm_ctr):
           dirName = str(root_dir) + '/' + str(realm_mapping[i][j]) + '/' + 'ts'
           realm_name = realm_mapping[i][j]
           try:
               os.makedirs(dirName)
               print("Directory " , dirName ,  " Created ") 
           except FileExistsError:
               print("Directory " , dirName ,  " already exists")       
               pass 
           for j in range(0,len(subdirs.freq)):
             dirName2 = dirName + '/' + str(freq_mapping[i][j]) + '/' + chunk_freq + '/'
             try:
                  os.makedirs(dirName2)
                  print("Directory " , dirName2 ,  " Created ")
             except FileExistsError:
                  print("Directory " , dirName2 ,  " already exists")
                  pass
              #touch files
             for v in range(0, len(subdirs.vars)):
               for t in range(0, len(subdirs.time)):
                 filename = "{0}.{1}.{2}.nc".format(str(realm_name),str(subdirs.time[t]),str(subdirs.vars[v]))
                 try:
                    Path(dirName2+filename).touch()
                    print(dirName2+filename+" created")
                 except:
                    print("touch failed on ", dirName2+filename)
                    pass
      
         
if __name__ == '__main__':
    main()
