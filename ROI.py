def roi_calculator():
    # Plant information
    production_rate = 36.5  # Ton/hr
    availability = 0.8  # 80%
    product_rate = 1100  # Euro/ton

    # User inputs
    downtime_count = int(input("Enter the number of downtimes: "))
    downtime_reduction_percentage = float(input("Enter the expected reduction percentage: "))
    DT_ratio = downtime_reduction_percentage*0.01
    Investment = float(input("Enter the investment amount: "))

    total_downtime_duration = 0
    for i in range(1, downtime_count + 1):
        downtime_duration = float(input(f"Enter the duration of downtime {i} in hours: "))
        total_downtime_duration += downtime_duration

    # Original production calculation
    Initial_production = production_rate * availability * ((24*365) - total_downtime_duration)

    # Elevated production calculation
    reduced_downtime_duration = total_downtime_duration * (1 - DT_ratio)
    Increased_production = production_rate * availability * ((24*365) - reduced_downtime_duration)

    # Revenue calculation
    original_revenue = Initial_production * product_rate
    Elevated_revenue = Increased_production * product_rate
    Savings = Elevated_revenue-original_revenue

    # ROI calculation
    roi = Investment/ Savings #in years

    # Display results
    print("\nROI Calculator Results:")
    print(f"Original Production: {Initial_production} Tons")
    print(f"Elevated production: {Increased_production} Tons")
    print(f"Savings: {Savings} Euros")
    print(f"ROI: {roi:.2f} Years")

# Run the ROI calculator
roi_calculator()