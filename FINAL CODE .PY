# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:18:49 2023

@author: swetha
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 3, 2023

@author: swetha
"""

import pandas as pd
import matplotlib.pyplot as plt

# Function to read data from a CSV file
def read_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Function for Visualization 1: Multiple Line Chart to Compare Countries
def multiple_line_chart(data, selected_countries, years):
    country_data = data[data["Country Name"].isin(selected_countries)]

    plt.figure(figsize=(16, 8))
    for country in selected_countries:
        country_row = country_data[country_data["Country Name"] == country]
        plt.plot(years, country_row[years].values.tolist()[0], marker='o', label=country)

    plt.title("Electricity Production from Coal Sources (2005-2015)")
    plt.figtext(0.5,-0.1,"electricity production for coal sources over 2005 to 2015 years of time /n among various countries", ha="center",fontsize=12)
    plt.xlabel("Year")
    plt.ylabel("% of Total Electricity Production")
    plt.grid(True)
    plt.legend()
    plt.show()

#Function for Visualization 2: Bar Chart for a Specific Year
def bar_chart_for_year(data, selected_year):
    year_data = data[data[selected_year].notna()]
    plt.figure(figsize=(10, 6))
    plt.bar(year_data["Country Name"], year_data[selected_year])
    plt.title(f"Electricity Production from Coal Sources in {selected_year}")
    plt.xlabel("Country")
    plt.ylabel("% of Total Electricity Production")
    plt.xticks(rotation=90)
    plt.grid(axis="y")
    plt.show()
    
# Function for Visualization 3: Pie Chart for a Specific Country
def pie_chart(data, country_name, years):
    country_data = data[data["Country Name"] == country_name]
    production_data = country_data[years].values.tolist()[0]
    labels = years

    # Explode one slice (optional for emphasis)
    explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    plt.figure(figsize=(8, 8))
    plt.pie(production_data, labels=labels, autopct='%1.1f%%', startangle=140, pctdistance=0.85, explode=explode)
    plt.title(f"Electricity Production from Coal Sources in {country_name} (2005-2015)")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

# Main function to run the program
def main():
    file_path = r"C:\Users\navee\Downloads\Electricity production from coal sources (% of total).csv"
    data = read_data(file_path)

    years = ["2005 [YR2005]", "2006 [YR2006]", "2007 [YR2007]", "2008 [YR2008]", "2009 [YR2009]", "2010 [YR2010]", "2011 [YR2011]", "2012 [YR2012]", "2013 [YR2013]", "2014 [YR2014]", "2015 [YR2015]"]
    selected_countries = ["Germany", "Poland", "United Kingdom", "United States", "India"]
    multiple_line_chart(data, selected_countries, years)
    bar_chart_for_year(data, "2015 [YR2015]")
    pie_chart(data, "Germany", years)  # You can add this line to call the pie chart function

if __name__ == "__main__":
    main()
