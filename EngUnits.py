#!/usr/bin/env python3

'''Module designed to make common engineering unit conversions.'''

# ======== Functions ======================================================================

def convert(value, uin, uout):
    """Currently supported units:
    Mass: 'kg', 'g', 'metric ton', 'lbm', 'oz', 'ton'
    Length: 'm', 'cm', 'mm', 'mum', 'A', 'in', 'ft', 'yd', 'mile'
    Volume: 'm3', 'L', 'cm3', 'mL', 'ft3', 'imp gal', 'gal', 'qt'
    Force: 'N', 'kg-m/s2', 'dyne', 'g-m/s2', 'lbf', 'lbm-ft/s2'
    Pressure: 'atm', 'Pa', 'kPa', 'bar', 'dyne/cm2', 'mmHg', 'torr', 'mH2O', 'lbf/in2', 'psi', 'ftH2O', 'inHg'
    Energy: 'J', 'N-m', 'ergs', 'dyne-cm', 'kW-h', 'cal', 'ft-lbf', 'Btu'
    Power: 'W', 'J/s', 'cal/s', 'ft-lbf/s', 'Btu/s', 'hp'
    Moles: 'mol', 'lbmol'

    Units to add:
    """

    umass = ['kg', 'g', 'metric ton', 'lbm', 'oz', 'ton']
    ulength = ['m', 'cm', 'mm', 'mum', 'A', 'in', 'ft', 'yd', 'mile']
    uvolume = ['m3', 'L', 'cm3', 'mL', 'ft3', 'imp gal', 'gal', 'qt']
    uforce = ['N', 'kg-m/s2', 'dyne', 'g-m/s2', 'lbf', 'lbm-ft/s2']
    upressure = ['atm', 'Pa', 'kPa', 'bar', 'dyne/cm2', 'mmHg', 'torr', 'mH2O',
                 'lbf/in2', 'psi', 'ftH2O', 'inHg']
    uenergy = ['J', 'N-m', 'ergs', 'dyne-cm', 'kW-h', 'cal', 'ft-lbf', 'Btu']
    upower = ['W', 'J/s', 'cal/s', 'ft-lbf/s', 'Btu/s', 'hp']
    umol = ['mol', 'lbmol']

    # Dictionaries contain coefficients with respect to one of the units
    # The units in are divided by their coefficient, then multiplied by 
    # the units out coefficient
    mass_out = {'kg':1, 'g':1000, 'metric ton':0.001, 'lbm':2.20462, 
                'oz':35.27392, 'ton':5e-4/0.453593}
    length_out = {'m':1, 'cm':100, 'mm':1000, 'mum':1e6, 'A':1e10, 
                  'in':39.37, 'ft':3.2808, 'yd':1.0936, 'mile':0.0006214}
    volume_out = {'m3':1, 'L':1000, 'cm3':1e6, 'mL':1e6, 'ft3':35.3145, 
                  'imp gal':220.83, 'gal':264.17, 'qt':1056.68}
    force_out = {'N':1, 'kg-m/s2':1, 'dyne':1e5, 'g-m/s2':1e5, 'lbf':0.22481, 
                 'lbm-ft/s2':32.174*0.22481}
    pressure_out = {'atm':1, 'Pa':1.01325e5, 'kPa':101.325, 'bar':1.01325,
                    'dyne/cm2':1.01325e6, 'mmHg':760, 'mH2O':10.333, 
                    'lbf/in2':14.696, 'psi':14.696, 'ftH2O':33.9, 'inHg':29.921}
    energy_out = {'J':1, 'N-m':1, 'ergs':1e7, 'dyne-cm':1e7, 'kW-h':2.778e-7, 
                  'cal':0.23901, 'ft-lbf':0.7376, 'Btu':9.486e-4}
    power_out = {'W':1, 'J/s':1, 'cal/s':0.23901, 'ft-lbf/s':0.7376, 
                 'Btu/s':9.486e-4, 'hp':1.341e-3}
    moles_out = {'mol':453.59237, 'lbmol':1}

    types_list = [mass_out, length_out, volume_out, force_out, pressure_out, 
                  energy_out, power_out, moles_out]

    found = False
    for udic in types_list:
        if uin in udic.keys():
            units = udic
            found = True
            break

    if not found:
        print(f"Unit {uin} not supported")
        return None

    coef_uin = units[uin]
    for key in units.keys():
        units[key] = units[key]/coef_uin

    coef = units[uout]
    # print(coef)
    value_out = value*coef

    return value_out

def getR(units):
    '''Possible inputs are:
        Pa, bar, atm, mmHg, atmR, psi, J, cal, Btu
    '''
    all_R = {'Pa':8.314, 
             'bar':0.08314, 
             'atm':0.08206, 
             'mmHg':62.36, 
             'atmR':0.7302, 
             'psi':10.73, 
             'J':8.314, 
             'cal':1.987, 
             'Btu':1.987}

    if units in all_R.keys():
        R = all_R[units]
    else:
        print("Not a valid unit for function GetR.")
        return

    return R


# =========== Hidden Classes ======================================================
class _Rgas:
    '''To see options run: ```print(Rgas())```'''
    def __init__(self):

        self.Pa = 8.314
        self.bar = 0.08314
        self.atm = 0.08206
        self.mmHg = 62.36
        self.atmR = 0.7302
        self.psi = 10.73
        self.J = 8.314
        self.cal = 1.987
        self.Btu = 1.987

    def __str__(self):
        # print("R Gas Constant:")
        # print("\nUnits\t\t\tAttribute Name")
        # print('-'*40)
        # print("m3-Pa/(mol-K)\t\tPa")
        # print("L-bar/(mol-K)\t\tbar")
        # print("L-atm/(mol-K)\t\tatm")
        # print("L-mmHg/(mol-K)\t\tmmHg")
        # print("ft3-atm/(lbmol-R)\tatmR")
        # print("ft3-psia/(lbmol-R)\tpsi")
        # print("J/(mol-K)\t\tJ")
        # print("cal/(mol-K)\t\tcal")
        # print("Btu/(lb-mol-R)\t\tBtu")

        string = f"""\

R Gas Constant:

Units               Accessor    Value
--------------------------------------
m3-Pa/(mol-K)       Pa          {self.Pa}
L-bar/(mol-K)       bar         {self.bar}
L-atm/(mol-K)       atm         {self.atm}
L-mmHg/(mol-K)      mmHg        {self.mmHg}
ft3-atm/(lbmol-R)   atmR        {self.atmR}
ft3-psia/(lbmol-R)  psi         {self.psi}
J/(mol-K)           J           {self.J}
cal/(mol-K)         cal         {self.cal}
Btu/(lb-mol-R)      Btu         {self.Btu}"""
        return string

# ====== Data ====================================================

Rgas = _Rgas()