import pandas as pd
import streamlit as st
from PIL import Image
image = Image.open('log.jpeg')
st.image(image, use_column_width=True)


st.header('Please select the length of the peptides:')

number = st.number_input("Input length", value=5, placeholder="Type a number...")
st.write('The current length is ', number)

st.header('1. Type or paste amino acid sequence of peptide in single letter code:')
sequnce_input1 = '>Example 1\nMSSKTTPAPVYIWTADEAIKFLKEWNFSLGIILLFITIILQFGYTSRSMFVYVIKMIILWLMWPLTIILTIFNCVYALNNVYLGLSIVFTIVAIIMWIVYFVNSIRLFIRTGSFWSFNPETNNLMCIDMKGTMYVRPIIEDYHTLTVTIIRGHLYIQGIKLGTGYSWADLPAYMTVAKVTHLCTYKRGFLDRISDTSGFAVYVKSKVGNYRLPSTQKGSGMDTALLRNNI'
seq_a1 = st.text_area('Sequnce Input 1', sequnce_input1, height=100)
seq_a2 = seq_a1.splitlines()
seq_a3 = seq_a2[1:]
seq_a4 = ''.join(seq_a3)

st.header('2. Type or paste amino acid sequence of peptide in single letter code:')
sequnce_input2 = '>Example 2\nMADTIFGSGNDQWVCPNDRQLALRAKLQTGWSVHTYQTEKQRRKQHLSPAEVEAILQVIQRAERLDVLEQQRIGRLVERLETMRRNVMGNGLSQCLLCGEVLGFLGSSSVFCKDCRKKVCTKCGIEASPGQKRPLWLCKICSEQREVWKRSGAWFYKGLPKYILPLKTPGRADDPHFRPLPTEPAEREPRSSETSRIYTWARGRVVSSDSDSDSDLSSSSLEDRLPSTGVRDRKGDKPWKESGGSVEAPRMGFTHPPGHLSGCQSSLASGETGTGSADPPGGPRPGLTRRAPVKDTPGRAPAADAAPAGPSSCLG'
seq_b1 = st.text_area('Sequnce Input2', sequnce_input2, height=100)
seq_b2 = seq_b1.splitlines()
seq_b3 = seq_b2[1:]
seq_b4 = ''.join(seq_b3)

st.button("Start analysis", type="primary")

if st.button('Stop analysis'):
    st.write('Thank you for using Alignmentaj!')
else:
    def pentapeptides():
        l = []
        c = len(seq_a4)
        st.title(':blue[_Results_]')
        for i in range(c):
            if len(seq_a4[i:i + number]) < number:
                break
            if seq_a4[i:i + number] in seq_b4:
                seq_a4[i:i + number]
                l.append(bool(True))
            else:
                l.append(False)
        my_list = any(l)
        if my_list == False:
            st.write('Alignmentaj did not find similar peptides in your sequnces!')
        st.write('*Thank you for using Alignmentaj!!!*')





pentapeptides()
