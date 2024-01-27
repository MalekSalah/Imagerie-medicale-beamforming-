clear all;
load("RF.mat"); # Load data 
c = 1500 #Speed of sound in water 
global param, c;

# Computer transductor positions
X = param.pitch .* param.ReceivingElts;
X_i = X;
Z =  

