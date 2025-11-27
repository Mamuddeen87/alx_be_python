from datetime import datetime, timedelta

def display_current_datetime():
    """Display current date and time in YYYY-MM-DD HH:MM:SS format"""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date  # returning in case we need it later


def calculate_future_date(current_date, days_to_add):
    """
    Calculate the future date by adding specified number of days
    to the given current_date
    """
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate future date
    try:
        days_input = int(input("Enter the number of days to add to the current date: ").strip())
        calculate_future_date(current_date, days_input)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")


if __name__ == "__main__":
    main()

