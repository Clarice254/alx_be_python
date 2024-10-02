from datetime import datetime, timedelta
def display_current_datetime():
    """prints the current date and time in 'YYYY-MM-DD HH:MM:SS' format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
def calculate_future_date(number_of_days):
    """Calculates and displays the future date after adding specified days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}.")
def main():
    #Displays the current date
    display_current_datetime()
    #Get number of days to be added from the user
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    #calculate fute date and display
    calculate_future_date(days_to_add)
if __name__ == "__main__":
    main()
