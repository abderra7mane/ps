import pscmd


def main():
    cmd = pscmd.PsCmd()
    try:
        cmd.cmdloop()
    except KeyboardInterrupt:
        print "\nCtrl-C captured. terminating"


if __name__ == "__main__":
    main()
