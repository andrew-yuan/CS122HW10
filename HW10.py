# ----------------------------------------------------------------------
# Name: HW10.py
# Purpose:
#
# Date:
# ----------------------------------------------------------------------
"""

"""
import pandas as pd


def load_file(filename):
    # read csv into a DataFrame
    df_cars = pd.read_csv(filename, delimiter=',')
    # print(df_cars)
    return df_cars


def q1(df):
    """
    How many cars are made by the manufacturer Honda?
    """
    print("(Q1)Number of Honda cars: ", len(df.loc[df['Mfr Name'] == 'Honda']))
    return len(df.loc[df['Mfr Name'] == 'Honda'])


def q2(df):
    """
    How many 'Guzzlers' are there (as indicated by the column 'Guzzler?')
    """
    print("(Q2)Number of Guzzlers: ", (len(df.loc[df['Guzzler?'] == 'G'])))
    return len(df.loc[df['Guzzler?'] == 'G'])


def q3(df):
    """
    What is the value of the highest combined Fuel Efficiency as given by
    "Comb FE (Guide) - Conventional Fuel"?
    """
    comb_fe = 'Comb FE (Guide) - Conventional Fuel'
    print("(Q3)Highest Fuel Efficiency: ",
          df.loc[df[comb_fe].idxmax()][comb_fe])
    return df.loc[df[comb_fe].idxmax()][comb_fe]


def q4(df):
    """
    Which division and car line has the lowest combined FE - Conventional Fuel?
    """
    comb_fe = 'Comb FE (Guide) - Conventional Fuel'
    low_fe_df = df.loc[df[comb_fe].idxmin()]
    print("(Q4)Lowest Fuel Efficiency: Division=", low_fe_df['Division'],
          "Carline=", low_fe_df['Carline'])
    return low_fe_df['Division'], low_fe_df['Carline']


def q5(df):
    """
    What is the highest combined FE - Conventional Fuel among all wheel drives.
    'Drive Desc'.
    """
    comb_fe = 'Comb FE (Guide) - Conventional Fuel'
    # First narrow down to all wheel drives
    all_wheel_df = df.loc[df['Drive Desc'] == 'All Wheel Drive']
    # Next find highest combined FE - Conventional Fuel
    print("(Q5)Highest FE among wheel drives:", all_wheel_df[comb_fe].idxmax())
    return all_wheel_df[comb_fe].idxmax()


def q6(df):
    """
    Which car line has the largest difference between Highway and City Fuel
    efficiency - Conventional Fuel?
    """
    hwy_fe = 'Hwy FE (Guide) - Conventional Fuel'
    city_fe = 'City FE (Guide) - Conventional Fuel'
    print("(Q6)Highest FE diff between Hwy and City: ",
          max(df[hwy_fe] - df[city_fe]))
    return max(df[hwy_fe] - df[city_fe])



def q7(df):
    """
    What is the average annual fuel cost (Annual Fuel1 Cost - Conventional
    Fuel) of supercharged cars?
    """
    ann_fe = 'Annual Fuel1 Cost - Conventional Fuel'
    # First narrow down to supercharged cars
    super_df = df.loc[df['Air Aspiration Method Desc'] == 'Supercharged']
    print("(Q7)Average annual FE cost of supercharged cars: ",
          round(super_df[ann_fe].mean(), 2))
    return super_df[ann_fe].mean()


def q8(df):
    """
    What SUV has the lowest annual fuel cost?   Use "Carline Class Desc" to
    identify SUVs.
    """
    # First narrow down to SUVs
    suv = df['Carline Class Desc'].str.contains('SUV')
    print("q8 : " + suv['Annual Fuel1 Cost - Conventional Fuel'].idmin())
    return suv['Annual Fuel1 Cost - Conventional Fuel'].idmin()


def main():
    df = load_file(r"2019 FE Guide.csv")
    q1(df)
    q2(df)
    q3(df)
    q4(df)
    q5(df)
    q6(df)
    q7(df)
    # q8(df)



if __name__ == '__main__':
    main()