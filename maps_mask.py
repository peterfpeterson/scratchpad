import DirectEnergyConversion as reduction
rootdir="/home/pf9/code/systemtests/Data/"
white = rootdir+'MAP17186.raw'
sample = rootdir+'MAP17269.raw'
config['default.facility']='ISIS'

# Libisis values to check against
tiny=1e-10
huge=1e10

v_out_lo = 0.01
v_out_hi = 100.

vv_lo = 0.1
vv_hi = 2.0
vv_sig = 0.0

sv_sig = 3.3
sv_hi = 1.5
sv_lo = 0.0
s_zero = True

reducer = reduction.setup_reducer('MAPS')
diag_mask = reducer.diagnose(white, sample=sample, tiny=tiny, huge=huge, 
                             van_out_lo=v_out_lo, van_out_hi=v_out_hi,
                             van_lo=vv_lo, van_hi=vv_hi, van_sig=vv_sig,
                             samp_lo=sv_lo, samp_hi=sv_hi, samp_sig=sv_sig, samp_zero=s_zero)
Load("/home/pf9/code/systemtests/Data/MAP17269.raw", OutputWorkspace="MAP17269")
#print "***have mask"
#sample_ws = mtd[sample]
#print "***applying mask"
#MaskDetectors(sample_ws, MaskedWorkspace=diag_mask)
#print "***mask applied"
	
# Save the masked spectra nmubers to a simple ASCII file for comparison
#self.saved_diag_file = os.path.join(mtd.settings['defaultsave.directory'], 'CurrentDirectInelasticDiag.txt')
#handle = file(self.saved_diag_file, 'w')
#for index in range(sample_ws.getNumberHistograms()):
#    if sample_ws.getDetector(index).isMasked():
#        spec_no = sample_ws.getSpectrum(index).getSpectrumNo()
#        handle.write(str(spec_no) + '\n')
#handle.close
