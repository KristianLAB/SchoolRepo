from dataclasses import dataclass

DELIMITER = ";"


@dataclass
class TIMESTAMP:
    weekday: str = ""
    hour: str = ""
    consumption: float = 0.0
    price: float = 0.0


@dataclass
class DAY_USAGE:
    weekday: str = ""
    usage: float = 0.0
    cost: float = 0.0


def read_timestamps(filename: str) -> list[TIMESTAMP]:
    timestamps: list[TIMESTAMP] = []
    print(f'Reading file "{filename}".')

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                row = line.rstrip()
                if row == "":
                    continue

                columns = row.split(DELIMITER)
                ts = TIMESTAMP()

                ts.weekday = columns[0]
                ts.hour = columns[1]
                ts.consumption = float(columns[2])
                ts.price = float(columns[3])

                columns.clear()
                timestamps.append(ts)

    except FileNotFoundError:
        print("Error: File not found.")
        return []

    return timestamps


def analyse(timestamps: list[TIMESTAMP]) -> list[DAY_USAGE]:
    print("Analysing timestamps.")


    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturnday", "Sunday"
    ]

    results: list[DAY_USAGE] = []


    for day in days:
        du = DAY_USAGE()
        du.weekday = day
        du.usage = 0.0
        du.cost = 0.0
        results.append(du)


    for ts in timestamps:
        for result in results:
            if ts.weekday == result.weekday:
                result.usage += ts.consumption
                result.cost += ts.consumption * ts.price

    return results


def display(results: list[DAY_USAGE]):
    print("Displaying results.")
    print("### Electricity consumption summary ###")

    for r in results:
        print(f" - {r.weekday} usage {r.usage:.2f} kWh, cost {r.cost:.2f} €")

    print("### Electricity consumption summary ###")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")

    timestamps = read_timestamps(filename)
    results = analyse(timestamps)
    display(results)

    print("Program ending.")


if __name__ == "__main__":
    main()