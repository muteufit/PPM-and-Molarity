def PPMToMolar():
    PPM = float(input("Enter PPM: "))
    molar_weight = float(input("Enter molar mass (g/mol): "))
    density = float(input("Enter density (g/mL): "))
    molarity = (PPM / 1e6) * (density / molar_weight)
    return molarity


def MolarToPPM():
    molarity = float(input("Enter Molarity (M): "))
    molar_mass = float(input("Enter molar mass (g/mol): "))
    density = float(input("Enter density (g/mL): "))
    PPM = (molarity * molar_mass * 1e6) / density    
    return PPM


