# ==========================================================
# COCOMO COST ESTIMATION
# Project: Transport Ticket System
# ==========================================================

print("==============================================")
print("       COCOMO COST ESTIMATION")
print("       Transport Ticket System")
print("==============================================")

# ----------------------------------------------------------
# INPUT
# ----------------------------------------------------------

# Estimated size of the project in KLOC
# KLOC = Thousand Lines of Code
kloc = float(input("Enter estimated project size (KLOC): "))

# Average monthly salary of one developer
salary = float(input("Enter average monthly salary per developer (₹): "))


# ----------------------------------------------------------
# BASIC COCOMO - ORGANIC MODEL
# ----------------------------------------------------------
# Effort = 2.4 * (KLOC ^ 1.05)
# Development Time = 2.5 * (Effort ^ 0.38)

effort = 2.4 * (kloc ** 1.05)

development_time = 2.5 * (effort ** 0.38)

# Average number of developers
staff = effort / development_time

# Total project cost
cost = effort * salary


# ----------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------

print("\n==============================================")
print("          COCOMO ESTIMATION RESULT")
print("==============================================")

print(f"Project Name       : Transport Ticket System")
print(f"Project Size       : {kloc:.2f} KLOC")
print(f"Effort             : {effort:.2f} Person-Months")
print(f"Development Time   : {development_time:.2f} Months")
print(f"Average Staff      : {staff:.2f} Developers")
print(f"Estimated Cost     : ₹{cost:,.2f}")

print("==============================================")
print("             END OF ESTIMATION")
print("==============================================")
