import numpy as np
import pylab as plt
import scipy.linalg as lin

'''acid V & corresponding acid pHs are volumes V of an acid with pH that is sufficient
to acidify the whole volume of planet Earth;
#a fitting of V with respect to pH as V approaches the volume of a drop
#will show the pH necessary for a drop of acid to acidify Earth'''

with plt.xkcd():
    acidV=([1073741824,9932111872,100126425088,1999844147200,500000228376576,999999919882240,100000000041288000,1000000000412880000,99999999999948600000,1.00000000000002E+22,2E+23,5E+23,7E+23,3.7E+24,6.7E+24,8.7E+24,1.17E+25,1.67E+25])
    acidpH=([-13.0830391394209,-12.1168974066818,-11.1133902989402,-9.8129428580012,-7.41496880680599,-7.11393904446908,-5.11393904256859,-4.11393934323688,-2.11397241565759,-0.117266985841803,1.12494250051012,1.4437006358153,1.54407086727358,1.8692328488981,1.92298552143799,1.93951981720181,1.95424294373402,1.96744427970152])
    trendpH=([-12.8691934965321,-11.9489544144276,-10.9931252348977,-9.75446374370773,-7.47042055919558,-7.18369311233599,-5.2787156809444,-4.32622698190478,-2.42124958399656,-0.516272185917106,0.722944182064392,1.10197754322023,1.24116284581662,1.92991093311076,2.17553212629604,2.2835866828115,2.40614017394923,2.55332883305979])


    plt.plot(acidV, acidpH,label=r'pH Calculator')
    plt.plot(acidV, trendpH,label=r'Regression')
    plt.legend(loc='lower right',title='Obtained by:')
    #plt.legend(loc='upper left')    
    
    plt.annotate(
    "pH OF WATER DROP NEEDED TO \nACIDIFY THE WORLD'S OCEAN\n(pH WITH V AS V --> 0.06 mL)",
    xy=(4E+23, -13.45), arrowprops=dict(arrowstyle='->'), xytext=(4E+24, -4))    
        
    plt.xlabel('Volume of acid V, mL')
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.ylabel('pH of acid to acidify with volume V')
    plt.title('Acidic Ocean \n Andrew Ryan, 2013')
    
plt.show()