
co2_comp = input('What is the CO2 composition?')
n2_comp = input('What is the n2 composition?')
h2s_comp = input('What is the h2s composition?')
h2o_comp = input('What is the h2o composition?')
gas_gravity = input('What is the measured gas gravity?')

 # convert inputs to numerals
co2_comp = float(co2_comp)
n2_comp = float(n2_comp)
h2s_comp = float(h2s_comp)
h2o_comp = float(h2o_comp)
gas_gravity = float(gas_gravity)

# the if statement

if co2_comp <= 0.12 or n2_comp <= 0.03 or h2s_comp<=0:
    corr_gas_gravity = (gas_gravity- 1.1767*h2s_comp -1.5196*co2_comp - 0.9672*n2_comp - 0.622*h2o_comp)/(1- h2s_comp - co2_comp - n2_comp - h2o_comp)
    print('The corrected gas gravity is', corr_gas_gravity)
    
#determing pseudocritical pressure and pseudo critical temperature

p_pch=756.8-131*corr_gas_gravity-3.6*corr_gas_gravity**2
t_pch= 169.2 + (349.5*corr_gas_gravity) - (74.0*corr_gas_gravity**2)



# displaying the results.
print( 'The hydrocarbon pseudo-critical pressure is',p_pch,'psia')
print('The hydrocarbon pseudo-critical temperature is',t_pch,'deg Rankine')

# determing pseudoreduced pressure and pseudoreduced temperature

pseudo_red_pre=(1-co2_comp-n2_comp-h2s_comp-h2o_comp)*p_pch + 1306*h2s_comp+1071*co2_comp+493.1*n2_comp+3200.1*h2o_comp

pseudo_red_temp=(1-co2_comp-n2_comp-h2s_comp-h2o_comp)*t_pch +672.35*h2s_comp+547.58*co2_comp+227.16*n2_comp+1164.9*h2o_comp



print( 'The hydrocarbon pseudo-reduced pressure is',pseudo_red_pre,'psia')
print( 'The hydrocarbon pseudo-reduced temperatureis',pseudo_red_temp,'deg Rankine')

















