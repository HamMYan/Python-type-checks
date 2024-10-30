from typing import Union, List, Dict, Callable


def formatter_wo_dash(name: str, surname: str) -> str:
    return f"{name}  {surname} "


def formatter_with_dash(name: str, surname: str) -> str:
    return f"{name} - {surname} "


def get_full_name(name: str, surname: str, formater: Callable) -> str:
    return formater(name, surname)


def friends_list(username: str, list_of_friends: List[Union[int, str]]) -> str:
    output = f"{username}'s friends \n"
    for user in list_of_friends:
        output += f"{user}\n"

    return output


def country_info(countries: Dict[str, List[str]]) -> str:
    output = ""
    for country, cities in countries.items():
        output += f"{country}:\n"
        for city in cities:
            output += f" -{city},\n"
        output += "\n"

    return output


# countries = {
#     "USA": ["Charlotte", "New York", "Glendale"],
#     "Armenia": ["Yerevan", "Sisian", "Gyumri"],
# }

print(get_full_name("John","Smith",formatter_with_dash))
print(get_full_name("John","Smith",formatter_wo_dash))

# print(country_info(countries))

# print(friends_list("Andrew", ["Adam Smith", "Johnny Depp", 5, "Brad Pitt"]))

# print(get_full_name("Anna","Anyan",30.2))
