import re


class StringCalculator:

    @staticmethod
    def add(csv_string_of_numbers):
        list_of_numbers = []
        delimeters = [","]

        if csv_string_of_numbers == "":
            return 0

        # if we have the // control code we need to parse out a custom delimeter
        if csv_string_of_numbers[0:2] == "//":
            delimeters = csv_string_of_numbers[2:csv_string_of_numbers.index("\n")].split(",")
            csv_string_of_numbers = csv_string_of_numbers[csv_string_of_numbers.index("\n"):len(csv_string_of_numbers)]

        list_of_negative_numbers = []
        delimeter_regex = "[" + ", ".join(delimeters) + "]"
        for num in re.split(delimeter_regex, csv_string_of_numbers):
            if num != "":
                clean_num = int(num.replace("\n", ""))
                if clean_num < 0:
                    list_of_negative_numbers.append(clean_num)
                elif clean_num < 1000:
                    list_of_numbers.append(clean_num)

        if len(list_of_negative_numbers) > 0:
            raise Exception("Cannot Process Negative Numbers: " + str(list_of_negative_numbers))

        return sum(list_of_numbers)
