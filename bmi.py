import pandas as pd

def cm_to_m(height):
    """
    The function returns the height in meter given in centimeter.
  
        Parameters:
            height (float): The height in centimeter.
          
        Returns:
            The height in meter.
    """
    return height/100

def get_BMI(height,weight):
    """
    The function returns the BMI in kg/m^2  given height in m  and weight in Kg.
  
        Parameters:
            height (float): The height in centimeter.
            weight (float): The weight in centimeter.
          
        Returns:
            The BMI in kg/m^2.
    """
    return weight / height**2


def get_category(BMI):
    """
     The function returns the BMI category given BMI in kg/m^2.
  
        Parameters:
            BMI (float): The BMI in kg/m^2.
          
        Returns:
            The category of the BMI.
    """
    if BMI <= 18.4:
        return "Underweight"
    elif BMI <= 24.9:
        return "Normal weight"  
    elif BMI <= 29.9:
        return "Overweight"
    elif BMI <= 34.9:
        return "Moderately obese"
    elif BMI <= 39.9:
        return "Severely obese"
    else:
        return "Very severely obese"

def get_risk(BMI):
    """
     The function returns the risk given BMI in kg/m^2.
  
        Parameters:
            BMI (float): The BMI in kg/m^2.
          
        Returns:
            The risk of the BMI.
    """
    if BMI <= 18.4:
        return "Malnutrition risk"
    elif BMI <= 24.9:
        return "Low risk" 
    elif BMI <= 29.9:
        return "Enhanced risk"
    elif BMI <= 34.9:
        return "Medium risk"
    elif BMI <= 39.9:
        return "High risk"
    else:
        return "Very high risk"

data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

df = pd.DataFrame(data)

# Adding the BMI , BMI Category and Health risk

df["BMI"] = get_BMI(cm_to_m(df["HeightCm"]),df["WeightKg"])
df["BMI Category"] = df["BMI"].apply(lambda x:get_category(x))
df["Health risk"] = df["BMI"].apply(lambda x:get_risk(x))

# Count the total number of overweight people
print(len(df[df["BMI Category"]=="Overweight"]))

# Printing The DataFrame
print(df)