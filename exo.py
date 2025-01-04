
def main():
    # La notion de compréhension de liste
    username = ["AMine", "Claire", "VALERIe", "KaRIne"]
    username = [u.lower() for u in username]

    print(username)



if __name__ == '__main__':
    main()