# ----------------------------------------------------------------------
# Name: HW10.py
# Purpose:
#
# Date: 4/30/19
# ----------------------------------------------------------------------
"""

"""
import pandas as pd
import numpy as np


def load_file(filename):
    # read csv into a DataFrame
    df_cars = pd.read_csv(filename, delimiter=',')
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
    print("(Q4)Lowest Fuel Efficiency: ", low_fe_df['Division'],
          low_fe_df['Carline'])
    return low_fe_df['Division'], low_fe_df['Carline']


def q5(df):
    """
    What is the highest combined FE - Conventional Fuel among all wheel drives.
    Use'Drive Desc'. The function must return a float.
    """
    comb_fe = 'Comb FE (Guide) - Conventional Fuel'
    # First narrow down to comb FE among wheel drives
    all_wheel_df = df.loc[df['Drive Desc'] == 'All Wheel Drive']
    # Next find highest combined FE - Conventional Fuel
    print("(Q5)Highest FE among wheel drives:",
          max(all_wheel_df[comb_fe]))
    return max(all_wheel_df[comb_fe])


def q6(df):
    """
    Which car line has the largest difference between Highway and City Fuel
    efficiency - Conventional Fuel?
    """
    hwy_fe = 'Hwy FE (Guide) - Conventional Fuel'
    city_fe = 'City FE (Guide) - Conventional Fuel'
    df['fe_diff'] = df[hwy_fe] - df[city_fe]
    print("(Q6)Highest FE diff between Hwy and City: ",
          df.loc[df['fe_diff'].idxmax()]['Carline'])
    return df.loc[df['fe_diff'].idxmax()]['Carline']


def q7(df):
    """
    What is the average annual fuel cost (Annual Fuel1 Cost - Conventional
    Fuel) of supercharged cars?
    """
    ann_fe = 'Annual Fuel1 Cost - Conventional Fuel'
    # First narrow down to supercharged cars
    super_df = df.loc[df['Air Aspiration Method Desc'] == 'Supercharged']
    print("(Q7)Average annual FE cost of supercharged cars: ",
          super_df[ann_fe].mean())
    return super_df[ann_fe].mean()


def q8(df):
    """
    What SUV has the lowest annual fuel cost?   Use "Carline Class Desc" to
    identify SUVs.
    """
    ann_fe = 'Annual Fuel1 Cost - Conventional Fuel'
    # Narrow down to SUVs
    suv_df = df[df['Carline Class Desc'].str.contains('SUV', na=False)]
    print("(Q8)Lowest annual FE cost of SUVs: ",
          suv_df.loc[suv_df[ann_fe].idxmin()]['Carline'])
    return suv_df.loc[suv_df[ann_fe].idxmin()]['Carline']


def q9(df):
    """
    Which manufacturer has the most cars with manual transmission?
    The function must return a string.
    :param df:
    :return:
    """
    # Narrow down to manual transmission cars
    tr_df = df.loc[df['Transmission'].str.contains('Manual', na=False)]
    print("(Q9)Mfr with most manual transmission cars: ",
          tr_df['Mfr Name'].value_counts().idxmax())
    return tr_df['Mfr Name'].value_counts().idxmax()


def q10(df):
    """
    What is the average annual fuel cost by car division?  The function
    must return a Pandas series.
    :param df:
    :return:
    """
    ann_fe = 'Annual Fuel1 Cost - Conventional Fuel'
    print("(Q10)Average annual fuel cost by car division",
          df.groupby('Division').agg({ann_fe: np.average}))
    return df.groupby('Division').agg({ann_fe: np.average})


def q11(df):
    """
    What criteria would you use to buy a car?  Write a function that returns
    your perfect car based on your criteria.  This function must return a
    string representing the perfect carline for you.
    :param df:
    :return:
    """


def test_outputs(df):
    assert (q1(df) == 64)
    assert (q2(df) == 56)
    assert (q3(df) == 58.0)
    assert (q4(df) == ('Bugatti', 'Chiron'))
    assert (q5(df) == 40.0)
    assert (q6(df) == 'CRUZE')
    assert (q7(df) == 2515.4545454545455)
    assert (q8(df) == 'RAV4 HYBRID AWD')
    assert (q9(df) == 'BMW')


def main():
    df = load_file(r"2019 FE Guide.csv")
    test_outputs(df)


if __name__ == '__main__':
    main()