import sys
import filesearching

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write(" Usage - python <filename> <extension>\n")
        print(" extension - py,txt,7z,bz,mp3,pdf,exe ... ")
        sys.exit()
    else:
        try:
            ans = filesearching.searching_files()
        except Exception as err:
            print(str(err))
            sys.exit()
        if ans == 1:
            print(" Something is found \n")
            print(" -> Check NAMES \n -> Check full PATHS ")
            choice = input("\n Tell me ?\n NAMES / PATHS : ").lower()
            filesearching.show_terminal(choice)
            send_choice = input(
                "\n --- Send files -> found_files ---\n Yes / No : "
            ).lower()
            filesearching.sending_files(send_choice)
        else:
            print(" Nothing Found here ")
            exit()
    print("\n -- Thanks ")
