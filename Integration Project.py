"""__author__ = Jonah Rachman"""

# I import the requests module set up in my PyCharm interpreter
# Hit the gear icon in the top right
# Hit the settings button
# Hit the project tab
# Hit the python interpreter button
# Hit the + symbol
# Search for the word requests
# Hit the Install Package button
import requests

# SPRINT 1 REQUIREMENTS

# The end= argument modifies the end of a string
# in this case removing the line separation
print("Both of these print functions will be on the same line ", end="")
print("Both of these print functions will be on the same line")
# The sep= argument modifies the separations between strings
# in this case replacing them with hyphens
print("This", "Will", "Have", "Hyphens", "Instead", "of", "Spaces", sep="-")
# The **(Exponentiation) operator raises an int or float
# to the power of another number
print(2 ** 5)
# The *(Multiplication) operator multiplies an int or float by another number
print(2 * 5)
# The /(Division) operator divides an int or float by another number
print(2 / 5)
# The %(Modulus) operator gives the remainder of the division between two
# number
print(5 % 2)
# The //(Floor Division) operator rounds the result of the dvision
# between two numbers down to the closest number
print(5 // 2)
# The +(Addition) operator adds an int or float to another number
print(5 + 2)
# The -(Subtraction) operator subtracts an int or float from another number
print(5 - 2)
# +(Concatenation) string operator combines two strings
print("I am concatenating " + "these strings")
# The *(Repetition) string operator repeats a string
# a specified number of times
print("Hello" * 10)

# SPRINT 2 REQUIREMENTS

# Shortcut Operators modify a variable assignment using shorthand operators
num = 100
num += 100
num -= 100
num *= 1
num /= 2
num %= 30
num **= 1
num //= 10
# Will print 2.0 after all reassignment operations
print(num)
print("")
print("")
print("** SPRINT REQUIREMENTS ** \n \n")


# This program takes in an address given by the user
# uses an API made by Mapbox to geocode the address
# Passes the information to an API made by OpenWeatherMap
# and returns the current weather information
# depending on the users desired data
def get_weather(_lat, _lon):
    """
    This function uses the latitude and longitude given by the Mapbox API to
    request the current weather data from that location
    :param _lat: The latitude of the location the user entered
    :param _lon: The longitude of the location the user entered
    """
    # I define a few variable to make a request to OpenWeather using
    # their API and my assigned API key
    api_key = "685650d422a3808bcfec9f49e086ff48"
    # I format the string here to accept
    # different arguments put into the get_weather function
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=" \
          f"{_lat}&lon={_lon}&appid={api_key}&units=imperial"
    response = requests.get(url)
    # I parse the raw data given by my API request into a dictionary format
    weather_data = response.json()
    # I check if the city was found using the "cod" tag in the given data
    if weather_data["cod"] != "404":
        # I set multiple variables to the corresponding
        # data using its tag in the dictionary
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        pressure = weather_data["main"]["pressure"]
        feels_like = weather_data["main"]["feels_like"]
        temp_min = weather_data["main"]["temp_min"]
        temp_max = weather_data["main"]["temp_max"]
        visibility = weather_data["visibility"]
        wind_speed = weather_data["wind"]["speed"]
        weather_description = weather_data["weather"][0]["description"]
        print("Data Available: "
              "\n1. Temperature "
              "\n2. Humidity "
              "\n3. Pressure "
              "\n4. Feels_Like "
              "\n5. Temp_Min "
              "\n6. Temp_Max "
              "\n7. Visibility "
              "\n8. Wind_Speed")
        requested_data = input("\nPlease enter the weather data you want"
                               " using their numbers separated by a space"
                               " Ex.(3 4 5)\nFor only a general description,"
                               " enter nothing: \n").split()
        if "1" in requested_data:
            print("Temperature: " + str(temperature) + " F°")
        if "2" in requested_data:
            print("Humidity: " + str(humidity) + " %")
        if "3" in requested_data:
            print("Pressure: " + str(pressure) + " hPa")
        if "4" in requested_data:
            print("Feels_Like: " + str(feels_like) + " F°")
        if "5" in requested_data:
            print("Temp_Min: " + str(temp_min) + " F°")
        if "6" in requested_data:
            print("Temp_Max: " + str(temp_max) + " F°")
        if "7" in requested_data:
            if visibility == 10000:
                print("Visibility: " + str(visibility) + "(max)" + " ft")
            else:
                print("Visibility: " + str(visibility) + " ft")
        if "8" in requested_data:
            print("Wind_Speed: " + str(wind_speed) + " Mph")
        print("General Description: " + weather_description)
    else:
        print("City not found")


def main():
    """
        This function uses the latitude and longitude given by the Mapbox API
         to request the current weather data from that location
        """
    user_loop = True
    while user_loop:
        search_text = ""
        address = (
            input("\nPlease enter a location "
                  " (be specific): ")).split()
        if address:
            for i in address:
                search_text += (i + "%20")

            search_text = search_text[:-3]
            geo_url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/" \
                      f"{search_text}.json?access_token=pk" \
                      f".eyJ1Ijoiam9uYWgtcmFjaG1hbiIsImEiOiJjbGR1dmtrdT" \
                      f"kwOWphM3JycXY1djl4MGlrIn0.e_8d_18Vpu76QYvnrRHMfw"
            geo_response = requests.get(geo_url)
            location_data = geo_response.json()
            if geo_response.status_code != "404":
                try:
                    latitude = (location_data["features"][2]["center"][1])
                    longitude = (location_data["features"][2]["center"][0])
                    print("\nAddress found:",
                          location_data["features"][2]["place_name"] + "\n")
                except IndexError:
                    print("\nAddress not found")
                    latitude = "null"
                    longitude = "null"
            else:
                print("API Error, check mapbox account")
            try:
                # I think this warning is just incorrect
                get_weather(latitude, longitude)
            except KeyError:
                pass
        else:
            print("\n You did not enter anything!")
        correct_input = False
        while not correct_input:
            user_loop = input(
                "\nWould you like to enter another address (Yes or No)?\n")
            if user_loop.lower() == "yes" or user_loop.lower() == "y":
                user_loop = True
                correct_input = True
            elif user_loop.lower() == "no" or user_loop.lower() == "n":
                user_loop = False
                correct_input = True
            else:
                print("That was not a correct input!")
                correct_input = False


if __name__ == "__main__":
    main()
# Future Goals for this program
# Allow user to input city and country
# without having to convert to lat and lon *COMPLETED
# Research more data the API can give and allow
# for more weather options *COMPLETED
# Request data from previous dates
# to show temperature trends *Have to pay for that API :(
# Allow user to specify what weather information they want *COMPLETED
