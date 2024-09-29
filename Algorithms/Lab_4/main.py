def print_formatted_list(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i, item in enumerate(result, 1):
            print(f"{i}. {item}")
        print("_____________________________________________________________")
    return wrapper


@print_formatted_list
def common_participants(group, conference, webinar):
    common = group.intersection(conference, webinar)
    return common


@print_formatted_list
def any_participants(group, conference, webinar):
    any_part = group.union(conference, webinar)
    return any_part


@print_formatted_list
def no_participants(group, conference, webinar):
    no_part = group.difference(conference, webinar)
    return no_part


def main():
    group = {"Avierina", "Holod", "Kostenko", "Lubko", "Antonova", "Hortenko"}
    conference = {"Avierina", "Holod", "Kostenko"}
    webinar = {"Lubko", "Antonova", "Avierina"}

    print("Group:", group)
    print("Conference:", conference)
    print("Webinar:", webinar)

    print("\nПриймали участь хоча б в одному заході:")
    any_participants(set(group), set(conference), set(webinar))

    print("\nПриймали участь в обох заходах:")
    common_participants(set(group), set(conference), set(webinar))

    print("\nНе приймали участі в жодному з заходів:")
    no_participants(set(group), set(conference), set(webinar))


if __name__ == '__main__':
    main()


