import inspect
import time
import sys
import curses

def ErrorHandler(ErrorMessage, TraceMessage, AdditionalInfo, stdscr):
    # Window2.ScrollPrint('ErrorHandler',10,TimeStamp=True)
    #Window4.ScrollPrint('** Just a moment...**',8)
    CallingFunction = inspect.stack()[1][3]
    FinalCleanup(stdscr)
    print("")
    print("")
    print("--------------------------------------------------------------")
    print("ERROR - Function (", CallingFunction, ") has encountered an error. ")
    print(ErrorMessage)
    print("")
    print("")
    print("TRACE")
    print(TraceMessage)
    print("")
    print("")
    if (AdditionalInfo != ""):
        print("Additonal info:", AdditionalInfo)
        print("")
        print("")
    print("--------------------------------------------------------------")
    print("")
    print("")
    time.sleep(1)
    sys.exit('Meshwatch exiting...')


def FinalCleanup(stdscr):
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.curs_set(1)
    curses.endwin()
