#!/usr/bin/env python

#TODO test after conda pkg is published and make changes as needed 
from catalogbuilder.scripts import gen_intake_gfdl
import sys

input_path = "/archive/am5/am5/am5f3b1r0/c96L65_am5f3b1r0_pdclim1850F/gfdl.ncrc5-deploy-prod-openmp/pp/"
output_path = "test"
sys.argv = ['INPUT_PATH', input_path, output_path]
print(sys.argv)
gen_intake_gfdl.main()
