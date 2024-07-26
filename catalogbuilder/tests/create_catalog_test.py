#!/usr/bin/env python

@pytest.mark.skip(reason="this can only work with a conda installed catalogbuilder now")
#TODO test after conda pkg is published and make changes as needed 
from catalogbuilder.scripts import gen_intake_gfdl
#from . import gen_intake_gfdl
import sys

input_path = "archive/am5/am5/am5f3b1r0/c96L65_am5f3b1r0_pdclim1850F/gfdl.ncrc5-deploy-prod-openmp/pp"
output_path = "test"
try:
  gen_intake_gfdl.create_catalog(input_path,output_path)
except:
  sys.exit("Exception occured calling gen_intake_gfdl.create_catalog")
