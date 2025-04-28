import argparse
from pymongo import MongoClient
from dataBase import client, collection

#aljrlwjr
def greet():
 

    print("welcome in notes app \n")


greet()


def inputs():
    parser = argparse.ArgumentParser(description="parser")
    subparser = parser.add_subparsers(dest="command")
    addParser = subparser.add_parser("add")
    addParser.add_argument("noteName", type=str, help="note name ")
    addParser.add_argument("content", nargs="+", help="note content")
  

    editParser = subparser.add_parser("edit")
    editParser.add_argument("noteNum", help="note number")
    editParser.add_argument("content", nargs="+", help="the new note content")

    delParser = subparser.add_parser("delete")
    delParser.add_argument("noteNum", help="note number")

    PrintParser = subparser.add_parser("print")
    #sjrljljr
    showParser = subparser.add_parser("show")
    showParser.add_argument("noteNum", type=int, help="note number")
    args = parser.parse_args()
    return {"args": args}



def add(name, content):
    document = {"name": name, "content": content}
    #jskkkskll
    collection.insert_one(document)



def getNotes():
    notes = collection.find()
    return {"notes": notes}
#slslslsllelelell

def size(notes):
    i = 0
#aljlajewljarwljarwejrjklejlwerjwelljkrewjkl
    for note in notes:
        i += 1
    return i


def printNotes(notes, size):
    if size == 0:
        print("there are no notes !!!")
        return
    i = 0
    for note in notes:
        i += 1
        print(i, note["name"])


def showNote(noteNumber, size):
    if size < noteNumber:
        print(f"sorry there is  no note called::{noteNumber}")
        return
    note = getNotes()["notes"][int(noteNumber)-1]
    if note:
        print(note)
        return
    print("there is no note  called: {}".format(note["name"]).capitalize())
    return


def checkIfAll(name):#sjrwlrwlrw;lj
    if name.lower() == "all":
        return True
    return False


def delete(num):
    if checkIfAll(num):
        collection.delete_many({})
        print("all notes deleted  successfly!")
        return
    notes = getNotes()["notes"]
    if size(notes) < int(num) or num.isalpha():
        print(f"there is no  note called: {num}")
        print(f"please type  to see all   the notes (python3 engine.py print)")
        return
    note = getNotes()["notes"][int(num)-1]

    collection.delete_one(note)
    print(f"note {note["name"]} deleted  successfly!")


def edit(num, content, size):
    if size < int(num) or num.isalpha():
        print(f" there is no note  called: {num}")
        print(f" please type to see  all the notes (python3 engine.py print)")
        return

    note = getNotes()["notes"][int(num)-1]
    collection.update_one(note, {"$set": {"content": content}})
    print(" note edited  successfly  ")


def codeHandler(args):
    command = args.command
    if command == "add":#sjrljrwrwjr
        add(args.noteName, args.content)
    if command == "edit":
        edit(args.noteNum, args.content, size(getNotes()["notes"]))
    if command == "delete":
        delete(args.noteNum, "l")
    if command == "print":#hsrlwwejlrwrrlsjwljr
        printNotes(getNotes()["notes"], size(getNotes()["notes"]))
    if command == "show":
        showNote(args.noteNum, size(getNotes()["notes"]))

#shrlsjr
codeHandler(inputs()["args"])
