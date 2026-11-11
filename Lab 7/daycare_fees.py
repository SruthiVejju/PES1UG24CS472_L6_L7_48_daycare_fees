import math


def parse_enrolment(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Enrolment details must be a non-empty string")

    if text.count(":") != 1:
        raise ValueError("Enter details in age_group:hours format")

    age_group, hours = text.split(":")
    age_group = age_group.strip()
    hours = hours.strip()

    if not age_group or not hours:
        raise ValueError("Age group and hours cannot be empty")

    try:
        hours = float(hours)
    except ValueError:
        raise ValueError("Hours must be a valid number")

    if not math.isfinite(hours) or hours < 0:
        raise ValueError("Hours must be finite and non-negative")

    return age_group.title(), hours


def hours_average(hours_csv):
    if not isinstance(hours_csv, str) or not hours_csv.strip():
        raise ValueError("Weekly hours must be a non-empty string")

    parts = hours_csv.split(",")

    if any(not part.strip() for part in parts):
        raise ValueError("Hours cannot contain empty values")

    try:
        values = [int(part.strip()) for part in parts]
    except ValueError:
        raise ValueError("All weekly hours must be integers")

    return sum(values) // len(values)


def payable_fee(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Fee details must be a non-empty string")

    if text.count("|") != 1:
        raise ValueError("Enter details in fee|discount format")

    fee, discount = text.split("|")
    fee = fee.strip()
    discount = discount.strip()

    if not fee or not discount:
        raise ValueError("Fee and discount cannot be empty")

    try:
        fee = float(fee)
        discount = float(discount)
    except ValueError:
        raise ValueError("Fee and discount must be valid numbers")

    if not math.isfinite(fee) or not math.isfinite(discount):
        raise ValueError("Fee and discount must be finite numbers")

    if fee < 0 or discount < 0:
        raise ValueError("Fee and discount cannot be negative")

    total = fee * 1.18 - discount
    return max(total, 0)


def main():
    print("==== Running parse_enrolment ====")
    user_input = input("Enter age group:hours (e.g. toddler:25): ")
    try:
        result = parse_enrolment(user_input)
        print("Age Group and Hours:", result)
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running hours_average ====")
    user_input = input("Enter weekly hours as CSV (e.g. 20,25,30): ")
    try:
        result = hours_average(user_input)
        print("Average Hours:", result)
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 3000|250): ")
    try:
        result = payable_fee(user_input)
        print("Payable Fee:", result)
    except ValueError as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()